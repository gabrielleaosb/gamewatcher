from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, CustomAuthenticationForm

def auth_view(request):
    """ View para lidar com login e cadastro """
    login_form = CustomAuthenticationForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('home')
            else:
                messages.error(request, "Erro no cadastro. Verifique os campos.")
        else:
            login_form = CustomAuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")

    context = {
        'form': login_form,
        'register_form': register_form
    }
    return render(request, 'users/auth.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('home')
