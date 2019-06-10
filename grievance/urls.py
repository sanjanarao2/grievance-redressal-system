"""grievance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from complaint import views as compviews
from users import views as userviews


urlpatterns = [
    path('complaint/', include('complaint.urls')),
    path('admin/', admin.site.urls),
    path('', userviews.index, name='index'),
    path('faqs', userviews.faqs, name='faqs'),
    path('login', userviews.login, name='login'),
    path('registration', userviews.register, name='register'),
    path('register', compviews.home, name='complaint-registration'),
    path('dashboard/', compviews.dashboard, name='complaint-dashboard'),
    path('done/', compviews.done, name='complaint-registered'),

]
