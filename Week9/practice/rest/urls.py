# urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # List and Create view
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, Update, and Delete view
]
