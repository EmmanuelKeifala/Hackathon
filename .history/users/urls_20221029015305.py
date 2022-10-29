from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("upload/", views.upload, name="upload business data")
    path('Analyst_home/', views.Analyst_home, name='Analyst_home'),
    path('generalusers_home/', views.generalusers_home, name='generalusers_home'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
