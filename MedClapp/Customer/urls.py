
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from Customer.views import Customerlist,Customercreate,Customerdetails,index,Customeredit,Customerdelete,loginpagee,logoutt,registerationn,Userhome,Viewstatus,IndexUser,Dashboardd

urlpatterns = [
    
    path('list/', Customerlist.as_view(), name="customerlist"),
    path('create/',Customercreate.as_view(), name="customercreate"),
    path('details<int:pk>/', Customerdetails.as_view(), name='customerdetails'),
    path('index/', index.as_view(), name="index"),
    path('edit<int:pk>/', Customeredit.as_view(), name="customeredit"),
    path('delete<int:pk>/', Customerdelete.as_view(), name="customerdelete"),
    # path('employee_register/',employee_register.as_view(), name='employee_register'),
    # path('login/',login_request, name='login'),
    path('Customer_register/', registerationn.as_view(), name="registerationn"),
    path('Customer_log', loginpagee.as_view(), name="loginpagee"),
    path('logout', logoutt.as_view(), name='logout'),
    path("User<int:pk>",Userhome,name="Userhome"),
    path("view<int:pk>",Viewstatus,name="Viewstatus"),
    path("indexx/",IndexUser,name="IndexUser"),
    path('main/',Dashboardd,name="Dashboardd"),

]