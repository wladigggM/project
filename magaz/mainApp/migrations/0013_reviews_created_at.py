# Generated by Django 4.2.7 on 2024-03-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_item_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано'),
        ),
    ]
