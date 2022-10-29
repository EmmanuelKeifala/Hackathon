import email
from enum import auto
from pickle import FALSE
from unicodedata import name
from django.db import models


# Create your models here.

# this is for the admin


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

# Analysts Table


class Analysts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

# this is for the Enterpreneurs table


class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE, null=True, blank=True)
    analyst = models.ForeignKey(
        Analysts, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    date_of_training = models.DateTimeField(auto_now=False)
    idea = models.TextField()
    institution = models.TextField()
    qualification = models.TextField()
    location = models.TextField()
    objects = models.Manager()

    # this is for the entrepenuer


class Enterpreneur(models.Model):
    id = models.AutoField(primary_key=True)
    userEmail = models.EmailField()
    number_of_sales = models.TextField()
    revenue = models.TextField()
    number_of_customers = models.TextField()
    year = models.IntegerField()
