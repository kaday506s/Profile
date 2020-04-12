from rest_framework import permissions

from apps.users.models import Users


class PostsPermissions(permissions.BasePermission):
    """
        Method for checking permissions
    """
    def has_permission(self, request, view, *args, **kwargs):

        if request.user.is_anonymous or \
                not request.user.is_active:
            return False

        if request.user.is_superuser:
            return True

        user = Users.objects.get(id=view.kwargs['pk'])
        if user.username == request.user.username:
            return True

        return False
