# Generated by Django 4.2.7 on 2024-03-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_reviews_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug_name',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Слаг (предмета))'),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug_name',
            field=models.SlugField(blank=True, max_length=100, verbose_name='Слаг (форен кей)'),
        ),
    ]