from .models import Project, Task

from rest_framework import serializers



class Taskserializer(serializers.Modelserializer):
    class Meta:
        model = Task
        feilds = ['id', 'name', 'status']


class ProjectSerializer(serializers.ModelSerializer):
    tasks=Taskserializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'tasks']