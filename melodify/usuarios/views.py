from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def login_vista(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == 'POST':
        mail = request.POST.get('email')
        password = request.POST.get('password') 

        usuario = authenticate(request, username = mail, password = password)

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:    
            return render(request, "usuarios/login.html", context= {'error': "Usuario o contraseña incorrectos"})
