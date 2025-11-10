from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Item

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Tu usuario',
      'class': 'from-contro'
 }
))

password= forms.CharField(widget=forms.PasswordInput(
            attrs={
                'pplaceholder': 'password',
                'class': 'form-control'
            }
        ))

class SignupForm(UserChangeForm):
    class Meta:
        model= User
        fields= ('username', 'email', 'password2')


        username = forms.CharField(widget=forms.EmailInput(
            attrs= {
                'pplaceholder': 'Tu Email',
                'class': 'form-control'
            }
        ))
        password1= forms.CharField(widget=forms.PasswordInput(
            attrs={
                'pplaceholder': 'password',
                'class': 'form-control'
            }
        ))
        password2= forms.CharField(widget=forms.PasswordInput(
            attrs={
                'pplaceholder': 'repite password',
                'class': 'form-control'
            }
        ))
    