"""lpc_g1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from g1.views import inicio, listaEvento, eventoId, listaEventoCientificos, eventoCientificosId, listaPessoa, pessoaId, listaPessoaFisica, pessoaFisicaId, listaPessoaJuridica, pessoaJuridicaId, listaAutor, autoresId, listaArtigoCientifico, artigoCientificoId, inscricao

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/', inicio),
    url(r'^eventos/', listaEvento),
    url(r'^eventoscientificos/', listaEventoCientificos),
    url(r'^pessoa/', listaPessoa),
    url(r'^pessoafisica/', listaPessoaFisica),
    url(r'^pessoajuridica/', listaPessoaJuridica),
    url(r'^autor/', listaAutor),
    url(r'^artigocientifico/', listaArtigoCientifico),
    url(r'eventoid/([0-9])$', eventoId),
    url(r'eventoid/7', eventoId),
    url(r'eventocientificoid/([0-9])$', eventoCientificosId),
    url(r'pessoaid/([0-9])$', pessoaId),
    url(r'pessoafisicaid/([0-9])$', pessoaFisicaId),
    url(r'pessoajuridicaid/([0-9])$', pessoaJuridicaId),
    url(r'autorid/([0-9])$', autoresId),
    url(r'artigocientificoid/([0-9])$', artigoCientificoId),
    url(r'inscricao/', inscricao),



]
