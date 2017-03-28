from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.CharField('email', max_length=100)
    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        super(Pessoa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('eventoPrincipal', max_length=200)
    sigla = models.CharField('sigla', max_length=10)
    dataEhoraDeInicio = models.DateTimeField('dataEhoraDeInicio')
    palavrasChave = models.CharField('palavrasChave', max_length=50)
    logoTipo = models.CharField('logoTipo', max_length=50)
    realizador = Pessoa ()
    cidade = models.CharField('cidade', max_length=50)
    uf = models.CharField('uf', max_length=5)
    endereco = models.CharField('endereco', max_length=200)
    cep = models.CharField('cep', max_length=50 )
    participantes = []

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.endereco = self.endereco.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

class EventoCientifico(Evento ,models.Model):
    issn = models.CharField('issn', max_length=200)
    def save(self, *args, **kwargs):
        self.issn = self.issn.upper()

        super(EventoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return self.issn

class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=50)
    autores = []
    evento = EventoCientifico()
    def save(self, *args, **kwargs):
        self.titulo = self.titulo.upper()

        super(ArtigoCientifico, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Autor(Pessoa, models.Model):
    curriculo = models.TextField('curriculo')
    artigos = []
    def save(self, *args, **kwargs):
        self.curriculo = self.curriculo.upper()

        super(Autor, self).save(*args, **kwargs)

    def __str__(self):
        return self.curriculo


class PessoaJuridica(Pessoa,models.Model):
    cnpj = models.CharField('cnpj', max_length=50)
    razaoSocial = models.CharField('razaoSocial', max_length=100)
    def save(self, *args, **kwargs):
        self.cnpj = self.cnpj.upper()

        super(PessoaJuridica, self).save(*args, **kwargs)

    def __str__(self):
        return self.cnpj


class PessoaFisica(Pessoa, models.Model):
    cpf=models.CharField('cpf', max_length=50)
    def save(self, *args, **kwargs):
        self.cpf = self.cpf.upper()

        super(PessoaFisica, self).save(*args, **kwargs)

    def __str__(self):
        return self.cpf

class Participante(PessoaFisica, models.Model ):
    dataHoraInscricao = models.DateTimeField('data')
    tipoInscricao = models.CharField('tipoInscricao', max_length=50)
    def save(self, *args, **kwargs):
        self.dataHoraInscricao = self.cpf.upper()

        super(Participante, self).save(*args, **kwargs)

    def __str__(self):
        return self.dataHoraInscricao
