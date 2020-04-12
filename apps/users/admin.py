from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.users.models import Users, UserVerifications, Interests

User = get_user_model()

admin.site.register(Users)
admin.site.register(Interests)
admin.site.register(UserVerifications)
