# Generated by Django 4.1.2 on 2022-10-29 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("email", models.TextField()),
                ("password", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Analysts",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("email", models.TextField()),
                ("password", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Enterpreneur",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("userEmail", models.EmailField(max_length=254)),
                ("number_of_sales", models.TextField()),
                ("revenue", models.TextField()),
                ("number_of_customers", models.TextField()),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Trainee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("email", models.TextField()),
                ("age", models.IntegerField()),
                ("gender", models.TextField()),
                ("date_of_training", models.DateTimeField()),
                ("idea", models.TextField()),
                ("institution", models.TextField()),
                ("qualification", models.TextField()),
                ("location", models.TextField()),
                (
                    "admin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.admin",
                    ),
                ),
                (
                    "analyst",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.analysts",
                    ),
                ),
            ],
        ),
    ]