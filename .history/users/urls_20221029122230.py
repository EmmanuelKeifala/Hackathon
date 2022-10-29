from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dash/', views.Dash, name='dash'),
    path('board/', views.DangerDash, name='board'),
    path('board/', views.DangerDash, name='board'),
    path('trainees/', views.tarinees, name='trainees'),


    path('profile/', views.profile, name='profile'),
    path("upload/", views.upload, name="upload"),
    path('Analyst_home/', views.Analyst_home, name='Analyst_home'),
    path('generalusers_home/', views.generalusers_home, name='generalusers_home'),
    path('Details/', views.details, name='details'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
