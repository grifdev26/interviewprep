from django.test import TestCase

from apps.user_posts.models.user import User


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Joe Smith", email="joe@email.com")
        self.assertEqual(str(user), "Joe Smith (joe@email.com)")