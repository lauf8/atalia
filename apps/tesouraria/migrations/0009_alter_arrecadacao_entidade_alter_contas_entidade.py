# Generated by Django 4.2.7 on 2023-11-27 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0006_alter_patrimonio_nome'),
        ('tesouraria', '0008_arrecadacao_pagamento_alter_fornecedor_tipo_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrecadacao',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidade_arrecadacao', to='entidade.entidade'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='entidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entidade_conta', to='entidade.entidade'),
        ),
    ]