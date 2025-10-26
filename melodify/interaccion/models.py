from django.db import models

from melodify.usuarios.models import Usuario

class Notificacion(models.Model):
    fecha_creacion = models.DateField()

class Reporte(models.Model):
    notificacion = models.OneToOneField(
        Notificacion,
        models.CASCADE,
        primary_key=True
    )

class Invitacion(models.Model):
    notificacion = models.OneToOneField(
        Notificacion,
        models.CASCADE,
        primary_key=True
    )
    destino = models.ForeignKey(Usuario, models.CASCADE, related_name="invitado")

