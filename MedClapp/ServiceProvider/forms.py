from django import forms
from django.forms import ModelForm
from ServiceProvider.models import Userprofile,CustomUser,Doctor
from Customer.models import Request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Customer.forms import Requestform
from Admin_Section.models import department,Category
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ServiceProvider.models import CustomUser


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields='__all__'

class UserprofileForm(ModelForm):
    class Meta:
        model = Userprofile
        fields='__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = department
        fields='__all__'

class DoctorForm(forms.ModelForm):
    class Meta(UserCreationForm):
        model = Doctor
        fields='__all__'



class CustomUserCreationForm(ModelForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','fullname','phone','address','category','zip_code','location')
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control"}),
        }      



#end

class RequestConfirmfm(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
        widgets = {
            "bloodgrouprequest": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
        }           


class LoginForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','password')
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }  

