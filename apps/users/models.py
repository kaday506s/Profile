from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from hashlib import md5
from datetime import datetime


def random_md5():
    return md5(str(datetime.now()).encode()).hexdigest()


ChoicesSex = (
    ('M', 'Man'),
    ('W', 'Woman'),
)


class Interests(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Interests_name"),
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    """
        To images i am using other DB
    """
    name_desc = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images"
    )

    def __str__(self):
        return self.name_desc


class Users(AbstractUser):
    middle_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Middle name"),
    )
    email = models.EmailField(
        _('email address'),
        blank=False,
        null=False
    )
    phone = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_("Phone"),
    )
    mobile_phone = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_("Mobile phone"),
    )
    sex = models.CharField(
        blank=True,
        max_length=1,
        choices=ChoicesSex
    )

    about_myself = models.TextField(
        blank=True,
        null=True
    )

    interests = models.ManyToManyField(
        Interests,
        blank=True,
    )

    images = models.ManyToManyField(
        Image,
        blank=True,
    )
    avatars = models.ImageField(
        upload_to='images_avatars',
        blank=True,
        null=True
    )
    date_birthday = models.DateTimeField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')

    def __str__(self):
        return self.username


class UserVerifications(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_verifications',
    )
    token = models.CharField(
        max_length=256,
        unique=True,
        default=random_md5,
        null=False,
        verbose_name=_("token")
    )
    is_activate = models.BooleanField(
        default=False
    )
    is_send_mail = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user.username}-{self.is_activate}"
