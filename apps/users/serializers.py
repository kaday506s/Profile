from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import Users, UserVerifications, Interests, Image


class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    interests = InterestsSerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Users
        fields = [
          "username", "middle_name",
          "phone", "mobile_phone", "sex",
          "first_name", "last_name", "email",
          "is_active", "middle_name",
          "interests", "about_myself",
          "date_birthday", "avatars",
          "images"
        ]

    def create(self, validated_data):
        validated_data["is_active"] = False
        user = Users.objects.create_user(**validated_data)
        user.save()

        UserVerifications.objects.get_or_create(
            user=user
        )

        return user


class UserLiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
          "username", "middle_name",
          "sex", "date_birthday",
          "avatars",
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):

        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data['user'] = {
            "id": self.user.id,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "username": self.user.username,
        }

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
