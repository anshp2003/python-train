# views.py
from rest_framework import generics # type: ignore
from rest.models import Book
from .serializers import BookSerializer

# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Fetch all Book records
    serializer_class = BookSerializer  # Use the BookSerializer to convert queryset to JSON

# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
