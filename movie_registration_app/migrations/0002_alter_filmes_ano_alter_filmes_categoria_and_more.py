# Generated by Django 4.2 on 2023-04-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='ano',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='duracao',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='categoria',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='filme',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='bilheteria',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='premiacoes',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='sinopse',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='acoes',
            field=models.CharField(max_length=150),
        ),
    ]
