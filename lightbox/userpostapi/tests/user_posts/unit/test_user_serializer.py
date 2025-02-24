from django.test import TestCase

from apps.user_posts.models.user import User
from apps.user_posts.serializers.user_serializer import UserSerializer


class UserSerializerTest(TestCase):
    def test_valid_serialization(self):
        user = User(id="2", name="Mary Jackson", email="mary@email.com")
        serializer = UserSerializer(user)
        expected_data = {'id':2, 'name': 'Mary Jackson', 'email': 'mary@email.com'}
        self.assertEqual(serializer.data, expected_data)

    def test_invalid_serialization(self):

        invalid_data = {"name": ""}  # Missing description
        serializer = UserSerializer( data=invalid_data )
        self.assertFalse(serializer.is_valid())