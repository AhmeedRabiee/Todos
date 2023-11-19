from .serializer import TaskSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Task

# Create your views here.
class GetTasks(generics.ListAPIView):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer
class SingleTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class AddTask(generics.CreateAPIView):
     serializer_class = TaskSerializer
class UpdateTask(generics.UpdateAPIView):
       serializer_class = TaskSerializer
       queryset = Task.objects.all()
       
     