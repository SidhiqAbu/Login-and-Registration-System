from django.db import models

# Create your models here.

class myApp(models.Model):
    userName = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
