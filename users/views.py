from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

def faqs(request):
    return render(request, 'faqs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Congratulations on registration {username}! Login to proceed')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {"form" : form })
