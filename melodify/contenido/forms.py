from django import forms
from .models import Cancion

class CancionForm(forms.Form):
    nombre = forms.CharField(min_length=5, max_length=200)
    archivo = forms.FileField()
