# Generated by Django 4.2.7 on 2023-12-21 17:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0009_mensalidade_membro_mensalidade_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='celular',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
