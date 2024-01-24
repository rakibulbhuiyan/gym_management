from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Enquiry,Trainer
from django.contrib.auth.models import User

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields=['full_name','email','detail']

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
class ProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields=['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        