from django.db import models
from django.urls import reverse
from django import forms

from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import mysql.connector

# Create your models here.
class Patient(models.Model):

    mysql_connection = mysql.connector.connect(host="localhost", user="root", passwd="Kolkata@1", database="patient_record_rest")

    if mysql_connection.is_connected():
        transaction = mysql_connection.cursor()
        transaction.execute(" select Transaction_display_name from Transaction where Transaction_name ='{}' and Lang_code = {} ".format('patient_fname', 1, ))
        patient_fname_verbose = str(transaction.fetchone()[0])

    patient_fname = models.CharField(max_length=255, verbose_name=patient_fname_verbose)
    patient_lname = models.CharField(max_length=255, verbose_name="Last Name")
    age = models.FloatField(verbose_name="Age of Patient")
    #gender = models.CharField(max_length=1, verbose_name="Gender")
    TYPE_SELECT = (('F', 'Female'),('M', 'Male'),)
    gender = models.CharField(max_length=11,choices=TYPE_SELECT)
    #gender = forms.ChoiceField(widget=forms.RadioSelect)
    ailment = models.CharField(max_length=1000, verbose_name="Ailment")
    patient_report = models.FileField(blank=True)

    def get_absolute_url(self):
        return reverse('patient:patientview')  #, kwargs={'pk': self.pk})

    def __str__(self):
        return self.patient_fname + " : " + self.ailment

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token_authorization(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)