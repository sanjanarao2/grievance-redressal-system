from django.db import models
from django.utils import timezone
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
