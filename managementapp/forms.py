from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AdduserForm(forms.Form):

     name=forms.CharField(max_length=200)
     pimage=forms.ImageField()
     email=forms.CharField(max_length=200)
     mobile=forms.IntegerField()
     qualification=forms.CharField(max_length=200)
     designation=forms.CharField(max_length=200)

class UserForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']