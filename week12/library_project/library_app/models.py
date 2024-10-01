from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True,null=True)


    def __str__(self):
        return self.name
    

class genres(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self): 
        return self.name
    

class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    publication_date=models.DateField() 
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    genres=models.ManyToManyField(genres,related_name="books")
    is_available=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class BorrowedRecord(models.Model):
    STATUS_CHOICES = [
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="borrowed_records")
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default="Borrowed")
    
    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"