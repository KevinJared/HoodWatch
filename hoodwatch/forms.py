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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('name', 'loc')
