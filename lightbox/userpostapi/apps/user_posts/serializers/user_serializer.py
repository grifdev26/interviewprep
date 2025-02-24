from rest_framework import serializers
from apps.user_posts.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']  # Include the fields you want to expose
