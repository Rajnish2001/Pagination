from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'name'
    cursor_query_param = 'mycursor'
