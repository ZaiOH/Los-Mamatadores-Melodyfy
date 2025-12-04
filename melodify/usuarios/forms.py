from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RegistroFormUsuario(UserCreationForm):

    email = forms.EmailField(
        label='Correo electrónico',
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )
    
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
    )

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        help_text=None,
    )

    password2 = forms.CharField(
        label='Validar contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Validar contraseña'}),
        help_text=None,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            self.add_error(
                'password2',
                ValidationError(
                    "Las contraseñas no coinciden." 
                )
            )

        
        if email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        "El correo que ingresaste ya está asociado a una cuenta."
                    )
                )

        if username:
            if User.objects.filter(username=username).exists():
                self.add_error(
                    'username',
                    ValidationError(
                        "El nombre de usuario que ingresaste ya está asociado a una cuenta."
                    )
                )
                
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
