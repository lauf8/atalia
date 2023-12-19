from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from cpf_field.models import CPFField



class Entidade(models.Model):

    
    nome = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.nome

class Membro(models.Model):


    nome = models.CharField(max_length=75)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=75, blank=True)
    celular = PhoneNumberField(null=False, blank=False, unique=True)
    cpf = CPFField('cpf')
    ativo = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Patrimonio(models.Model):


    nome = models.CharField(max_length=75)
    quantidade = models.IntegerField()
    entidade =  models.ForeignKey(Entidade, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Percapta(models.Model):


    nome = models.CharField(max_length=75)
    captacao = models.DecimalField(max_digits=10, decimal_places=2)
    cmsb = models.DecimalField(max_digits=10, decimal_places=2)
    cmi = models.DecimalField(max_digits=10, decimal_places=2)
    fdj_gleb = models.DecimalField(max_digits=10, decimal_places=2)
    dm_gleb = models.DecimalField(max_digits=10, decimal_places=2)
    reforma = models.DecimalField(max_digits=10, decimal_places=2)
    dm_atalaia = models.DecimalField(max_digits=10, decimal_places=2)
    fdj_atalia = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Mensalidade(models.Model):


    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    percapita = models.ForeignKey(Percapta, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    comprovante = models.ImageField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
