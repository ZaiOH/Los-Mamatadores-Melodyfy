from django.contrib.auth.models import User
from django.db import models

from contenido.models import Cancion, LDR

class Reporte(models.Model):
    cancion = models.ForeignKey(Cancion, models.CASCADE, related_name="reportado")
    reportador = models.ForeignKey(User, models.CASCADE)
    motivo = models.CharField(max_length=255)
    

class Invitacion(models.Model):
    ACEPTACION_CHOICES = {
        'R': 'Rechazada',
        'P': 'Pendiente',
        'A': 'Aceptada',
    }
    lista = models.ForeignKey(LDR, models.CASCADE)
    destino = models.ForeignKey(User, models.CASCADE, related_name="invitado")
    intentos = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=1, choices=ACEPTACION_CHOICES, default='A')

class Seguir(models.Model):
    seguidor = models.ForeignKey(User, models.CASCADE, related_name="usuario_seguidor")
    seguido = models.ForeignKey(User, models.CASCADE, related_name="usuario_seguido")
    fecha = models.DateTimeField()

class CancionLike(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)
    cancion = models.ForeignKey(Cancion, models.CASCADE)

class LDRLike(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)
    lista = models.ForeignKey(LDR, models.CASCADE)

class Historial(models.Model):
    usuario = models.ForeignKey(User, models.CASCADE)
    cancion = models.ForeignKey(Cancion, models.CASCADE)
    contador = models.PositiveIntegerField()
