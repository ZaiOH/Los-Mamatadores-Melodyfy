from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db import models

class Usuario(AbstractBaseUser):
    nombre_usuario = models.CharField(validators=[MinLengthValidator(5)],max_length=15, unique=True)
    email = models.EmailField()
    descripcion = models.CharField(max_length=325)
    fecha_nacimiento = models.DateField()
    contraseña = models.TextField(validators=[MinLengthValidator(5)])
    USERNAME_FIELD = 'nombre_usuario' 

class Artista(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete = models.CASCADE,
        primary_key=True,
    )
