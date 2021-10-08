from rest_framework import serializers 
from ComaterialesApp.models.catalogo import Catalogo

class CatalogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalogo
        fields = ['id_catalogo', 'categoria']