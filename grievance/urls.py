
from django.contrib import admin
from django.urls import path, include
from complaint import views as compviews
from users import views as userviews
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('complaint/', include('complaint.urls')),
    path('admin/', admin.site.urls),
    path('', userviews.index, name='index'),
    path('faqs/', userviews.faqs, name='faqs'),
    path('registration/', userviews.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', compviews.home, name='complaint-registration'),
    path('dashboard/', compviews.dashboard, name='complaint-dashboard'),
    path('dashboard/<int:cmp_id>', compviews.redressal, name='complaint-redressal'),
    path('mycomplaints/', compviews.mycomplaints, name='complaint-view'),
    path('edit/', compviews.edit, name='edit'),
    path('changepassword/', compviews.passwordchange, name='edit-password'),
    path('done/', compviews.done, name='complaint-registered'),

]
