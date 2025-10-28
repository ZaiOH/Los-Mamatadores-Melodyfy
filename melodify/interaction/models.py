from django.db import models

class Notification(models.Model):
    creation_date = models.DateField()
    message = models.TextField(db_default='',max_length=400)

class Report(models.Model):
    notification = models.OneToOneField(
        'interaction.Notification',
        models.CASCADE,
        primary_key=True
    )

class Invitation(models.Model):
    notificacion = models.OneToOneField(
        'interaction.Notification',
        models.CASCADE,
        primary_key=True
    )
    destino = models.ForeignKey('users.User', models.CASCADE, related_name="invited")

