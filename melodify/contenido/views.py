from django.contrib.auth.models import User
from django.db.models import query
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from contenido.models import LDR, Cancion
from usuarios.models import Artista
from interaccion.models import Invitacion

# Esta función crea el contexto compartido de todos los templates y le anexa el contexto especifico de cada vista
def make_context(usuario, extra_context = {}):
    if usuario.is_anonymous:
        is_artista = False 
        notificaciones = []
    else:
        is_artista = Artista.objects.contains(usuario)
        notificaciones = [{
            'id': i.id,
            'nombre': i.lista.nombre,
        } for i in Invitacion.objects.filter(destino=usuario, estado='P')]
    return {
        'is_artista': is_artista,
        'notificaciones': notificaciones,
    } | extra_context

def vista_principal(request, ldr_id=None):
    return render(request, 'base.html', context = make_context(request.user))

def ver_ldr(request, ldr_id=None):
    usuario = request.user
    ldr = get_object_or_404(LDR, id=ldr_id)

    if request.method == "POST" and "renombre" in request.POST:
        ldr.nombre = request.POST["renombre"]
        ldr.save()
        return redirect("ver-ldr", ldr_id=ldr_id)
    canciones = ldr.canciones.all()
    editores = [e.id for e in ldr.editores.all()]
    if usuario is not None and not usuario.is_anonymous:
        is_artista = Artista.objects.contains(usuario) 
        is_editor = ldr.editores.contains(usuario)
    else:
        is_editor = False

    is_ultimo = ldr.editores.all().count() == 1

    context = make_context(usuario, {
        'id': ldr_id,
        'is_artista': is_artista,
        'is_editor': is_editor,
        'is_ultimo': is_ultimo,
        'nombre': ldr.nombre,
        'canciones': canciones,
        'cids': [c.id for c in canciones],
        'editores': editores,
    })

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
        return HttpResponse("No eres editor de esta lista", status=401)

@login_required
def eliminar_cancion_ldr(request, ldr_id, cid):
    usuario = request.user
    ldr = get_object_or_404(LDR, id=ldr_id)
    cancion = get_object_or_404(Cancion, id=cid)

    if ldr.editores.contains(usuario):
        ldr.canciones.remove(cancion)
        return HttpResponse(status=204)
    else:
        return HttpResponse("No eres editor de esta lista", status=401)

@login_required
def abandonar_ldr(request, ldr_id):
    usuario = request.user
    ldr = get_object_or_404(LDR, id=ldr_id)

    ldr.editores.remove(usuario)
    if ldr.editores.all().count() == 0:
        ldr.delete()
    
    return redirect("inicio")
