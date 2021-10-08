from rest_framework import serializers 
from ComaterialesApp.models.factura import Factura

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ['id_detalles', 'precio','cantidad']
