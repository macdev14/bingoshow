from django import forms
from .models import Pergunta, Usuario
from django.core.exceptions import ValidationError
from django.contrib import admin
class UserForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = '__all__'

