from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        #field_classes = {'username': UsernameField}
        widgets = {
            'first_name': forms.fields.TextInput(attrs={'placeholder': 'First name...'}),
            'last_name': forms.fields.TextInput(attrs={'placeholder': 'Last name...'}),
            'username': forms.fields.TextInput(attrs={'placeholder': 'Username...'}),
            'email': forms.fields.TextInput(attrs={'placeholder': 'Email...'}),
            #'password1': forms.fields.TextInput(attrs={'placeholder': 'Enter password...'}),
            #'password2': forms.fields.TextInput(attrs={'placeholder': 'Confirm password...'}),
        }

        def __init__(self, *args, **kwargs):
            super(UserRegistration, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': _("Password...")})
            self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': _("Password...")})
