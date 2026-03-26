from django import forms
from .models import *

class FormularioProductos(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'