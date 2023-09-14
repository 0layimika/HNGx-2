from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=45)
    dob=models.CharField(max_length=10)
    telephone=models.CharField(max_length=11)
    address=models.CharField(max_length=50)