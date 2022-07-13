from django.shortcuts import render
from rest_framework.generics import ListAPIView
from PageNumberPaginationApp.models import Student
from PageNumberPaginationApp.serializers import StudentSerializer
from PageNumberPaginationApp.pagination import MyPageNumberPagination


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
