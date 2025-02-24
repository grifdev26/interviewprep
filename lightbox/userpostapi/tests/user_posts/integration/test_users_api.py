
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.user_posts.models.user import User


class UsersApiTests(APITestCase):

    def test_get_users(self):
        response = self.client.get(reverse('users_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_user_creation(self):
        response = self.client.post(reverse('users_api'), {'name': 'Jane Jackson', 'email': 'jane@email.com'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Jane Jackson')
        self.assertEqual(response.data['email'], 'jane@email.com')

    def test_user_creation_bad_input(self):
        response = self.client.post(reverse('users_api'), {'name': ''})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_detail(self):
        url = reverse('user_detail_api', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Joe Smith')
        self.assertEqual(response.data['email'], 'joe.smith@email.com')

    def test_get_user_detail_bad_id(self):
        url = reverse('user_detail_api', kwargs={'pk': 22})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        error_message = response.data['detail']

        self.assertEqual(error_message.code, 'not_found')
        self.assertEqual(error_message, 'User with id=22 not found.')

