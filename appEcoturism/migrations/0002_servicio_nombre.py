# Generated by Django 3.2.9 on 2021-11-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEcoturism', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='nombre',
            field=models.CharField(default='Servicio', max_length=100, verbose_name='nombre'),
            preserve_default=False,
        ),
    ]
