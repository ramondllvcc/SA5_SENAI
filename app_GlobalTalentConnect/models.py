from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    idade = models.IntegerField( null=True)
    email = models.EmailField(default='example@example.com', null=True)
    pais_trabalho = models.CharField(max_length=255, default='Brasil', null=True)