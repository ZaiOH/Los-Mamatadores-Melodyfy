from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from contenido.models import LDR

class VistaPrincipal(TemplateView):
    template_name = "base.html"

@login_required
def ver_ldr(request):
    return redirect("")
@login_required
def crear_ldr(request):
    ldr = LDR(nombre="Nueva lista de reproduccion")
    ldr.save()
    ldr.editores.add(request.user)

    return redirect("")
