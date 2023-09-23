# Generated by Django 4.2.5 on 2023-09-23 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageOfPreparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.CharField(verbose_name='Фото')),
                ('description', models.CharField(verbose_name='Описание')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Этап приготовления',
                'verbose_name_plural': 'Этапы приготовления',
            },
        ),
    ]