from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    sex = models.CharField(max_length=1)
    pic = models.ImageField()
    pwd = models.CharField(max_length=15)
