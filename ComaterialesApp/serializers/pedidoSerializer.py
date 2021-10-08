from rest_framework import serializers 
from ComaterialesApp.models.pedido import Pedido

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['id_pedido', 'info']

