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
    
    nombre_usuario = models.CharField(max_length=30)
    USERNAME_FIELD = 'nombre_usuario'

class Artista(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        models.CASCADE,
        primary_key=True,
    )
