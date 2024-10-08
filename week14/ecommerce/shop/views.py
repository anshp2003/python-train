from django.shortcuts import render
from .models import category_model,product_model,order_model
from .serializers import ProductSerializer,OrderSerializer,CategorySerializer
from rest_framework import generics

# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset=category_model.objects.all()
    isserializer=CategorySerializer


class productListView(generics.ListAPIView):
    queryset=product_model.objects.all()
    serializer_class=ProductSerializer


class product_listView(generics.RetriveAPIView):
    queryset=product_model.objects.all()
    serializer_class=ProductSerializer

class OrderCreateView(generics.ListAPIView):
    queryset=order_model.objects.all()
    serializer_class=OrderSerializer

