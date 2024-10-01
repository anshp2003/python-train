from django.shortcuts import render
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
# Create your views here.

class ProjectDetailView(generics.RetrieveAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    def get_queryset(self):
        """
        Optionally filter the queryset by task status.
        """
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            # Filter the tasks within the project by status
            queryset = queryset.prefetch_related(
                models.Prefetch('tasks', queryset=Task.objects.filter(status=status))
            )
        return queryset