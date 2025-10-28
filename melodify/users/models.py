from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(validators=[MinLengthValidator(5)],max_length=15)
    email = models.EmailField()
    description = models.CharField(max_length=325)
    born_date = models.DateField()
    password = models.TextField(validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.username

class Artist(models.Model):
    user = models.OneToOneField(
        'users.User',
        models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return 'Artist ' + self.user.username

class Follows(models.Model):
    base_user= models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="base_user")
    target_user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="target_user")
    date = models.DateTimeField()
    
    def __str__(self):
        return self.base_user.username + "-->" + self.target_user.username


class ReproductionCounter(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    song = models.ForeignKey('content.Song', on_delete=models.CASCADE)
    amount = models.IntegerField(db_default=0)

    def __str__(self):
        return self.user.username + " >> " + self.song.name + ': ' + self.amount

class SongLikes(models.Model):
    user  = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_liking')
    song = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.user.username + " LIKE " + self.song.name

