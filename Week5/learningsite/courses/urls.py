# from django.contrib import admin
from django.urls import path
# from .courses import views
from courses import views
urlpatterns = [
    path('',views.home,name='home'),
]