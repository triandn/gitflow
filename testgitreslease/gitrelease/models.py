from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256 , default = '', blank = True)
    password = models.CharField(max_length=256 , default = '', blank = True)

class Company(models.Model):
    company_name = models.CharField(max_length=256 , default = '', blank = True)
    