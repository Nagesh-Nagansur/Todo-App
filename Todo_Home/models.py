from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    discrption=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title

class Todos(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField(max_length=1000)
    datecreated=models.DateTimeField(auto_now_add=True)
    important=models.BooleanField(null=True)
