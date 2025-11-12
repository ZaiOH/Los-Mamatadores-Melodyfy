from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from contenido.models import LDR, Cancion

class VistaPrincipal(TemplateView):
    template_name = "base.html"

def ver_ldr(request, ldr_id=None):
    ldr = get_object_or_404(LDR, id=ldr_id)

    #TODO: checar que es editor
    if request.method == "POST" and "renombre" in request.POST:
        ldr.nombre = request.POST["renombre"]
        ldr.save()
        return redirect("ver-ldr", ldr_id=ldr_id)
    canciones = ldr.canciones.all()
    is_editor = False#ldr.editores.contains(request.user)

    context = {
        'id': ldr_id,
        'is_editor': is_editor,
        'nombre': ldr.nombre,
        'canciones': canciones
    }

    return render(request, 'contenido/ldr.html', context)

def buscar_contenido(request):
    query = request.GET.get('q', '')
    tipo = int(request.GET.get("tipo", 0))
    resultados = []

    if query:
        if tipo == 0:
            resultados = User.objects.filter(nombre_usuario__icontains=query)
        elif tipo == 1: 
            resultados = Cancion.objects.filter(nombre__icontains=query)
        elif tipo == 2:
            resultados = LDR.objects.filter(nombre__icontains=query)

    context = {
        'query': query,
        'resultados': resultados,
        'tipo': tipo,
    }

    return render(request, "contenido/busqueda.html", context=context)

@login_required
def crear_ldr(request):
    usuario = request.user
    ldr = LDR.objects.create(nombre="Nueva lista de reproduccion")
    ldr.save()
    ldr.editores.add(request.user)

    return redirect("ver-ldr", ldr_id=ldr.id)
