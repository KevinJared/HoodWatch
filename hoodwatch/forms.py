from django import forms
from .models import *


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','user_name','bio')


class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','location','occupants']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','bio']


class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        fields = ['name','hood','email']
