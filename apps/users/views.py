from django_filters import rest_framework as filters

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_200_OK,
    HTTP_404_NOT_FOUND
)

from rest_framework.exceptions import ParseError

from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin
)

from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

# My modules
from apps.users.models import Users, UserVerifications
from apps.users.serializers import UserSerializer, MyTokenObtainPairSerializer, UserLiteSerializer
from apps.users.filters import UserFilter
from apps.users.consts import ErrorMsg
from apps.users.task import main_schedule_task

# Custom method permissions
from apps.contrib.permissions import PostsPermissions


class UsersViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    """
        To registration user and activate account
    """
    queryset = Users.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    def create(self, request, *args, **kwargs):
        """
            {"username":"name", "password":"password", "email":"test@e.e"}
        """
        data = request.data

        password = data.pop("password", None)
        if not password:
            return ParseError(
                ErrorMsg.UserPassword.value
            )

        user_data = self.get_serializer(data=data)
        user_data.is_valid(raise_exception=True)

        user_data.save(password=password)

        main_schedule_task.delay(user_data.data)

        return Response(user_data.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def activate(self, request, **kwargs):
        """
            Example:
                after registration you get email with link to activate account
                link :
                    http://localhost:8000/api/v1/users/activate?token=5393f37748d9deb578383a119976fd05
                and then :
                    get token after click on link and active acc


        """
        token = request.query_params.get("token")
        if not token:
            return ParseError(ErrorMsg.NotToken.value)

        try:
            user_verification = UserVerifications.objects.get(token=token)
        except UserVerifications.DoesNotExist:
            return ParseError(ErrorMsg.TokenDoesNotExist.value)

        if user_verification.is_activate:
            return Response(status=HTTP_404_NOT_FOUND)

        user_verification.is_activate = True
        user_verification.user.is_active = True

        user_verification.user.save()
        user_verification.save()

        return Response(status=HTTP_200_OK)

    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return UserLiteSerializer
        return UserSerializer


class UsersUpdateViewSets(GenericViewSet, UpdateModelMixin):
    """
        To update user info
    """
    serializer_class = UserSerializer
    permission_classes = (PostsPermissions,)

    http_method_names = ["patch"]

    def get_object(self):
        user = Users.objects.get(id=self.kwargs["pk"])
        return user


class LoginViewSet(TokenObtainPairView):
    """
        To create token access
    """
    serializer_class = MyTokenObtainPairSerializer
