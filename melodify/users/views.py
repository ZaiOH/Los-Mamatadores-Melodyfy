from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def see_user(request):
    return HttpResponse('Hello World')