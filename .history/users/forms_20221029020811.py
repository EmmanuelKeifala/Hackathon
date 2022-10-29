from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Enterpreneur


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BusinessData(ModelForm):
    number_of_sales = forms.TextInput()
    revenue = forms.TextField()
    number_of_customers = forms.TextInput()
    year = forms.IntegerField()
