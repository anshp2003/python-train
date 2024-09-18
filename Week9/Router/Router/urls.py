"""
URL configuration for Router project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from route.views import BookViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router-generated URLs
urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include(router.urls)),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('route/', include('route.urls')),
# ]
