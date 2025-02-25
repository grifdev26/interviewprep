from django.http import Http404
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.renderers import JSONRenderer

from apps.user_posts.models.user import User
from apps.user_posts.serializers.user_serializer import UserSerializer
from apps.user_posts.views.pagination import CustomPagination


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by( 'id')
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """
        Customize this method to add any additional logic for creating a user if needed.
        """
        serializer.save()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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

    # def update(self, request, *args, **kwargs):
    #     """
    #     PUT method to update a user object. DRF automatically handles validation.
    #     """
    #     return super().update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     """
    #     DELETE method to delete a user object. DRF automatically handles the deletion.
    #     """
    #     return super().destroy(request, *args, **kwargs)