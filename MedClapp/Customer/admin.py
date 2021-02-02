from django.contrib import admin
from .models import Request,Customerprofile

# Register your models here.

admin.site.register(Customerprofile),
admin.site.register(Request),
# admin.site.register(Customersignup)
# admin.site.register(User)