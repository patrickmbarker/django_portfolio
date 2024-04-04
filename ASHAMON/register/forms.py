from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):  ##This new class inherits from UserCreationForm
    email = forms.EmailField()

    class Meta:   #this allows to save into users db
        model = User 
        fields = ["username","email","password1", "password2"] #this specifies the order that we want the fields to show up in the form.