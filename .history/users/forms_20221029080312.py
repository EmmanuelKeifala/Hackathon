from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Enterpreneur
from .models import Trainee


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
        "type": "number",
        "placeholder": "Number of customers"}))
    year = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "number",
        "min": "1900", "max": "2099",
        "step": "1", "value": "2022",
        "placeholder": "Year"}))
    userEmail = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Number of customers"}))

    class Meta:
        model = Enterpreneur
        fields = ['number_of_sales', 'revenue', 'number_of_customers', "year"]


class userProfile(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "UserName"}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Email"}))
    age = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "number",
        "placeholder": "Age"}))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "gender"}))
    idea = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Your Vision"}))
    date_of_training = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "date",
        "placeholder": "Date of Training"}))
    institution = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Institution"}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Qualification"}))

    class Meta:
        model = Trainee
        fields = ['name', 'email', 'age', "gender",
                  "idea", "institution", "qualification", "date_of_training"]


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
