from rest_framework import generics
from rest_framework.exceptions import NotFound

from apps.user_posts.models.post import Post
from apps.user_posts.models.user import User
from apps.user_posts.serializers.user_post_serializer import UserPostSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = UserPostSerializer

    def get_queryset(self):
        # Retrieve the user by the ID in the URL path (e.g., /users/1/posts)
        user_id = self.kwargs['user_id']  # 'user_id' is the path parameter
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound(detail="User not found.")

        # Return the posts of the specific user
        return Post.objects.filter(user=user)


    def perform_create(self, serializer):
        # Automatically set the user to the user in the URL before saving
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound(detail="User not found.")
        # Save the post with the user
        serializer.save(user=user)