
from django.contrib import admin
from django.urls import path, include
from complaint import views as compviews
from users import views as userviews
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
    path('mycomplaints/', compviews.mycomplaints, name='mycomplaints'),
    path('dashboard/<int:cmp_id>', compviews.redressal, name='complaint-redressal'),
    path('myprofile/', compviews.myprofile, name='myprofile'),
    path('edit/', compviews.edit, name='edit'),
    path('changepassword/', compviews.passwordchange, name='edit-password'),
    path('done/', compviews.done, name='complaint-registered'),
    path('/', include('django.contrib.auth.urls')),


    # path('password_reset/', auth_views.password_reset, name='password_reset'),
    # path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
    path('manager/',compviews.manager,name='manager'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
