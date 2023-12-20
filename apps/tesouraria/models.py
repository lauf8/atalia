from django.db import models
from apps.entidade.models import Entidade
from django.contrib.auth.models import User

CHOICES_PIX = [
    ('Sem', 'Sem Pix'),
    ('CPF', 'CPF'),
    ('CNPJ', 'CNPJ'),
    ('EMAIL', 'E-mail'),
    ('CHAVE', 'Chave Aleatória'),
    ('TELEFONE', 'Telefone'),
]

class Fornecedor(models.Model):
    nome = models.CharField(max_length=75, unique=True)
    celular = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    tipo_pix = models.CharField(max_length=8, choices=CHOICES_PIX,blank=True, null=True)
    pix = models.CharField(max_length=40, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Tipo_conta(models.Model):
    nome = models.CharField(max_length=75, unique=True)
    
    def __str__(self):
        return self.nome

class Tipo_arrecadacao(models.Model):
    nome = models.CharField(max_length=75, unique=True)
    
    def __str__(self):
        return self.nome

class Contas(models.Model):
    entidade =  models.ForeignKey(Entidade, related_name='entidade_conta', on_delete=models.CASCADE)
    tipo_despesa = models.ForeignKey(Tipo_conta, on_delete=models.CASCADE,blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, blank=True, null=True)
    data_recebimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.BooleanField(default=False)
    descricao = models.TextField(blank=True, null=True)
    comprovante = models.ImageField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        despesa = self.tipo_despesa.nome + ' ' +  str(self.valor) + 'R$'
        return despesa



class Arrecadacao(models.Model):
    entidade =  models.ForeignKey(Entidade,related_name='entidade_arrecadacao', on_delete=models.CASCADE)
    tipo_arrecadacao = models.ForeignKey(Tipo_arrecadacao, on_delete=models.CASCADE,blank=True, null=True)
    pagador = models.CharField(max_length=75)
    data_recebimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    pagamento = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

