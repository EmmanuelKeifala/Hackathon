
from django.forms import ModelForm
from django import forms


class Business(ModelForm):
    number_of_sales = forms.TextInput()
