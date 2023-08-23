from django.db import models
from entidade.models import Entidade

class Fornecedor(models.Model):
    nome = models.CharField(max_length=75)
    celular = models.CharField(max_length=15)

class Tipo_conta(models.Model):
    nome = models.CharField(max_length=75)

class Tipo_arrecadacao(models.Model):
    nome = models.CharField(max_length=75)

class Contas(models.Model):
    entidade =  models.ForeignKey(Entidade, on_delete=models.CASCADE)
    tipo_despesa = models.ForeignKey(Tipo_conta, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data_recebimento = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)


class Arrecadacao(models.Model):
    entidade =  models.ForeignKey(Entidade, on_delete=models.CASCADE)
    tipo_arrecadacao = models.ForeignKey(Tipo_arrecadacao, on_delete=models.CASCADE)
    pagadaor = models.CharField(max_length=75)
    data_recebimento = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
