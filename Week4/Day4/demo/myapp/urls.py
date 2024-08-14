# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('form/',views.form,name='form'),
    path('delete/<int:id>/', views.delete_form_data, name='delete_form_data'),
  

]