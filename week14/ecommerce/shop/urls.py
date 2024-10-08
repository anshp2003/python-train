from django.urls import path
from .views import CategoryListView, productListView, product_listView, OrderCreateView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', productListView.as_view(), name='product-list'),
    path('products/<int:pk>/', product_listView.as_view(), name='product-detail'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]
