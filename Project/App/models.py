from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Producto(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=20)
    Cantidad=models.IntegerField()
    Precio=models.FloatField()
    Descripcion=RichTextField()
    Imagen=models.ImageField(upload_to='Productos',null=True)
    Categoria=models.TextField(max_length=20)
    Colores=models.TextField(max_length=20)
    
    def __int__(self):
        return self.Nombre