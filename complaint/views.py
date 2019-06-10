from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Complaint
from .forms import ComplaintForm
# Create your views here.

def home(request):
    form = ComplaintForm()
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            context = Complaint.objects.create(**form.cleaned_data)
            return render(request, 'complaint-registered.html', {'form':context})

    form = ComplaintForm()
    context = {'form':form}
    return render(request, 'complaint-register.html', context)

def dashboard(request):
    context = {
        'complaints' : Complaint.objects.all()
    }
    return render(request, 'complaint-dashboard.html', context)

def done(request):
    context = 0
    content = {
    "form": context
        }
    return render(request, 'complaint-registered.html', content)
