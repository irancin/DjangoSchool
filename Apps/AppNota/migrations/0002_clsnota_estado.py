# Generated by Django 2.2.6 on 2019-10-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clsnota',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
