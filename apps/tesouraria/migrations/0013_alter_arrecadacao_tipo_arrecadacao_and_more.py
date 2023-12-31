# Generated by Django 4.2.7 on 2023-12-20 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tesouraria', '0012_alter_contas_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrecadacao',
            name='tipo_arrecadacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tesouraria.tipo_arrecadacao'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='tipo_despesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tesouraria.tipo_conta'),
        ),
    ]
