from django.contrib.auth.models import User
from django.db.models import query
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from contenido.models import LDR, Cancion

class VistaPrincipal(TemplateView):
    template_name = "base.html"

def ver_ldr(request, ldr_id=None):
    usuario = request.user
    ldr = get_object_or_404(LDR, id=ldr_id)

    if request.method == "POST" and "renombre" in request.POST:
        ldr.nombre = request.POST["renombre"]
        ldr.save()
        return redirect("ver-ldr", ldr_id=ldr_id)
    canciones = ldr.canciones.all()
    if usuario is not None and not usuario.is_anonymous:
        is_editor = ldr.editores.contains(usuario)
    else:
        is_editor = False

    context = {
        'id': ldr_id,
        'is_editor': is_editor,
        'nombre': ldr.nombre,
        'canciones': canciones,
        'ids': [c.id for c in canciones],
    }

    return render(request, 'contenido/ldr.html', context)

def buscar_contenido(request):
    query = request.GET.get('q', '')
    tipo = int(request.GET.get("tipo", 0))
    resultados = []

    if query:
        if tipo == 0:
            resultados = User.objects.filter(username__icontains=query)
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
    ldr.editores.add(usuario)

    return redirect("ver-ldr", ldr_id=ldr.id) 

# Esta función impura difiere de buscar_contenido en que regresa los resultados como json
def buscar_usuarios(request):
    query = request.GET.get("q", "")
    coincidencias = []
    if query:
        coincidencias = [{"id": user.id, "nombre": user.username} for user in User.objects.filter(username__icontains=query)] 

    return JsonResponse(coincidencias, safe=False)

def buscar_canciones(request):
    query = request.GET.get("q", "")
    coincidencias = []
    if query:
        coincidencias = [{"id": cancion.id, "nombre": cancion.nombre, "autor": cancion.autor.usuario.username} for cancion in Cancion.objects.filter(nombre__icontains=query)]
    return JsonResponse(coincidencias, safe=False)

@login_required
def añadir_cancion_ldr(request, ldr_id, cid):
    usuario = request.user
    ldr = get_object_or_404(LDR, id=ldr_id)
    cancion = get_object_or_404(Cancion, id=cid)

    if ldr.editores.contains(usuario):
        ldr.canciones.add(cancion)
        return HttpResponse(status=204)
    else:
        return HtttpResponse("No eres editor de esta lista", status=500)
