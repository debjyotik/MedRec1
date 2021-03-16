from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Patient(models.Model):
    patient_fname = models.CharField(max_length=255, verbose_name="First Name")
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