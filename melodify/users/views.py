from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def see_user(request, username):
    user_data = User.objects.filter(username__exact=username)
    if user_data.exists():
        user = User.objects.get(pk=1)
        return render(request, "user.html", {
            "username" : user.username,
            "description" : user.description
        })
    else:
        return render(request, "user-not-found.html")