from django.forms import ModelForm, RadioSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *


Roles =[
    ('Admin', 'Admin'),
    ('Data_Entry', 'Data_Entry'),
]


class creat(ModelForm):
    class Meta:
        model = create
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    parmission = forms.ChoiceField(widget=RadioSelect(), choices=Roles)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']