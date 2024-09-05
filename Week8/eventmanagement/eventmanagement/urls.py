"""
URL configuration for eventmanagement project.

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
# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include the URLs from the 'accounts' app
    path('event/', include('events.urls')),        # Include the URLs from the 'event' app
    path('ticket/', include('ticket.urls')),      # Include the URLs from the 'ticket' app
]

# Serving static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Optional: if you need a catch-all route
# Only add this at the end to avoid conflicts with other URLs
from django.views.generic import TemplateView

urlpatterns += [
    path('<path:path>/', TemplateView.as_view(template_name="404.html")),  # Catch-all for 404 errors
]
