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
    number_of_sales = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Number of sales"}))
    revenue = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "number",
        "placeholder": "Total Income"}))
    number_of_customers = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Number of sales"}))
    year = forms.DateField()

    class Meta:
        model = Enterpreneur
        fields = ['number_of_sales', 'revenue', 'number_of_customers', "year"]
