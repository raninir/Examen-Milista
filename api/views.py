from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Usuario, Lista, Tienda, Producto
from .serializers import TiendaSerializer,ProductoSerializer
import json
# Create your views here.

class TiendaApiShow(APIView):
    def get(self, request):
        tienda = Tienda.objects.all()
        serializer = TiendaSerializer(tienda, many=True)
        return Response(serializer.data)



class ProductoApiShow(APIView):
    def get(self, request):
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many= True)
        return Response (serializer.data)
