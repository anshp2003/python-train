from django.shortcuts import render
from rest_framework.views import APIView
from .models import Author,Book,Publisher,Order, OrderItem
from .serializers import OrderSerializer,publisherSerializer
from rest_framework.response import Response
 
 
class listViewone(APIView):
    def get(self, request, *args, **kwargs):
        publisher=Publisher.objects.all()
        serializer = publisherSerializer(publisher, many=True)
        return Response(serializer.data)
    
 
from django.db.models import F
 
class listView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.prefetch_related(
            'items',
            'items__book__authors',
            'items__book__publisher'
        ).select_related('user')
 
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)