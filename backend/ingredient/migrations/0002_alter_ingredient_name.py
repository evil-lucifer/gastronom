# Generated by Django 4.2.5 on 2023-09-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(unique=True, verbose_name='Название'),
        ),
    ]
