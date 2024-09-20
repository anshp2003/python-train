from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class TasklistCreateAPIView(APIView):
    def get(self,request,*arg,**kwargs):
        Task1=Task.objects.all()
        serializer=TaskSerializer(Task1,many=True)
        return Response(serializer.data)
    

    def post(self,request,*arg,**kwarg):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        Task1=get_object_or_404(Task, pk=pk)
        serializer=TaskSerializer(Task1)
        return Response(serializer.data)
    
    def put(self, request, pk, *args, **kwargs):
        # Update a task
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        # Delete a task
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
