from django.urls import path
from apijwt.views import RegisterView,ProtectedView,LogoutView,custom_login

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', custom_login, name='custom_login'),

]


