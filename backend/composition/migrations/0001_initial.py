# Generated by Django 4.2.5 on 2023-09-23 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
        ('ingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Сomposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('count', models.FloatField(verbose_name='Количество')),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredient.ingredient', verbose_name='Ингредиент')),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Состав',
                'verbose_name_plural': 'Состав',
            },
        ),
    ]
