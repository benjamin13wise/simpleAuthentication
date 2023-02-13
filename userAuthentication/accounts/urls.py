from django.urls import path 
from django.contrib.auth.views import LoginView,LogoutView
from .views import home , register

urlpatterns = [
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('home',home,name='home'),
    path('register',register,name='register'),
]
