from rest_framework import serializers 
from ComaterialesApp.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id_cliente', 'full_name']