from django.db import models

# Create your models here.
class data(models.Model):

    path=models.CharField(max_length=100)
    indexx=models.CharField(max_length=30)
    