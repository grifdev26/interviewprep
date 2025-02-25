from rest_framework.pagination import BasePagination, PageNumberPagination
from rest_framework.response import Response

from project import settings


class CustomPagination(PageNumberPagination):
    page_size = settings.REST_FRAMEWORK.get('PAGE_SIZE', 50)
    max_page_size = settings.REST_FRAMEWORK.get('MAX_PAGE_SIZE', 500)
    page_size_query_param = settings.REST_FRAMEWORK.get('PAGE_SIZE_QUERY_PARAM','page_size')


    # def paginate_queryset(self, queryset, request, view=None):
    #
    #     request_page_size = self.get_page_size(request)
    #     print( f"request page size {request_page_size}")
    #
    #     qs = super().paginate_queryset( queryset, request, view )
    #     if request_page_size == 1 :
    #         print( "!!!   paginated qs !!!!!")
    #         print( qs )
    #     return qs

    def get_paginated_response(self, data):

        response_data = {
            'count': self.page.paginator.count,
            'results': data
        }

        if self.get_next_link() is not None :
            response_data['next'] = self.get_next_link()

        if self.get_previous_link() is not None:
            response_data['previous'] = self.get_previous_link()

        return Response( response_data )
