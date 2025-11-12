from django import forms

class LDRNombreForm(forms.Form):
    nuevo_nombre = forms.CharField("Nuevo Nombre de la Lista")

