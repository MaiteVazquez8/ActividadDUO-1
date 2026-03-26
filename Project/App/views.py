from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def Home(request):
    return render(request,'Base.html')

def agregarProd(request):
    producto=Producto.objects.all()
    data={
        'Formularios':FormularioProductos()
    }
    if request.method=='POST':
        query=FormularioProductos(data=request.POST,files=request.FILES)
        if query.is_valid():
            query.save()
            data['Mensaje']='Datos Registrados'
        else:
            data['Formularios']=FormularioProductos()

    return render(request,'Pages/agregarProductos.html',data)

def verProductos(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    print(productos)  # Esto imprimirá en la consola del servidor los productos obtenidos.
    data = {
        'productos': productos
    }
    return render(request, 'Pages/Productos.html', data)