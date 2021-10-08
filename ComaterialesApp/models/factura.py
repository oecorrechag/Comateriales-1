from django.db import models
from .producto import Producto
from .pedido import Pedido


class Factura(models.Model):
    id_detalles = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    precio = models.BigIntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    
