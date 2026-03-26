from django.shortcuts import render,get_object_or_404
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
    productos = Producto.objects.all()
    print(productos)
    data = {
        'productos': productos
    }
    return render(request, 'Pages/Productos.html', data)

def modificarProducto(request,Codigo):
    buscar=get_object_or_404(Producto,Codigo=Codigo)
    data={
        'Formularios':FormularioProductos(instance=buscar)
    }
    if request.method=='POST':
        query=FormularioProductos(data=request.POST,instance=buscar,files=request.FILES)
        if query.is_valid():
            query.save()
            data['Mensaje']='Producto modificado correctamente'
        else:
            data['Mensaje']='Error al modificar el producto'

    return render(request,'Pages/modificarProducto.html',data)