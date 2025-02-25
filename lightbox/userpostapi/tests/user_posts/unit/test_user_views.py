from django.test import TestCase
from rest_framework.test import APIRequestFactory

from apps.user_posts.views.user_views import UserList


class UserListViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_user_list(self):
        request = self.factory.get("/users/")
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 4)

    def test_create_user(self):
        user_data = {'name': 'Bob Jenkins', 'email': 'bob@email.com'}

        request = self.factory.post("/users/", user_data, format="json")
        response = UserList.as_view()(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Bob Jenkins')
        self.assertEqual(response.data['email'], 'bob@email.com')
