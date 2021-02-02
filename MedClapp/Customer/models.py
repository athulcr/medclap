from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


    
class Customerprofile(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=4)
    choice = (
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
    )
    bloodgroup = models.CharField(max_length=100,choices=choice)
    choicea = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    gender = models.CharField(max_length=100,choices=choicea)
    height = models.CharField(max_length=10,default=None)
    weight = models.CharField(max_length=10,default=None)
    address = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images',default=None) 
  

    def __str__(self):
        return self.name

class Request(models.Model):
    choicea = (
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
    )
    bloodgrouprequest = models.CharField(max_length=100,choices=choicea)
    location = models.TextField(max_length=250)
    choiceb = (
        ('Emergency','Emergency'),
        ('Moderate','Moderate'),
        ('Normal','Normal'),
    )
    priority = models.CharField(max_length=100,choices=choiceb,default='None')


def __str__(self):
    return self.priority
