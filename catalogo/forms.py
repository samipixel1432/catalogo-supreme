from django import forms
from .models import Producto, Categoria


class ProductoForm(forms.ModelForm):
    # Campo extra para subir imagen — se convierte a base64 en la vista
    imagen_archivo = forms.ImageField(required=False, label='Subir imagen')

    class Meta:
        model = Producto
        fields = [
            'nombre', 'referencia', 'categoria',
            'descripcion_corta', 'descripcion',
            'precio', 'imagen_url',
            'disponible', 'destacado',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'referencia': forms.TextInput(attrs={'placeholder': 'Ej: REF-001'}),
            'descripcion_corta': forms.TextInput(attrs={'placeholder': 'Descripción breve (máx. 320 caracteres)'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción completa del producto'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
            'imagen_url': forms.URLInput(attrs={'placeholder': 'https://...  (URL externa de imagen)'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'orden']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
