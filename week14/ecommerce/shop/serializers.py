from rest_framework import serializers
from .models import category_model, product_model, order_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_model
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_model
        fields = ['id', 'title', 'description', 'price', 'stock', 'category', 'image']


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = order_model
        fields = ['id', 'product', 'quantity', 'order_date', 'status']
