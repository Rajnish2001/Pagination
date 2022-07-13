from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3 #set the default limit
    limit_query_param = 'mylimit' #replace the limit to custom name
    offset_query_param = 'myoffset' #replace the offset to custom name
    max_limit = 5
    
