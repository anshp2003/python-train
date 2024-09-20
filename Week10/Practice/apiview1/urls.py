from django.urls import path
from .views import TasklistCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', TasklistCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]
