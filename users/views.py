from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def faqs(request):
    return render(request, 'faqs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method== "POST":
        form = UserCreationForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for { username }')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form" : form })
