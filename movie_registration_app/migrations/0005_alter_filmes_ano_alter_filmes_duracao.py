# Generated by Django 4.2 on 2023-04-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_registration_app', '0004_remove_filmes_acoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='duracao',
            field=models.IntegerField(),
        ),
    ]
