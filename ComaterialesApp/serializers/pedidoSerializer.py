from rest_framework import serializers 
from comaterialesApp.models.pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['id_pedido', 'info']

