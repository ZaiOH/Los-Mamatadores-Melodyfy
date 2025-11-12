from django.contrib.auth.models import User
from django.db import models

class Artista(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key=True,
    )
