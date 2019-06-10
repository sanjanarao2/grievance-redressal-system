from django.db import models
from django.utils import timezone
<<<<<<< HEAD
from django.contrib.auth.models import User


class Complaint(models.Model):
    date = models.DateTimeField(default=timezone.now)
#   author = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10,blank=True, null=True)
    email = models.EmailField(default='123@xyz.org')
    complaint = models.CharField(max_length=1000)
#   photo = models.ImageField(blank=True,null=True)

    def token(self):
        self.token = 'CMPLNOO'+str(self.id)
        return self.token
=======
# Create your models here.

class department(models.Model):
    
    dept_name = models.CharField(max_length=10,default='Other')

    def __str__(self):
        return self.dept_name

class complaint(models.Model):
    dept_id = models.ForeignKey('department',on_delete = models.CASCADE)
    token_no = models.CharField(max_length=8)
    grevience = models.CharField(max_length=500)
    #created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   # have to check if this is working
    
    public_notes = models.CharField(max_length=250,default=' ')
    private_notes = models.CharField(max_length=250,default=' ')

    def __str__(self):
        return self.grevience
>>>>>>> 642a1e5a6f1e442b0b6b91cdbd0bcfaa6b902910
