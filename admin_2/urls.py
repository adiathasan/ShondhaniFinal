from django.urls import path

from .views import *

urlpatterns = [
    path('', homePublic, name='homePublic'),
    path('plasmaDonor/form/', plasmaForm, name='donPub'),
    path('admin_2/', homeAdmin, name='homeAdmin'),
    path('donor/table', donorTable, name='donorTable'),
    path('admin_2/login', loginPage, name='login'),
    path('admin_2/register', registerPage, name='register'),
    path('admin_2/logout', logout_user, name='logout'),
    path('admin_2/form1', formAdmin, name='form1'),
    path('admin_2/form2', TriageVol, name='triVol'),
    path('admin_2/calendar', calendar, name='calendar'),
    path('admin_2/donor/<str:pk>', viewDetail, name='donor_detail'),
    path('triage/detail/<str:pk>', triageView, name='triageDetail'),
    path('requester/detail/<str:pk>', reqView, name='reqDetail'),
    path('requisition/volunteer', reqFormVol, name='reqVol'),
    path('requisition/public', reqFormPub, name='reqPub'),
    path('donor/volunteer', donorVol, name='donVol'),
    path('donor/motivated/volunteer', motDonForm, name='motDonForm'),
    path('triage/table', triageTable, name='triageTable'),
    path('requester/table', reqTable, name='reqTable'),
    path('donorRequester/table', donReqTable, name='donReqTable'),
    path('donorRequester/form', donReqFormView.as_view(), name='donReqForm'),
]

