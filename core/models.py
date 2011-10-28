from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=70)
    senha = models.CharField(max_length=70)
    grupo = models.IntegerField()

class Pauta(models.Model):
    usuario = models.ForeignKey(Usuario)
    data_criacao = models.DateField("Data", auto_now_add=True)
    data_validacao = models.DateField("Data Validacao")
    data_delibera = models.DateField("Data Deliberacao")
    data_votacao = models.DateField("Data Votacao")
    votos_promover = models.IntegerField()
    titulo = models.CharField(max_length=70)
    pauta = models.TextField()


class Deliberacao(models.Model):
    pauta = models.ForeignKey(Pauta)
    usuario = models.ForeignKey(Usuario)
    proposta = models.TextField()

class Voto(models.Model):
    pauta = models.ForeignKey(Pauta)
    usuario = models.ForeignKey(Usuario)
    deliberacao = models.ForeignKey(Deliberacao)
    tipo = models.IntegerField()

class Comentario(models.Model):
    pauta = models.ForeignKey(Pauta)
    datahora = models.DateTimeField("Data e Hora",auto_now_add=True)
    texto = models.TextField()
