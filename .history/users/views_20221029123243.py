import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from users.models import Analysts, Trainee
from .forms import UserRegisterForm, userProfile
from .forms import BusinessData
from .forms import userProfile
from .forms import Analyst_Form
from .forms import *
import pandas as pd

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def Dash(request):
    item = Enterpreneur.objects.all().values()
    df = pd.DataFrame(item)
    num_cos = df.number_of_customers.tolist()

    df1 = df.number_of_sales.tolist()
    df = df["year"].tolist()

    mydict = {
        'df': df,
        'df1': df1,
        'num_cos': num_cos,
    }
    return render(request, "users/Analysis.html", context=mydict)


def generalusers_home(request):

    return render(request, "users/home.html")


def DangerDash(request):
    item = Enterpreneur.objects.all().values()
    df = pd.DataFrame(item)
    num_cos = df.number_of_customers.tolist()

    df1 = df.number_of_sales.tolist()
    df = df["year"].tolist()

    mydict = {
        'df': df,
        'df1': df1,
        'num_cos': num_cos,
    }
    return render(request, "comment/officer_home.html", context=mydict)


def trainees(request):
    data = Trainee.objects.all()
    if request.method == "POST":
        nm = request.POST["name"]
        em = request.POST["email"]
        ag = request.POST["age"]
        ge = request.POST["gender"]
        dag = request.POST["date_of_training"]
        ida = request.POST["idea"]
        ins = request.POST["institution"]
        qua = request.POST["qualification"]

        data = Trainee(nm=name, em=email, ag=age, ge=gender, dag=date_of_training,
                       ida=idea, ins=institution, qua=qualification)
        data.save();
        res = "Thanks for the data"
        return render(request, "user/Trainees.html", {"status": res})
    return render(request, "user/Trainees.html", {"info": da ta})
    


def Analyst_home(request):
    if request.method == "POST":
        form = Analyst_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully as an Analyst')
            return redirect('home')
    else:
        form = Analyst_Form()

    return render(request, 'users/loginAnalyst.html', {'form': form})


def upload(request):
    if request.POST:
        form = BusinessData(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, "users/upload.html", {'form': BusinessData})


# @login_required
def details(request):
    if request.POST:
        formVal = userProfile(request.POST)
        print(request.POST)
        if formVal.is_valid():
            formVal.save()
        return redirect("/")
    return render(request, "users/details.html", {'form': userProfile})


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
