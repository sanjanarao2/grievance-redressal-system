from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class Complaint(models.Model):
    
    d1="department1"
    d2="department2"
    d3="department3"
    d4="Other"
    dept_choice = ((d1,"department1"),(d2,"department2"),(d3,"department3"),(d4,"Other"))
    
    s1="unresolved"
    s2="resolved"
    s3="spam"
    status_choice = ((s1,"unresolved"),(s2,"resolved"),(s3,"spam"))

    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    dept = models.CharField(max_length = 15, choices = dept_choice, default = d4)
    status = models.CharField(max_length = 15, choices = status_choice, default = s1)
    complaint = models.CharField(max_length=1000)
    resolution = models.CharField(max_length=1000)
    resolved_by = models.CharField(max_length = 32, default=None, blank=True, null=True)
#   photo = models.ImageField(blank=True,null=True)

    def token(self):
        self.token = 'CMPLNOO'+str(self.id)
        return self.token
