from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from Customer.models import Customerprofile,Request
from Customer.forms import Customerform,Requestform,LoginForm,CustomUserCreationForm
from django.views.generic import TemplateView, CreateView ,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from Customer.backends import CustomerBackend

# from django.contrib.auth.forms import AuthenticationForm

# def register(request):
#     return render(request, '../templates/index.html')

class Customerlist(TemplateView):
    template_name = "Customer/customerlist.html"
    model = Customerprofile
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)


class Customercreate(CreateView):
    model = Customerprofile
    form_class = Customerform()
    template_name = "Customer/customercreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Customerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customerlist')
        else:
            return redirect('customercreate')

class Customerdetails(TemplateView):
    model = Customerprofile
    template_name = "Customer/customerdetails.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)


class index(TemplateView):
    template_name = "Customer/index.html"
    model = Customerprofile
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)

class Customeredit(TemplateView):
    model = Customerprofile
    form_class = Customerform()
    template_name = "Customer/customeredit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = Customerform(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = Customerform(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customerlist')
        else:
            return render(request, self.template_name, self.context)


class Customerdelete(DeleteView):
    model = Customerprofile
    template_name = "Customer/customerdelete.html"
    form_class = Customerform()
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = Customerform(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('customerlist')      


        
       
class registerationn(TemplateView):
    form_class = CustomUserCreationForm
    template_name = "Customer/UserRegister.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpagee")
        else:
            self.context['form'] = self.form_class
            return render(request, self.template_name, self.context)


class loginpagee(TemplateView):
    form_class = LoginForm
    template_name = "Customer/UserLogin.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone'] # take email in form for username
            password = form.cleaned_data['password']
            print(phone,",",password)
            user = CustomerBackend(phone=phone, password=password,backend='ServiceProvider.backends.CustomerBackend')
            # print(user)
            login(request, user)
            print("success")
        return redirect('Dashboardd')
        # return render(request, self.template_name)

class logoutt(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('loginpagee')


def Userhome(request,pk):
    form = Requestform()
    context = {'form': form}
    if request.method == 'POST':
        # leave_Status=request.POST('leave_status')
        obj = Request.objects.all()
        obj.priority = 'pending'
        context['status'] = obj.priority
        print(obj.priority)
        form = Requestform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Customer/check.html", context)
    return render(request, "Customer/userhome.html", context)

def Viewstatus(request, pk):
    obj = Request.objects.get(id=pk)
    status = obj.priority
    context = {}
    context['status'] = status
    return render(request, "Customer/Viewstatus.html", context)

def IndexUser(request):
    return render(request, "Customer/indexx.html")

def Dashboardd(request):
    return render(request,"Customer/basee.html")


