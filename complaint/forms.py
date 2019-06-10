from django import forms
from .models import Complaint

class ComplaintForm(forms.Form):
    contact = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=True)
    complaint = forms.CharField(max_length=1000, required=True)
#   photo = forms.ImageField(required=False)
