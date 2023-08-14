from rest_framework import generics
from .models import Categoria, Producto
from .serializer import CategoriaSerializer, ProductoSerializer

# Create your views here.
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer