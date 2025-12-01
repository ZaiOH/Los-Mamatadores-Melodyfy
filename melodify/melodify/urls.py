"""
URL configuration for melodify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido.views import vista_principal, buscar_canciones, buscar_usuarios, ver_ldr, buscar_contenido, crear_ldr, añadir_cancion_ldr, eliminar_cancion_ldr, abandonar_ldr
from interaccion.views import invitar_ldr, aceptar_invitacion, rechazar_invitacion
from usuarios.views import registrar_usuario, login_usuario, logout_usuario 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_usuario, name = 'login'),
    path('registrar/', registrar_usuario, name ="registrar"),
    path('logout/', logout_usuario, name='logout'),
    path('', vista_principal, name = 'inicio'),
    path('ldr/<int:ldr_id>/', ver_ldr, name = 'ver-ldr'),
    path('aldr/<int:ldr_id>/<int:cid>', añadir_cancion_ldr, name='añadir-ldr'),
    path('eldr/<int:ldr_id>/<int:cid>', eliminar_cancion_ldr, name='eliminar-ldr'), 
    path('sldr/<int:ldr_id>', abandonar_ldr, name='abandonar-ldr'),
    path('invldr/<int:ldr_id>/<int:uid>', invitar_ldr, name="invitar-ldr"),
    path('unirldr/<int:iid>', aceptar_invitacion, name="aceptar-invldr"),
    path('rejldr/<int:iid>', rechazar_invitacion, name="rechazar-invldr"),
    path('crear-ldr/', crear_ldr, name = 'crear-ldr'),
    path('buscar/', buscar_contenido, name = "buscar"),
    path('usuarios', buscar_usuarios),
    path('canciones', buscar_canciones),
]
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
