from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def faqs(request):
    return render(request, 'faqs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
