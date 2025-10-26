from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    pass

class Artista(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        models.CASCADE,
        primary_key=True,
    )
