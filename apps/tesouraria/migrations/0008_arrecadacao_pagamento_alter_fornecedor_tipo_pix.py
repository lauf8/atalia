# Generated by Django 4.2.4 on 2023-09-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tesouraria', '0007_alter_arrecadacao_valor_alter_contas_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrecadacao',
            name='pagamento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='tipo_pix',
            field=models.CharField(blank=True, choices=[('Sem', 'Sem Pix'), ('CPF', 'CPF'), ('CNPJ', 'CNPJ'), ('EMAIL', 'E-mail'), ('CHAVE', 'Chave Aleatória'), ('TELEFONE', 'Telefone')], max_length=8, null=True),
        ),
    ]