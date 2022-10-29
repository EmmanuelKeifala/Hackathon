from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django  import form



class Business(ModelForm):
    number_of_sales = forms.TextInput()
