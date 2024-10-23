from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomManager
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    Fist=models.CharField(max_length=100)
    last=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    profile_img=models.ImageField(upload_to="profile")
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=CustomManager()
    def __str__(self):
        return self.Fist