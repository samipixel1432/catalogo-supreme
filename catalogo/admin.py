from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'orden', 'total_productos']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['orden', 'nombre']

    @admin.display(description='Productos')
    def total_productos(self, obj):
        return obj.productos.count()


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'referencia', 'categoria', 'precio_formateado', 'disponible', 'destacado']
    list_filter = ['disponible', 'destacado', 'categoria']
    list_editable = ['disponible', 'destacado']
    search_fields = ['nombre', 'referencia', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ['categoria__orden', 'nombre']
    list_per_page = 50
    fieldsets = (
        ('Informacion principal', {'fields': ('nombre', 'slug', 'referencia', 'categoria')}),
        ('Contenido', {'fields': ('descripcion_corta', 'descripcion', 'imagen')}),
        ('Precio y visibilidad', {'fields': ('precio', 'disponible', 'destacado')}),
    )
