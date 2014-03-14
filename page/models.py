from django.db import models
from django.forms import ModelForm

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("User")

class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    dateJoined = models.DateTimeField('date joined')

class Instruction(models.Model):
    instructions = models.TextField(blank=True)
    author = models.ForeignKey(User)
    date = models.DateTimeField('date authored')
    title = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField()
  
