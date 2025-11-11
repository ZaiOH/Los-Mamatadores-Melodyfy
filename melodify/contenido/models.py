from django.db import models

from usuarios.models import Artista, Usuario

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.ForeignKey(
        Artista,
        models.CASCADE,
    )
    #imagen = models.ImageField()
    publicacion = models.DateField()
    archivo = models.FileField()

class LDR(models.Model):
    nombre = models.CharField(max_length=100)
    editores = models.ManyToManyField(Usuario)
    canciones = models.ManyToManyField(Cancion)
