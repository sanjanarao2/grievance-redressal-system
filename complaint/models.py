from django.db import models
from django.utils import timezone
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