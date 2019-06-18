from django import forms
from .models import Complaint
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserChangeForm
from users.forms import RegistrationForm,changedetails
from django.contrib.auth import get_user_model



d1="department1"
d2="department2"
d3="department3"
d4="Other"
dept_choice = ((d1,"department1"),(d2,"department2"),(d3,"department3"),(d4,"Other"))

class ComplaintForm(forms.Form):
    complaint = forms.CharField(max_length=1000, required=True)
    dept = forms.CharField(label='Department', widget=forms.Select(choices=dept_choice))

#   photo = forms.ImageField(required=False)

class editprofileform(changedetails):
    """phone = forms.CharField(max_length=10)
    housenumber = forms.CharField(max_length=255)
    locality = forms.CharField(max_length=255)
    village = forms.CharField(max_length=255)
    mandal = forms.CharField(max_length=255)
    district = forms.CharField(max_length=255)
    pincode = forms.CharField(max_length=6)"""
    
        
    
    