from django.db import models
from django.contrib.auth.models import User
 
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
 
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='pub_books')
    def __str__(self):
        return self.title
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
 
    def __str__(self):
        return f"Order {self.id} by {self.user.username} - {self.status}"
 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
 
    def __str__(self):
        return f"{self.quantity} x {self.book.title} in Order {self.order.id}"
 
    @property
    def item_total(self):
        # Assuming each Book has a 'price' field for the cost per book
        return self.quantity * self.book.price
 