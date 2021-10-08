from django.db import models
from .cliente import Cliente

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pago = models.IntegerField(null=False)
    estado = models.CharField(max_length=20, null=False)
    fecha_creacion = models.DateTimeField(null=False)
    info = models.CharField(max_length=20, null = False)
    