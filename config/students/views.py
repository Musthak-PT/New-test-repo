from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# GET all students + POST
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# GET one + PUT + PATCH + DELETE
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer