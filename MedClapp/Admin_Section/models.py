from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# from ServiceProvider.managers import CustomUser
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class department(models.Model):
    dept_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dept_name
