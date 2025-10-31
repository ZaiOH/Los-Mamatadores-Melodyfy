from django.db import models

from usuarios.models import Usuario
from contenido.models import Cancion, LDR

class Reporte(models.Model):
    cancion = models.ForeignKey(Cancion, models.CASCADE, related_name="reportado")
    reportador = models.ForeignKey(Usuario)
    motivo = models.CharField(max_length=255)
    

class Invitacion(models.Model):
    lista = models.ForeignKey(Usuario, models.CASCADE)
    destino = models.ForeignKey(Usuario, models.CASCADE, related_name="invitado")
    intentos = models.PositiveSmallIntegerField()

class Seguir(models.Model):
    seguidor = models.ForeignKey(Usuario, models.CASCADE)
    seguido = models.ForeignKey(Usuario, models.CASCADE)
    fecha = models.DateTimeField()

class CancionLike(models.Model):
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    cancion = models.ForeignKey(Cancion, models.CASCADE)

class LDRLike(models.Model):
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    lista = models.ForeignKey(LDR, models.CASCADE)

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, models.CASCADE)
    cancion = models.ForeignKey(Cancion, models.CASCADE)
    contador = models.PositiveIntegerField()