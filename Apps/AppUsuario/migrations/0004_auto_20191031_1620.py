# Generated by Django 2.2.6 on 2019-10-31 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0003_clsusuario_accesso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clsusuario',
            name='accesso',
            field=models.IntegerField(default=0),
        ),
    ]