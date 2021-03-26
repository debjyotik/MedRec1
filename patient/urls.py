from django.conf.urls import url
from django.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'patient'

urlpatterns = [
    
    url(r'^accounts/', include('allauth.urls')),
    #/
    url(r'^$', views.index, name='index'),

    #/register/
    url(r'^register/$', views.register_page, name='register'),

    #/login/
    url(r'^login/$', views.login_page, name='login'),

    #/logout/
    url(r'^logout/$', views.logout_user, name='logout'),

    #/patient/
    url(r'^patient/$', views.patientview, name='patientview'),

    #/patient/listjsn
    #url(r'^patient/listjsn/$', views.PatientList.as_view(), name='patientlistjason'),

    #/patient/1/
    url(r'^patient/(?P<patient_id>[0-9]+)/$', views.parientdetails, name='parientdetails'),

    #patient/add/
    url(r'patient/add/$', views.PatientCreate.as_view(), name='patient-add'),
]