from django.urls import path
from .views import verProductos, Home, agregarProd

urlpatterns = [
    path('', Home, name='Inicio'),
    path('AgregarProductos/', agregarProd, name='Agregar'),
    path('Productos/', verProductos, name='Producto'),
]