from django.urls import path
from .views import get_users

urlpatterns = [
    # For function-based view using @api_view decorator
    path('api/users/', get_users, name='get_users'),

    # Or for class-based view using APIView
    # path('api/users/', UserListView.as_view(), name='user_list'),
]
