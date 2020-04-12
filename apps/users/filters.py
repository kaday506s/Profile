from django_filters import FilterSet, CharFilter
from apps.users.models import Users


class UserFilter(FilterSet):
    name = CharFilter(lookup_expr='iexact')

    class Meta:
        model = Users
        fields = [
            "email", "sex", "date_birthday",
            "middle_name", "interests", "name"
        ]
