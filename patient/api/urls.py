from django.urls import path, re_path

from . import views

app_name = 'patient'

urlpatterns = [
    re_path(r'^patient/listjsn/$', views.api_patient_list, name = 'patientlistjason'),
    re_path(r'^patient/updatejsn/(?P<patient_id>[0-9]+)$', views.api_patient_update, name = 'patientupdatejason'),
    re_path(r'^patient/deletejsn/(?P<patient_id>[0-9]+)$', views.api_patient_delete, name = 'patientdeletejason'),
    re_path(r'^patient/addjsn$', views.api_patient_create, name = 'patientcreatejason'),
    re_path(r'^patient/register$', views.api_register_user, name = 'patientregisterjason'),
    
]