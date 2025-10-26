from django.db import models

from melodify.usuarios.models import Artista, Usuario

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.ForeignKey(
        Artista,
        models.CASCADE,
    )
    publicacion = models.DateField()
    archivo = models.FilePathField()

class LDR(models.Model):
    nombre = models.CharField(max_length=100)
    editores = models.ManyToManyField(Usuario)
    canciones = models.ManyToManyField(Cancion)
