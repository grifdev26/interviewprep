from rest_framework import serializers

from apps.user_posts.models.post import Post


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']