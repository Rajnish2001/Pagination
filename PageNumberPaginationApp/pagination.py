from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2 #page_size is desided to how much records are show a single page.
    page_query_param = 'q' #change the page to custom name in url page
    page_size_query_param = 'records' #users desided to page size
    max_page_size = 5 #deside the maximum size records of page
    # last_page_strings = 'end' #define the last page searching name
    
