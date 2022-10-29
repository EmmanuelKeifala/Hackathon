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
    number_of_sales = forms.SlugField()
    revenue = forms.SlugField()
    number_of_customers = forms.SlugField()
    year = forms.IntegerField()

    class Meta:
        model = Enterpreneur
        fields = ['number_of_sales', 'revenue', 'number_of_customers', "year"]
        widgets = {
            'number_of_sales': forms.SlugField(attrs={'class': 'form-control'}),
            'revenue': forms.SlugField(attrs={'class': 'form-control'}),
            'number_of_customers': forms.SlugField(attrs={'class': 'form-control'}),
            'year': forms.DateField(attrs={'class': 'form-control'})

        }
