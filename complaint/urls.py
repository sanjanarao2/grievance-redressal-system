from django.urls import path

<<<<<<< HEAD

urlpatterns = [

]
=======
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
>>>>>>> 642a1e5a6f1e442b0b6b91cdbd0bcfaa6b902910
