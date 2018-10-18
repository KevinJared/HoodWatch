from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="profile/a.jpg")
    bio = models.CharField(max_length=800,default="Welcome Me!")


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()

class Post(models.Model):
    sitename=models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    Description=models.CharField(max_length=800)
    image = models.FileField(upload_to='posts/')
    post_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    Technology = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ["-pk"]