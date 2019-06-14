from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Complaint
from .forms import ComplaintForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):

    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():

            context = Complaint()
            context.author = request.user
            context.complaint = form.cleaned_data['complaint']
            context.dept = form.cleaned_data['dept']
            context.save()
            return render(request, 'complaint-registered.html', {'form':context})

    form = ComplaintForm()
    context = {'form':form}
    return render(request, 'complaint-register.html', context)


@login_required
def dashboard(request):
    context = {
        'complaints' : Complaint.objects.all()
    }
    return render(request, 'complaint-dashboard.html', context)

@login_required
def mycomplaints(request):
    context = {
        'details' : request.user,
        'complaints' : Complaint.objects.filter(author= request.user)
    }
    return render(request, 'complaint-view.html', context)

@login_required
def done(request):
    context = 0
    content = {
    "form": context
        }
    return render(request, 'complaint-registered.html', content)
