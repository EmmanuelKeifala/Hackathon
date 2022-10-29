from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .forms import BusinessData
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def generalusers_home(request):
    return render(request, "users/home.html")


def Analyst_home(request):
    return render(request, "users/home.html")


def upload(request):
    if request.POST:
        form = BusinessData(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save
        return redirect("/")
    return render(request, "users/upload.html", {'form': BusinessData})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
