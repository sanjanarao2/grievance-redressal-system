from django import forms
from .models import Complaint

d1="department1"
d2="department2"
d3="department3"
d4="Other"
dept_choice = ((d1,"department1"),(d2,"department2"),(d3,"department3"),(d4,"Other"))

class ComplaintForm(forms.Form):
    contact = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=True)
    complaint = forms.CharField(max_length=1000, required=True)
    dept = forms.CharField(label='department?', widget=forms.Select(choices=dept_choice))

#   photo = forms.ImageField(required=False)
