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

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    locations = (
        ('Nairobi', 'Nairobi'),
        ('Zurich', 'Zurich'),
        ('Paris', 'Paris'),
        ('Munich', 'Munich'),
        ('Tokyo', 'Tokyo'),
        ('London', 'London'),
        ('Melbourne', 'Melbourne'),
        ('Sydney', 'Sydney'),
        ('Berlin', 'Berlin')
    )
    loc  = models.CharField(max_length=65, choices=locations)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'

    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods

    def __str__(self):
        return f"{self.loc}"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_biz(cls, hood):
        hoods = Business.objects.filter(hood_id=Neighbourhood)
        return hoods