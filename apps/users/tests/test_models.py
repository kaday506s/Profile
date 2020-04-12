from django.test import TestCase
from apps.users.models import Users, Interests, UserVerifications


class InterestsTest(TestCase):
    def setUp(self):
        self.interests = Interests.objects.create(
            name='GroupTest',
        )

    def test_model_fields(self):
        self.assertTrue(hasattr(Interests, 'name'))

    def test_type_model_fields(self):
        self.assertTrue(
            Interests._meta.get_field('name').get_internal_type(),
            'CharField'
        )

    def test_create_group(self):
        self.assertEqual(str(self.interests), self.interests.name)


class UsersTest(InterestsTest):
    def setUp(self):
        super(UsersTest, self).setUp()

    def test_model_fields(self):
        self.assertTrue(hasattr(Users, 'id'))
        self.assertTrue(hasattr(Users, 'first_name'))
        self.assertTrue(hasattr(Users, 'middle_name'))
        self.assertTrue(hasattr(Users, 'last_name'))
        self.assertTrue(hasattr(Users, 'password'))
        self.assertTrue(hasattr(Users, 'email'))
        self.assertTrue(hasattr(Users, 'is_staff'))
        self.assertTrue(hasattr(Users, 'is_superuser'))
        self.assertTrue(hasattr(Users, 'phone'))
        self.assertTrue(hasattr(Users, 'mobile_phone'))
        self.assertTrue(hasattr(Users, 'sex'))
        self.assertTrue(hasattr(Users, 'about_myself'))
        self.assertTrue(hasattr(Users, 'interests'))
        self.assertTrue(hasattr(Users, 'images'))
        self.assertTrue(hasattr(Users, 'avatars'))
        self.assertTrue(hasattr(Users, 'date_birthday'))

    def test_type_model_fields(self):
        self.assertTrue(
            Users._meta.get_field('id').get_internal_type(),
            'IntegerField'
        )
        self.assertTrue(
            Users._meta.get_field('first_name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('last_name').get_internal_type(),
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('password').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('email').get_internal_type,
            'EmailField'
        )
        self.assertTrue(
            Users._meta.get_field('is_staff').get_internal_type,
            'BooleanField'
        )
        self.assertTrue(
            Users._meta.get_field('is_superuser').get_internal_type,
            'BooleanField'
        )
        self.assertTrue(
            Users._meta.get_field('phone').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('username').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('mobile_phone').get_internal_type,
            'CharField'
        )
        self.assertTrue(
            Users._meta.get_field('images').get_internal_type,
            'ManyToManyField'
        )
        self.assertTrue(
            Users._meta.get_field('avatars').get_internal_type,
            'ImageField'
        )
        self.assertTrue(
            Users._meta.get_field('date_birthday').get_internal_type,
            'DateTimeField'
        )
        self.assertTrue(
            Users._meta.get_field('interests').get_internal_type,
            'ManyToManyField'
        )
        self.assertTrue(
            Users._meta.get_field('about_myself').get_internal_type,
            'TextField'
        )

    def test_string_representation(self):
        user = Users.objects.create(
            username='User',
            password="1234",
        )
        user.interests.add(self.interests)
        user.save()
        self.assertEqual(str(user), user.username)




