from django.urls import path
from events import views
from accounts.views import index_view,register_view,login_view,logout_view
from .views import book_ticket
urlpatterns = [
    path('index/',index_view,name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('events/', views.event_list, name='event_list'),


]



