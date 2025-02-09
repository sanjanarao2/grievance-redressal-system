from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone, six
from django.http import HttpResponse
from .models import Complaint
from .forms import ComplaintForm,editprofileform, complaintredressal, dashboardform
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups =(group, )
        else:
            groups = group
        if user.groups.filter(name__in=groups).exists():
            return True
        if raise_exception:
            raise PermissionDenied
        #if group == 'staff':
        #    user.is_staff=True
        #elif group == 'manager':
        #    user.is_manager=True
        return False
    return user_passes_test(check_perms, login_url=login_url)

@login_required
def home(request):

    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():

            context = Complaint()
            context.author = request.user
            context.complaint = form.cleaned_data['complaint']
            context.channel = form.cleaned_data['channel']
            context.stream = form.cleaned_data['stream']
            context.dept = form.cleaned_data['dept']
            context.image = form.cleaned_data['image']
            context.file = form.cleaned_data['file']
            #context.file = request.FILES['file']
            context.save()
            return render(request, 'complaint-registered.html', {'form':context})

    form = ComplaintForm()
    context = {'form':form}
    return render(request, 'complaint-register.html', context)

@login_required
@group_required('staff', 'manager')
def dashboard(request):
    form = dashboardform()
    dat = timezone.now()
    dep=request.GET.get("d")
    cha=request.GET.get("c")
    complaints_unre = Complaint.objects.filter(dept="department0",status = "unresolved")
    complaints_re = Complaint.objects.filter(dept="department0",status ="resolved")
    if dep and cha:

        complaints_unre = Complaint.objects.filter(dept=dep,channel=cha,status = "unresolved")
        complaints_re = Complaint.objects.filter(dept=dep,channel=cha,status ="resolved")
    if dep == "All" and cha !="All":
        complaints_unre = Complaint.objects.filter(channel=cha,status = "unresolved")
        complaints_re = Complaint.objects.filter(channel=cha,status ="resolved")
    if cha == "All"and dep != "All":
        complaints_unre = Complaint.objects.filter(dept=dep,status = "unresolved")
        complaints_re = Complaint.objects.filter(dept=dep,status ="resolved")
    if dep == "All" and cha =="All":
        complaints_unre = Complaint.objects.filter(status = "unresolved")
        complaints_re = Complaint.objects.filter(status ="resolved")

    context = {'form':form,'complaints_unre' : complaints_unre,'complaints_re':complaints_re,'dat':dat}
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
        'complaints' : Complaint.objects.filter(author= request.user)
    }
    return render(request, 'complaint-view.html', context)

@login_required
def myprofile(request):
    context = {
        'details': request.user
    }
    return render(request, 'profile.html', context)

@login_required
def done(request):
    context = 0
    content = {
    "form": context
        }
    return render(request, 'complaint-registered.html', content)

@group_required('manager')
def manager(request):
    return render(request, 'manager.html')



@login_required
@group_required('staff')
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
