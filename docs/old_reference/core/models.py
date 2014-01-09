from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=70)
    senha = models.CharField(max_length=70)
    grupo = models.IntegerField()
    def __unicode__(self):
        return self.usuario

class Pauta(models.Model):
    STATUS_CHOICE = (
            (1, 'Proposta'),
            (2, 'Deliberacao'),
            (3, 'Votacao'),
            (4, 'Fechada')
            )
    usuario = models.ForeignKey(Usuario)
    data_criacao = models.DateField("Data", auto_now_add=True)
    data_validacao = models.DateField("Data Validacao")
    data_delibera = models.DateField("Data Deliberacao")
    data_votacao = models.DateField("Data Votacao")
    votos_promover = models.IntegerField()
    titulo = models.CharField(max_length=70)
    pauta = models.TextField()
    status = models.IntegerField(max_length=1, choices = STATUS_CHOICE)
    def __unicode__(self):
        return self.titulo


class Deliberacao(models.Model):
    pauta = models.ForeignKey(Pauta)
    usuario = models.ForeignKey(Usuario)
    proposta = models.TextField()
    def __unicode__(self):
        return self.proposta

class Voto(models.Model):
    VOTE_CHOICE = (
            (1,  'Favor'),
            (-1, 'Contra'),
            )
    pauta = models.ForeignKey(Pauta, null=True)
    usuario = models.ForeignKey(Usuario)
    deliberacao = models.ForeignKey(Deliberacao, null=True)
    tipo = models.IntegerField(max_length=1, choices = VOTE_CHOICE)
    def __unicode__(self):
        return self.usuario.usuario

class Comentario(models.Model):
    pauta = models.ForeignKey(Pauta)
    datahora = models.DateTimeField("Data e Hora",auto_now_add=True)
    texto = models.TextField()
    def __unicode__(self):
        return self.texto
