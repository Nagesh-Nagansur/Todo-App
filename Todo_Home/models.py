from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    discrption=models.TextField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
