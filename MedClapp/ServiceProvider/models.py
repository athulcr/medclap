from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from Admin_Section.models import department,Category
import requests
# class Category(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(max_length=120)
    location=models.CharField(max_length=120,default='aluva')
    phone = models.CharField(max_length=120)
    zip_code = models.IntegerField(default=683102)
    latitude = models.DecimalField(blank=True,max_digits=9,decimal_places=6)
    longitude = models.DecimalField(blank=True, max_digits=9, decimal_places=6)
    fullname = models.CharField(max_length=120,unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return '%s %s %s %s %s' %(self.email,self.address,self.fullname,self.phone,self.zip_code)
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        r = requests.get(f'https://public.opendatasoft.com/api/records/1.0/search/?dataset=geonames-postal-code&q={self.zip_code}&facet=country_code&facet=admin_name1&facet=admin_code1&facet=admin_name2')
        self.latitude = r.json()['records'][0]['fields']['latitude']
        self.longitude = r.json()['records'][0]['fields']['longitude']
        super().save(*args, **kwargs)
    

    



# class Service(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

class Doctor(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    specialisation = models.ForeignKey(department, on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ImageField(upload_to='images',default=None)
    phone=models.CharField(max_length=120,default=None)
    organisation = models.CharField(max_length=120,default=None)

    def __str__(self):
        return self.fullname

class Userprofile(models.Model):
    coverpicture = models.ImageField(upload_to='images',default=None)
    photo = models.ImageField(upload_to='images',default=None)
    photo = models.ImageField(upload_to='images',default=None)
    photo = models.ImageField(upload_to='images',default=None)
    service = models.ForeignKey(department, on_delete=models.SET_NULL, blank=True, null=True)
    bed_numbers = models.CharField(max_length=120,default=20)

def __str__(self):
    return self.service

