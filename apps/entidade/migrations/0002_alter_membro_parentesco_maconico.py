# Generated by Django 4.2.4 on 2023-08-23 13:16

from django.db import migrations, models
from apps.entidade.models import Entidade



def criar_entidades(apps, schema_editor):
    Entidade.objects.create(nome='Loja')
    Entidade.objects.create(nome='Clube da Fraternidade')
    Entidade.objects.create(nome='Capítulo DeMolay')
    Entidade.objects.create(nome='Castelo')
    Entidade.objects.create(nome='Bethel')
    Entidade.objects.create(nome='Colmeia')



class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='parentesco_maconico',
            field=models.CharField(choices=[('FILHO(A)', 'Filho(a)'), ('ESPOSA', 'Esposa'), ('SOBRINHO(A)', 'Sobrinho(a)'), ('NETO(A)', 'Neto(a)'), ('SEM_PARENTESCO', 'Sem Parentesco')], default='SEM_PARENTESCO', max_length=20),
        ),
        migrations.RunPython(criar_entidades),
    ]