# Projeto de uma Agenda em Django

## Aprendizados

Na construção desse projeto, aprendi várias coisas novas e me familiarizei com várias funcionalidades do framework Django, algumas delas são:
- Pesonalização da área Admin do Django;
- Levantamento de erros 404;
- Alertas com o Django Messages;
- Campo de pesquisa, paginação configuração de arquivos estáticos (CSS, JS e imagens) para personalização do layout da agenda;
- Modelo MVT(Model, View, Templates) do Django;
- Modelo ORM(Object Relational Mapping);
- Utilização do sistema de autenticação do Django para controle de acesso de usuários
- Páginas semifechadas verificando usuários logados;
- Utilização do sistema de formulários do Django para entrada e validação de dados;
- Configuração de ambiente de produção (Nginx, uso de banco de dados em produção, configuração de variáveis de ambiente, etc);

## Instalação

Crie inicialmente um ambiente virtual python na pasta do projeto e ative-o:

1. Criando ambiente virtual:
```bash
  python3 -m venv venv
```
2. Ativando o ambiente virtual:
```bash
  . venv/bin/activate  
```
##
3. Instale o framework Django:
```bash
  pip install django==2.2.3
```
4. ou
```bash
  pip install -r requirements.txt
```
## Demonstração

Execute o seguinte comando para rodar o projeto:
```bash
  pyhton manage.py runserver
```
Clique no link http que será mostrado no terminal para ser redirecionado para a página.
<p>
    <img src="assets/readme/exImg.png">
</p>

## Documentação

Para caso de dúvidas, segue a 
[Documentação](https://docs.djangoproject.com/en/4.1/) do framework utilizado.
