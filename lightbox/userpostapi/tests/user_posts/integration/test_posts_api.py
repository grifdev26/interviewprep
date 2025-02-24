from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.user_posts.models.post import Post
from apps.user_posts.models.user import User


class PostsApiTests(APITestCase):

    def test_get_all_posts(self):
        response = self.client.get(reverse('posts_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)

    def test_post_creation(self):
        new_post = {'title': 'A New Post', 'content': 'Some new content', 'user_id':1}
        response = self.client.post(reverse('posts_api'), new_post)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'A New Post')
        self.assertEqual(response.data['content'], 'Some new content')

    def test_post_creation_blank_title(self):
        new_post = { 'title': '', 'content': 'Some new content', 'user_id':2}
        response = self.client.post(reverse('posts_api'), new_post)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error_message = response.data['title'][0]
        self.assertEqual(error_message.code, 'blank')
        self.assertEqual(error_message, 'This field may not be blank.')

    def test_post_create_bad_user(self):
        new_post = {'title': 'A New Post', 'content': 'Some new content', 'user_id':22}
        response = self.client.post(reverse('posts_api'), new_post)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error_message = response.data['user_id'][0]
        self.assertEqual(error_message.code, 'does_not_exist')
        self.assertEqual(error_message, 'Invalid pk "22" - object does not exist.')



