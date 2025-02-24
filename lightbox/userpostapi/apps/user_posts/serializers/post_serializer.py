from rest_framework import serializers

from apps.user_posts.models.post import Post
from apps.user_posts.models.user import User

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user_id']