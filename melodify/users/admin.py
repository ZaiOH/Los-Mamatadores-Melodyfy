from django.contrib import admin
from users.models import User, Artist, Follows, ReproductionCounter, SongLikes

# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Follows)
admin.site.register(ReproductionCounter)
admin.site.register(SongLikes)
