from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Invitacion
from contenido.models import LDR
from melodify.settings import MAX_INV

@login_required
def invitar_ldr(request, ldr_id, uid):
    usuario = get_object_or_404(User, id=uid)
    ldr = get_object_or_404(LDR, id=ldr_id)

    invitacion, _ = Invitacion.objects.get_or_create(lista=ldr, destino=usuario, defaults={
        'lista': ldr,
        'destino': usuario,
        'intentos': 0
    })

    if invitacion.estado == 'A':
        if ldr.editores.contains(usuario):
            # El usuario ya esta en la lista
            return HttpResponse("Usuario ya en la lista",status=409)
        else:
            # Si una invitacion ya fue aceptada pero el usuario se salió, reiniciar el conteo
            invitacion.estado = 'P'
            invitacion.intentos = 1
            invitacion.save()

            return HttpResponse(status=204)

    if invitacion.estado == 'R':
        if invitacion.intentos < MAX_INV:
            invitacion.intentos += 1
            invitacion.estado = 'P'
            invitacion.save()

            return HttpResponse(status=204)
        else:
            return HttpResponse("Este usario ha dejado claro que no quiere estar aquí", status=410)
    
    if invitacion.estado == 'P':
        return HttpResponse("Invitación pendiente", status=503)

@login_required
def aceptar_invitacion(request, iid):
    usuario = request.user
    invitacion = get_object_or_404(Invitacion, id=iid)
    ldr = invitacion.lista

    # Con esto nos aseguramos que solo el usuario invitado pueda aceptar o rechazar la invitación.
    if usuario.id != invitacion.destino.id:
        return HttpResponse(status=401)
    
    if invitacion.estado == 'A':
        return HttpResponse("El usuario ya acepto la invitacion", status=409)
    if invitacion.estado == 'R':
        return HttpResponse("El usuario ya rechazó la invitacion", status=409)
    if invitacion.estado == 'P':
        invitacion.estado = 'A'
        invitacion.save()
        ldr.editores.add(usuario)
        return redirect("ver-ldr", ldr_id=ldr.id)

def rechazar_invitacion(request, iid):
    usuario = request.user
    invitacion = get_object_or_404(Invitacion, id=iid)
    ldr = invitacion.lista

    if usuario.id != invitacion.destino.id:
        return HttpResponse(status=401)
    
    if invitacion.estado == 'A':
        return HttpResponse("El usuario ya acepto la invitacion", status=409)
    if invitacion.estado == 'R':
        return HttpResponse("El usuario ya rechazó la invitacion", status=409)
    if invitacion.estado == 'P':
        invitacion.estado = 'R'
        invitacion.save()
        return redirect(request.path)