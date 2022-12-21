from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def crate_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Para ser super usuario necesitas que is_staff sea verdadero')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Para ser super usuario necesitas que is_superuser sea verdadero')
        
        return self.crate_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80, unique=True, default="bill@user.com")
    username = models.CharField(max_length=45)
    date_of_birt = models.DateField(null=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self) -> str:
        return self.username