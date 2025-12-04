from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegistroFormUsuario, LoginForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroFormUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroFormUsuario()
    return render(request, 'usuarios/register.html', {'form': form})

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            form = LoginForm()
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")

    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def logout_usuario(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('login')
