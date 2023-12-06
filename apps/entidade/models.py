from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


CHOICES_PARENTESCO = [
    ('FILHO(A)', 'Filho(a)'),
    ('ESPOSA', 'Esposa'),
    ('SOBRINHO(A)', 'Sobrinho(a)'),
    ('NETO(A)', 'Neto(a)'),
    ('SEM_PARENTESCO', 'Sem Parentesco'),
]
class Entidade(models.Model):
    nome = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.nome

class Membro(models.Model):
    nome = models.CharField(max_length=75)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=75)
    celular = PhoneNumberField(null=False, blank=False, unique=True)
    marcon = models.BooleanField(default=False)
    demolay = models.BooleanField(default=False)
    escudeiro = models.BooleanField(default=False)
    abelhinha = models.BooleanField(default=False)
    fdj = models.BooleanField(default=False)
    rosa_do_oriente = models.BooleanField(default=False)
    clube_da_fraternidade = models.BooleanField(default=False)
    parentesco_maconico = models.CharField(max_length=20, choices=CHOICES_PARENTESCO,default= 'SEM_PARENTESCO')
    entidade =  models.ForeignKey(Entidade, on_delete=models.CASCADE)
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



