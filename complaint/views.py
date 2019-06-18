from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Complaint
from .forms import ComplaintForm,editprofileform,complaintredressal
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm



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
def edit(request):
    
    #person = get_user_model()
    if request.method == "POST":
        form = editprofileform(request.POST,instance = request.user,initial={'email':request.user.email,'phone':request.user.phone})     
        form.actual_user = request.user
        #if form.is_valid():
        form.save()
        return redirect('/mycomplaints')
    else:
        form = editprofileform(initial={'email':request.user.email,
            'phone':request.user.phone,
            'housenumber':request.user.housenumber,
            'locality':request.user.locality,
            'village':request.user.village,
            'mandal':request.user.mandal,
            'district':request.user.district,
            'pincode':request.user.pincode})     
        args = {'form':form}
        return render(request, 'edit.html', args)


@login_required
def passwordchange(request):
    
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)     
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/mycomplaints')
    else:
        form = PasswordChangeForm(user=request.user)     
        args = {'form':form}
        return render(request, 'edit-password.html', args)


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


@login_required
def redressal(request, cmp_id):
    comp = get_object_or_404(Complaint,pk=cmp_id)
    if request.method == "POST":
        form =complaintredressal(request.POST)
        if form.is_valid():  
            comp.status = form.cleaned_data['status']
            comp.resolution = form.cleaned_data['resolution'] 
            comp.resolved_by = request.user.username
            comp.save()
            return redirect('/dashboard') 
    
    form = complaintredressal()

    return render(request, 'complaint-redressal.html',{'comp':comp,'form':form})