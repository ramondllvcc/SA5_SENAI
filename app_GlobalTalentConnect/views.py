from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario


def usuarios_home(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.pais_trabalho = request.POST.get('pais_trabalho')
        novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'html/lista_de_usuarios.html', usuarios)


def cadastro(request):
    return render (request, 'html/cadastro.html')

def excluir_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    usuario.delete()
    return reversed('aba_excluir:excluir_usuario')

    
def exclusao(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'html/excluir_usuario.html', usuarios)
