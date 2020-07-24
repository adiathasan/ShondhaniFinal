from django.urls import path

from .views import *

urlpatterns = [
    path('', homePublic, name='homePublic'),
    path('plasma/form1/', plasmaForm, name='plasmaForm'),
    path('admin_2/', homeAdmin, name='homeAdmin'),
    path('admin_2/donorTable', donorTable, name='donorTable'),
    path('admin_2/login', loginPage, name='login'),
    path('admin_2/register', registerPage, name='register'),
    path('admin_2/logout', logout_user, name='logout'),
    path('admin_2/form1', formAdmin, name='form1'),
    path('admin_2/form2', formAdmin2, name='form2'),
    path('admin_2/calendar', calendar, name='calendar'),
    path('admin_2/donor/<str:pk>', viewDetail, name='donor_detail'),
    path('requisition/volunteer', reqFormVol, name='reqVol'),
]
