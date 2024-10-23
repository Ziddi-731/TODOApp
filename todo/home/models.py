from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver  
User = get_user_model()

# Create your models here.
class Timetable(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=120)
    def __str__(self):
        return self.title
    

class sig(models.Model):
    n=models.CharField(max_length=120)
def save_pre(sender,instance,**kwrags):
    print("Pre save working..........")
def save_post(sender,instance,**kwrags):
    print("Post save working..........")
post_save.connect(save_post,sender=sig)
pre_save.connect(save_pre,sender=sig)
@receiver(post_save, sender=User)
def profile(sender, instance,created,**kwrags):
    if created:
        Timetable.objects.create(user=instance)
    
