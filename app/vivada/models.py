from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, verbose_name="email")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)


class Books(models.Model):
    bookName = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=500)


class Questions(models.Model):
    question = models.CharField(max_length=100)
    questionCategory = models.CharField(max_length=100)


class Answers(models.Model):
    answer = models.CharField(max_length=100)


class Groceries(models.Model):
    groceryName = models.CharField(max_length=40)
    groceryType = models.CharField(max_length=40)
    groceryPrice = models.IntegerField()
