from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from users.models import Analysts, Trainee
from .forms import UserRegisterForm, userProfile
from .forms import BusinessData
from .forms import userProfile
from .forms import Analyst_Form


from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def generalusers_home(request):
    return render(request, "users/home.html")


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


def studentsView(request):
    cs_no = Students.objects.filter(course='Computer Science').count()
    cs_no = int(cs_no)
    print('Number of Computer Science Students Are', cs_no)

    ce_no = Students.objects.filter(course='Computer Engineering').count()
    ce_no = int(ce_no)
    print('Number of Computer Engineering Students Are', ce_no)

    se_no = Students.objects.filter(course='Software Engineering').count()
    se_no = int(se_no)
    print('Number of Software Engineering Students Are', se_no)

    sec_no = Students.objects.filter(course='Computer Security').count()
    sec_no = int(sec_no)
    print('Number of Computer Security Students Are', sec_no)

    male_no = Students.objects.filter(gender='Male').count()
    male_no = int(male_no)
    print('Number of Male Are', male_no)

    female_no = Students.objects.filter(gender='Female').count()
    female_no = int(female_no)
    print('Number of Female Are', female_no)

    gender_list = ['Male', 'Female']
    gender_number = [male_no, female_no]

    course_list = ['Computer Science', 'Computer Engineering',
                   'Software Engineering', 'Computer Security']
    number_list = [cs_no, ce_no, se_no, sec_no]
    context = {'course_list': course_list, 'number_list': number_list,
               'gender_list': gender_list, 'gender_number': gender_number}
    return render(request, 'comment/officer_home.html', context)
