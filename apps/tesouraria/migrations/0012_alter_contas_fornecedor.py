# Generated by Django 4.2.7 on 2023-12-20 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesouraria', '0011_arrecadacao_user_contas_user_fornecedor_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tesouraria.fornecedor'),
        ),
    ]