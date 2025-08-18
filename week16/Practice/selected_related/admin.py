from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (               
    Author,
    Publisher,
    Book,Order,OrderItem
)
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)