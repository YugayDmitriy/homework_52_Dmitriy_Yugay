# Generated by Django 3.2 on 2022-09-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discription',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
