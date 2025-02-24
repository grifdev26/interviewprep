from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView

from apps.user_posts.models.post import Post
from apps.user_posts.serializers.post_serializer import PostSerializer

@renderer_classes([JSONRenderer])
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer( posts, many=True)
        # return JsonResponse( {'users': serializer.data} )
        return Response( serializer.data )

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)

        return Response( serializer.errors, status.HTTP_400_BAD_REQUEST )

@renderer_classes([JSONRenderer])
class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Retrieve the book object based on the primary key (pk)
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound(detail=f"Post with id={pk} not found.")

    def get(self, request, pk):
        # Get the specific book by primary key
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        # Get the specific book to update
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()  # Save the updated book
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get the specific book to delete
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)