from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView

from apps.user_posts.models.user import User
from apps.user_posts.serializers.user_serializer import UserSerializer

@renderer_classes([JSONRenderer])
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer( users, many=True)
        # return JsonResponse( {'users': serializer.data} )
        return Response( serializer.data )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status.HTTP_400_BAD_REQUEST )

@renderer_classes([JSONRenderer])
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Retrieve the book object based on the primary key (pk)
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail=f"User with id={pk} not found.")

    def get(self, request, pk):
        # Get the specific book by primary key
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        # Get the specific book to update
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=False)

        if serializer.is_valid():
            serializer.save()  # Save the updated book
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get the specific book to delete
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
