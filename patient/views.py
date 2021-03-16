from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.template import loader
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator




from .models import Patient
from .forms import UserRegistration



# Create your views here.
def register_page(request):
    form = UserRegistration

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Patient ' + user + ' registered succesfully!') 
            return redirect('patient:login')

    context = {'form' : form}
    return render(request, 'patient/register.html', context)

def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=uname, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('patient:index')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'patient/login.html')

def logout_user(request):
    logout(request)
    return redirect('patient:login')

@login_required(login_url = 'patient:login')
def index(request):
    return render(request, 'patient/index.html')


@login_required(login_url = 'patient:login')
def patientview(request):
    patients = Patient.objects.all()
    #template = loader.get_template('patient/patient_view.html.html')
    context = {'patients' : patients,}
    #return HttpResponse(template.render(context, request))
    return render(request, 'patient/patient_view.html', context)

@login_required(login_url = 'patient:login')
def parientdetails(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient/patientdetails.html', {'patient' : patient})

@method_decorator(login_required, name='dispatch')
class PatientCreate(CreateView):
    model = Patient
    fields = ['patient_fname' , 'patient_lname' , 'age', 'gender', 'ailment', 'patient_report']    