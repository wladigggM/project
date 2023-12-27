# Generated by Django 4.2.7 on 2023-12-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=None, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]