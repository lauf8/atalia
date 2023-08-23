from apps.tesouraria.models import Tipo_conta, Tipo_arrecadacao
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesouraria', '0003_contas_pagamento_fornecedor_pix_fornecedor_tipo_pix'),
    ]
    def criar_despesas_contas(apps, schema_editor):
        Tipo_arrecadacao.objects.create(nome='Aluguel')
        Tipo_arrecadacao.objects.create(nome='Arrecadação de Fundos')
        Tipo_arrecadacao.objects.create(nome='Tronco da Solidaredade')
        Tipo_arrecadacao.objects.create(nome='Doação')
        
        Tipo_conta.objects.create(nome = 'Aluguel')
        Tipo_conta.objects.create(nome = 'Conta de Água')
        Tipo_conta.objects.create(nome = 'Conta de Luz')
        Tipo_conta.objects.create(nome = 'Supermercado')
        Tipo_conta.objects.create(nome = 'Limpeza')
        Tipo_conta.objects.create(nome = 'Manutenção')

        

   
    operations = [
        migrations.AddField(
            model_name='contas',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RunPython(criar_despesas_contas),
    ]
