from django.db import models
from django.utils import timezone
# A função timezone.now é utilizada como o valor padrão, o que significa que, 
# se você não especificar um valor para esse campo ao criar um novo registro, 
# a data e hora atuais serão automaticamente atribuídas a ele.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    # on_delete=models.DO_NOTHING, faz com que, quando a categoria for apagada, seus Contatos ligados não façam nada.

    def __str__(self): 
        return self.nome
