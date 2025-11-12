from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistroFormUsuario(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    contraseña_confirmacion = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_confirm(self):
        contraseña = self.cleaned_data.get('contraseña')
        contraseña_confirmacion = self.cleaned_data.get('contraseña_confirmacion')
        if contraseña and contraseña_confirmacion and contraseña != contraseña_confirmacion:
            raise ValidationError(_("Las contraseñas no coinciden"))
        return contraseña_confirmacion

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['contraseña'])
        if commit:
            usuario.save()
        return usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
