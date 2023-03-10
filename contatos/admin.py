from django.contrib import admin
from .models import Categoria, Contato

# Muda o título do admin
admin.site.site_header = 'Agenda Administrador'


# Exibindo mais campos na listagem de contatos
class ContadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    # Exibindo os campos que serão links
    list_display_links = ('id', 'nome', 'sobrenome')
    #  Exibindo os campos que serão usados para filtrar a listagem
    # list_filter = ('nome', 'sobrenome')
    # mostra 10 contatos por página
    list_per_page = 8
    # Exibe um campo de busca
    search_fields = ('nome', 'sobrenome', 'telefone')
    # Torna os campos listados editáveis
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContadoAdmin)