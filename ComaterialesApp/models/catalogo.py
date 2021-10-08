from django.db import models

class Catalogo(models.Model):
    id_catalogo = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=10, null=False)
    clasificacion = models.CharField(max_length=10, null=False)
    temporada = models.CharField(max_length=10, null=False)
    