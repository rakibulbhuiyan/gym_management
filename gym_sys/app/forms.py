from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Enquiry
from django.contrib.auth.models import User

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields=['full_name','email','detail']

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
