# Generated by Django 2.2.6 on 2019-10-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0002_clsusuario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='clsusuario',
            name='accesso',
            field=models.BooleanField(default=False),
        ),
    ]