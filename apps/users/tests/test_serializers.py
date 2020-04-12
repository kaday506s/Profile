from django.test import TestCase

from apps.users.models import Users, Interests
from apps.users.serializers import UserSerializer, InterestsSerializer


class GroupSerializerTest(TestCase):
    def setUp(self):
        self.interests = Interests.objects.create(
            name='Interests_1'
        )
        self.group_serializer = InterestsSerializer(self.interests)

    def test_contains_expected_fields(self):
        data = self.group_serializer.data

        self.assertEqual(
            set(data.keys()),
            {'name',  'id'}
        )


class UsersSerializerTest(GroupSerializerTest):
    def setUp(self):
        super(UsersSerializerTest, self).setUp()

        self.user = Users.objects.create_user(
            username="test",
            password="1234",
            email="test@mail.re",
            phone="123123123",
            middle_name="Test"
        )
        self.user.interests.add(self.interests)
        self.user.save()

        self.user_serializers = UserSerializer(self.user)

    def test_contains_expected_fields(self):
        data = self.user_serializers.data

        self.assertEqual(
            set(data.keys()),
            {
             "username", "middle_name",
             "phone", "mobile_phone", "sex",
             "first_name", "last_name", "email",
             "is_active", "middle_name",
             "interests", "about_myself",
             "date_birthday", "avatars",
             "images"
            }
        )