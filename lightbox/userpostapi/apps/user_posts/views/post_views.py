from django.http import Http404
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer

from apps.user_posts.models.post import Post
from apps.user_posts.serializers.post_serializer import PostSerializer
from apps.user_posts.views.pagination import CustomPagination


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by( 'id')
    serializer_class = PostSerializer
    renderer_classes = [JSONRenderer]
    pagination_class = CustomPagination


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = [JSONRenderer]

    def get_object(self):
        """
        Override to handle object retrieval logic, DRF handles exception automatically.
        """
        try:
            return super().get_object()
        except Http404:
            pk = self.kwargs.get('pk')
            raise NotFound(detail=f"User with id={pk} not found.")