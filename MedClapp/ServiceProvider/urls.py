from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Doctorcreate,Doctoredit,password_success,Usercreate,PasswordsChangeView,UserProfilelist,ActivateAccountView,SetNewPasswordView,RequestResetEmailView,Servicecreatee,DeleteDoctor,Doctorlist,servicelisting,Deletservice,servicingedit,categorydelete,Createservice,Categoryedit,Categorylist,Categorycreate,DeleteStatus,Hrhome,Leaveconfirm,loginpage,registeration,logoutt,base

urlpatterns = [
    path('password/',PasswordsChangeView.as_view(template_name='ServiceProvider/change-password.html')),
    path('password_success',password_success,name="password_success"),
    path('profilesection',Usercreate.as_view(),name="Usercreate"),
    path('userprofilelisting',UserProfilelist.as_view(),name="UserProfilelist"),
    path('serviceProviderlisting',Servicecreatee.as_view(),name="Servicecreatee"),
    path('doctorcreate',Doctorcreate.as_view(),name="Doctorcreate"),
    path('doctorlist',Doctorlist.as_view(),name="Doctorlist"),
    path('doctoredit<int:pk>',Doctoredit.as_view(),name="Doctoredit"),
    path('deletdoctor<int:pk>',DeleteDoctor.as_view(),name="DeleteDoctor"),
    path('servicecreate',Createservice.as_view(),name="Createservice"),
    path('servicelisting',servicelisting.as_view(),name="servicelisting"),
    path('serviceedit<int:pk>',servicingedit.as_view(),name="servicingedit"),
    path('deleteservice<int:pk>',Deletservice.as_view(),name="Deletservice"),
    path('categoryadd',Categorycreate.as_view(),name="Categorycreate"),
    path('categorylist',Categorylist.as_view(),name="Categorylist"),
    path('Categoedit<int:pk>',Categoryedit.as_view(),name="Categoryedit"),
    path('categorydelete<int:pk>',categorydelete.as_view(),name="categorydelete"),
    path('status<int:pk>', Hrhome, name="Hrhome"),
    path('leave<int:pk>', Leaveconfirm, name="Leaveconfirm"),
    # path('',Landing,name="Landing"), 
    path('register/', registeration.as_view(), name="register"),
    path('login', loginpage.as_view(), name="loginpage"),
    path('logout', logoutt.as_view(), name='logout'),
    path('base/', base.as_view(), name="base"),
    path('delete<int:pk>',DeleteStatus,name="DeleteStatus"),
    path('activate/<uidb64>/<token>',ActivateAccountView.as_view(),name="activate"),
    path('set-new-password/<uidb64>/<token>',SetNewPasswordView.as_view(),name="set-new-password"),
    path('request-reset-email',RequestResetEmailView.as_view(),name="request-reset-email"),
]