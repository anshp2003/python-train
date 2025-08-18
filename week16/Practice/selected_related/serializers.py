from rest_framework import serializers
from .models import Order, OrderItem, Book, Author, Publisher
 
# class OrderSerializer(serializers.ModelSerializer):
#     items = serializers.SerializerMethodField()
 
#     class Meta:
#         model = Order
#         fields = ['id', 'user', 'order_date', 'status', 'items']
 
#     def get_items(self, obj):
#         # Access `OrderItem` related data with nested `Book`, `Author`, and `Publisher` details
#         items = obj.items.all()
        
#         # Structure each item as nested data
#         serialized_items = [
#             {
#                 "id": item.id,
#                 "quantity": item.quantity,
#                 "book": {
#                     "id": item.book.id,
#                     "title": item.book.title,
#                     "publisher": {
#                         "id": item.book.publisher.id,
#                         "name": item.book.publisher.name
#                     },
#                     "authors": [
#                         {"id": author.id, "name": author.name} for author in item.book.authors.all()
#                     ]
#                 }
#             } for item in items
#         ]
#         return serialized_items
 
 
class publisherSerializer(serializers.ModelSerializer):
    pub_books = serializers.SerializerMethodField()
 
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'pub_books']
 
    def get_pub_books(self, obj):
        
        books = obj.pub_books.all()
        
        serialized_books = [
            {
                "id": book.id,
                "title": book.title,
                "authors": [
                        {"id": author.id, "name": author.name} for author in book.authors.all()
                    ]
            } for book in books
        ]
        return serialized_books
    
 
 
from django.db.models import F
 
 
class OrderSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
 
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date', 'status', 'authors', 'items']
 
    def get_authors(self, obj):
        # Directly retrieve a list of unique author names without using a loop
        return list(
            obj.items.values_list('book__authors').distinct()
        )
 
    def get_items(self, obj):
 
        setattr()
        # Use `values` to directly retrieve book and publisher details without `.annotate()`
        return list(
            obj.items.values(
                'id', 'quantity',
                book_title=F('book__title'),
                publisher_name=F('book__publisher__name')
            )
        )
