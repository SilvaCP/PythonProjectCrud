from django.db import models

# Create your models here.
class Filmes(models.Model):
    filme = models.CharField(max_length=150)
    ano = models.CharField(max_length=150)
    duracao = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    bilheteria = models.CharField(max_length=100)







