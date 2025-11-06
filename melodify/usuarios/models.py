from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Usuario(AbstractBaseUser):
    # Eliminamos los campos que no vamos a utilizar y que nos van a estorbar.
    is_superuser = None
    first_name = None
    last_name = None
    is_staff = None
    is_active = None
    groups = None
    user_permitions = None
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    
    nombre_usuario = models.CharField(max_length=30)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'nombre_usuario', 'password']

class Artista(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        models.CASCADE,
        primary_key=True,
    )
