from rest_framework import viewsets

from API.models import(
    Categoria, Producto
)

from API.serializers import(
    CategoriaSerializer, 
    ProductoSerializer
)
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer