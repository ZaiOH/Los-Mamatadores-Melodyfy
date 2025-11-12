from django.contrib.auth.models import User
from django.db import models

from usuarios.models import Artista

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE)
    publicacion = models.DateField()
    archivo = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duracion = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.nombre

class LDR(models.Model):
    nombre = models.CharField(max_length=100)
    editores = models.ManyToManyField(User)
    canciones = models.ManyToManyField(Cancion)
