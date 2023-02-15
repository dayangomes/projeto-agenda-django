from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email # Importa a função de validação de email
from django.contrib.auth.models import User # Importa o model User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST': 
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not usuario or not email or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio!')
        return render(request, 'accounts/cadastro.html')
    123456
    # Validação de email
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'accounts/cadastro.html')

    # Validação de usuario
    if len(usuario) < 3:
        messages.error(request, 'Usuário precisa ter no mínimo 6 caracteres!')
        return render(request, 'accounts/cadastro.html')

    # Validação de senha
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter no mínimo 6 caracteres!')
        return render(request, 'accounts/cadastro.html')

    # Validação das duas senha
    if senha != senha2:
        messages.error(request, 'Senhas informadas não são iguais!')
        return render(request, 'accounts/cadastro.html')

    # Verifica se o usuario já esta cadastrado na area admin do Django
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'accounts/cadastro.html')

    # Verifica se o email já esta cadastrado na area admin do Django
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Faça seu login.')
    user = User.objects.create_user(
        username=usuario, 
        email=email, 
        password=senha, 
        first_name=nome,
        last_name=sobrenome,
    )
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
