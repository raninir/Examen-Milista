
from rest_framework import serializers
from api.models import Usuario, Lista, Tienda, Producto, ListaUsuario, ListaProducto, TiendaProducto, ListaCompras

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = Tienda



class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        fields = (
             '__all__'
        )
        model = Producto