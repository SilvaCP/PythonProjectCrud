# Generated by Django 4.2 on 2023-04-20 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_registration_app', '0002_alter_filmes_ano_alter_filmes_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='bilheteria',
            field=models.CharField(max_length=150),
        ),
    ]