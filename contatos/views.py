from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
# Uma forma de levantar a exceção Http404 é utilizando o método get_object_or_404 do Django:
def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


# uma forma de levantar erros 404
# def ver_contato(request, contato_id):
#     try:
#         contato = Contato.objects.get(id=contato_id)
#         return render(request, 'contatos/ver_contato.html', {
#             'contato': contato
#         })
#     except Contato.DoesNotExist as e:
#         raise Http404()