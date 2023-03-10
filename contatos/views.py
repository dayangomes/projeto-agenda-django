from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Contato
from django.db.models import Q, Value  # importa o Q para fazer buscas mais complexas
from django.db.models.functions import Concat # importa o Concat para concatenar os campos
from django.contrib import messages

def index(request):
    
    contatos = Contato.objects.order_by("-id").filter(
        mostrar=True  # mostra apenas os contatos que estão marcados como mostrar=True
    )  # Posso colocar mais de um filtro, por exemplo: .filter(mostrar=True, nome='João')
    # ordena os contatos por id em ordem decrescente
    # contatos = Contato.objects.all()

    paginator = Paginator(contatos, 5)  # Show 5 contacts per page.
    page = request.GET.get("p")  # p é o nome do parâmetro que será passado na url
    contatos = paginator.get_page(
        page
    )  # contatos é o nome da variável que será passada para o template

    return render(request, "contatos/index.html", {
        "contatos": contatos
    })


# Uma forma de levantar a exceção Http404 é utilizando o método get_object_or_404 do Django:
def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(
        Contato, id=contato_id
    )  # pega o objeto ou levanta um 404

    """ Corrige o erro de quando o contato estiver oculto, ele ser mostrado sendo 
    acessado id no endereço """
    if not contato.mostrar:
        raise Http404()

    return render(request, "contatos/ver_contato.html", {
        "contato": contato
    })


def busca(request):
    termo = request.GET.get("termo")  # pega o termo da url

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, "Campo termo não pode ficar em branco.")
        # messages.add_message(request, messages.SUCCESS, "Testando com mais mensagens.") 
        return redirect('index')

    campos = Concat("nome", Value(" "), "sobrenome")
    # print(termo)

    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo)
        | Q(telefone__icontains=termo)
        | Q(categoria__nome__icontains=termo),
        mostrar=True  # Pega pelo nome, sem precisar ser exatamente igual
    )

    paginator = Paginator(contatos, 5)  # Show 5 contacts per page.
    page = request.GET.get("p")  # p é o nome do parâmetro que será passado na url
    contatos = paginator.get_page(
        page
    )  # contatos é o nome da variável que será passada para o template

    return render(request, "contatos/busca.html", {
        "contatos": contatos
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
