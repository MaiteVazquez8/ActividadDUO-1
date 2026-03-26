from django.urls import path
from .views import verProductos, Home, agregarProd, modificarProducto

urlpatterns = [
    path('', Home, name='Inicio'),
    path('AgregarProductos/', agregarProd, name='Agregar'),
    path('Productos/', verProductos, name='Producto'),
    path('ModificarProductos/<Codigo>', modificarProducto, name='Modificar'),
]