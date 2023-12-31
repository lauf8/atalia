# Generated by Django 4.2.4 on 2023-08-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesouraria', '0002_alter_fornecedor_nome_alter_tipo_arrecadacao_nome_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contas',
            name='pagamento',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='pix',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='tipo_pix',
            field=models.CharField(blank=True, choices=[('CPF', 'CPF'), ('CNPJ', 'CNPJ'), ('EMAIL', 'E-mail'), ('CHAVE', 'Chave Aleatória'), ('TELEFONE', 'Telefone')], max_length=8, null=True),
        ),
    ]
