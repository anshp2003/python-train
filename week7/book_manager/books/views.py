from django.shortcuts import render
# books/views.py
from django.shortcuts import render
from django.views import View
from .models import Book

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})
    
# books/views.py
from django.shortcuts import render, get_object_or_404

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_detail.html', {'book': book})
    
    
# books/views.py
from django.shortcuts import redirect
from .models import Book

class BookCreateView(View):
    def get(self, request):
        return render(request, 'books/book_form.html')

    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    

# books/views.py
class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_form.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_list')
    
# books/views.py
class BookDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_confirm_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list')
