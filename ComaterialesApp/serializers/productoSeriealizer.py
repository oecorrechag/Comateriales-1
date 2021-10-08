from rest_framework import serializers 
from comaterialesApp.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id_catalogo', 'categoria']