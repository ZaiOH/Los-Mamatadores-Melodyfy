from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(validators=[MinLengthValidator(5)],max_length=15)
    email = models.EmailField()
    description = models.CharField(max_length=325)
    born_date = models.DateField()
    password = models.TextField(validators=[MinLengthValidator(5)])

class Artist(models.Model):
    user = models.OneToOneField(
        'users.User',
        models.CASCADE,
        primary_key=True,
    )

class Follows(models.Model):
    base_user= models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="base_user")
    target_user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="target_user")
    date = models.DateTimeField()

class ReproductionCounter(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    song = models.ForeignKey('content.Song', on_delete=models.CASCADE)
    amount = models.IntegerField(db_default=0)

class SongLikes(models.Model):
    user  = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_liking')
    song = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='song')

