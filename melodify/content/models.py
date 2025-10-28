from django.db import models
from django import apps
class Song(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'users.Artist',
        models.CASCADE
    )
    publish_date = models.DateField()
    path = models.FilePathField()
    is_published = models.BooleanField(db_default=False)

class LDR(models.Model):
    name = models.CharField(max_length=100)
    collaborators = models.ManyToManyField('users.User')
    songs = models.ManyToManyField('content.Song')
    views = models.IntegerField(db_default=0)
