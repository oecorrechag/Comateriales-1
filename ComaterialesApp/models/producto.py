from django.db import models
from .catalogo import Catalogo

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100, null=False)
    precio = models.IntegerField(null=False)
    descripcion =  models.CharField(max_length=100, null=False)
    marca = models.CharField(max_length=15, null=False)
    fabricante = models.CharField(max_length=15, null=False)
    fecha_creacion = models.DateTimeField(null=False)
    unidades = models.IntegerField(null=False)
    id_catalogo =  models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    categoria_catalogo = models.CharField(max_length=10)
    clasificacion_catalogo = models.CharField(max_length=10)
