from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

class User_manager(BaseUserManager):
    def create_user(self, username, email, phone, housenumber, locality, village, mandal, district, pincode, password):
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            phone = phone,
            housenumber = housenumber,
            locality = locality,
            village = village,
            mandal = mandal,
            district = district,
            pincode = pincode
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email = email,
            phone = "Null",
            housenumber = "Null",
            locality = "Null",
            village = "Null",
            mandal = "Null",
            district = "Null",
            pincode = "Null", 
            password = password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=10)
    housenumber = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    mandal = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6)

#    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
#    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
#    nickname = models.CharField(max_length=32, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"
    objects = User_manager()

    def __str__(self):
        return self.username
