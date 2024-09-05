from django.urls import path
# from events import views
# from accounts.views import index_view,register_view,login_view,logout_view
from .views import approve_ticket,book_ticket
urlpatterns = [
    path('book-ticket/<int:event_id>/', book_ticket, name='book_ticket'),
    path('approve-tickets/', approve_ticket, name='approve_ticket')
]