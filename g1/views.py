# -*- coding: utf-8 -*-
import sys, os
from django.shortcuts import render
from django.http import HttpResponse
from g1.models import Evento,Pessoa, EventoCientifico, ArtigoCientifico, Autor, PessoaJuridica, PessoaFisica, Participante
def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/eventoscientificos'>Eventos Cientificos</a></li>
                    <li><a href='/pessoa'>Pessoa</a></li>
                    <li><a href='/pessoafisica'>Pessoa fisica</a></li>
                    <li><a href='/pessoajuridica'>Pessoa Juridica</a></li>
                    <li><a href='/autor'>Autor</a></li>
                    <li><a href='/artigocientifico'>Artigo Cientifico</a></li>
                    <li><a href='/eventosid/7'>Eventos com id 7</a></li>
                </ul>
            """
    return HttpResponse(html)
def listaEvento(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        html += '<li>'+'|'+evento.nome+'|'+evento.eventoPrincipal+'|'+evento.sigla+'|'+str(evento.dataEhoraDeInicio)+'|'+evento.palavrasChave+'|'+evento.realizador+' | '+evento.cidade+' | '+evento.uf+' | '+evento.endereco+' | '+evento.cep
    return HttpResponse(html)

def eventoId(request, id):
    try:
        evento = Evento.objects.get(pk = id)
        html = "<h1>Eventos por ID</h1>"
        html += '<li>'+' | '+evento.nome+' | '+evento.eventoPrincipal+' | ' +evento.sigla+' | '+str(evento.dataEhoraDeInicio)+' | '+evento.palavrasChave+' | '+evento.logoTipo+' | '+evento.cidade+' | '+evento.uf+ ' | '+evento.endereco+ ' | ' +evento.cep + '</li>'

        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Esse evento não existe!</center></h1>")

def listaEventoCientificos(request):
    html = "<h1>Lista de Evento Cientificos </h1>"
    lista = EventoCientifico.objects.all()
    for evento in lista:
        html += '<li>'+evento.issn+'</li>'
    return HttpResponse(html)


def eventoCientificosId(request, id):
    try:
        evento = EventoCientificos.objects.get(pk = id)
        html = "<h1>Evento Cientifico por ID</h1>"
        html += '<li>'+' | '+evento.issn+'</li>'

        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Esse Evento Cientifico não existe!</center></h1>")

def listaPessoa(request):
    html = "<h1>Lista de Pessoa</h1>"
    lista = Pessoa.objects.all()
    for pessoa in lista:
        html += '<li>'+pessoa.nome+'|'+pessoa.email+'</li>'
    return HttpResponse(html)

def pessoaId(request, id):
    try:
        pessoa = Pessoa.objects.get(pk = id)
        html = "<h1>Pessoa por ID</h1>"
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Essa pessoa não existe!</center></h1>")

def listaPessoaFisica(request):
    html = "<h1>Lista de Pessoa fisica</h1>"
    lista = PessoaFisica.objects.all()
    for pessoa in lista:
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.cpf+'</li>'
    return HttpResponse(html)

def pessoaFisicaId(request, id):
    try:
        pessoa = PessoaFisica.objects.get(pk = id)
        html = "<h1>Pessoa por ID</h1>"
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.cpf+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Essa pessoa fisica não existe!</center></h1>")


def listaPessoaJuridica(request):
    html = "<h1>Lista de Pessoa Juridica</h1>"
    lista = PessoaFisica.objects.all()
    for pessoa in lista:
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.cnpj+'|'+pessoa.razaoSocial+'</li>'
    return HttpResponse(html)

def pessoaJuridicaId(request, id):
    try:
        pessoa = PessoaJuridica.objects.get(pk = id)
        html = "<h1>Pessoa por ID</h1>"
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.cnpj+'|'+pessoa.razaoSocial+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Essa pessoa juridica não existe!</center></h1>")


def listaAutor(request):
    html = "<h1>Lista Autores</h1>"
    lista = Autor.objects.all()
    for pessoa in lista:
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.curriculo+'|'+pessoa.artigos+'</li>'
    return HttpResponse(html)

def autoresId(request, id):
    try:
        pessoa = Autor.objects.get(pk = id)
        html = "<h1>Autor por ID</h1>"
        html += '<li>'+'|'+pessoa.nome+'|'+pessoa.email+'|'+pessoa.curriculo+'|'+pessoa.artigos+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Essa Autor não existe!</center></h1>")

def listaArtigoCientifico(request):
    html = "<h1>Lista Artigos Cientificos</h1>"
    lista = ArtigoCientifico.objects.all()
    for art in lista:
        html += '<li>'+'|'+art.titulo+'|'+art.autores+'|'+art.evento+'|'+'</li>'
    return HttpResponse(html)


def artigoCientificoId(request, id):
    try:
        pessoa = ArtigoCientifico.objects.get(pk = id)
        html = "<h1>Artigo Cientifico por ID</h1>"
        html += '<li>'+'|'+art.titulo+'|'+art.autores+'|'+art.evento+'|'+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse("<h1><center>Esse artigo não existe!</center></h1>")

def inscricao(request):
    if request.method == 'POST':
        inscricao = Participante()
        inscricao.dataEhoraDeInicio= request.POST['dataEhoraDeInicio']
        inscricao.tipo =request.POST['Professor', 'Aluno', 'Profissional']
        inscricao.save()
        return HttpResponse('Inscricao Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção de Inscricao')
