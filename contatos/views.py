from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.core.paginator import Paginator
from .models import Contato

def index(request):
    contatos = Contato.objects.all()

    paginator = Paginator(contatos, 5) # Show 5 contacts per page.
    page = request.GET.get('p') # p é o nome do parâmetro que será passado na url
    contatos = paginator.get_page(page) # contatos é o nome da variável que será passada para o template



    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

# Uma forma de levantar a exceção Http404 é utilizando o método get_object_or_404 do Django:
def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) # pega o objeto ou levanta um 404
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