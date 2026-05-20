import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from urllib.parse import quote
from .models import Categoria, Producto, ProductoImagen
from .forms import ProductoForm, CategoriaForm


def _guardar_imagenes_multiples(request, producto):
    """Guarda todos los archivos enviados como ProductoImagen en base64."""
    archivos = request.FILES.getlist('imagenes_nuevas')
    for i, archivo in enumerate(archivos):
        mime = archivo.content_type or 'image/jpeg'
        datos = base64.b64encode(archivo.read()).decode('utf-8')
        ProductoImagen.objects.create(
            producto=producto,
            imagen_data=f'data:{mime};base64,{datos}',
            orden=producto.imagenes.count() + i,
        )

# Vercel: SQLite is read-only. Disconnect the signal that writes last_login
# to the database on every login — runs at import time, guaranteed to fire.
try:
    from django.contrib.auth.signals import user_logged_in
    from django.contrib.auth.models import update_last_login
    user_logged_in.disconnect(update_last_login)
except Exception:
    pass


def es_staff(user):
    return user.is_active and user.is_staff


# ── Vistas públicas ──────────────────────────────────────────────────────────

def landing(request):
    """Página de inicio / landing principal."""
    return render(request, 'catalogo/landing.html')


def acceso(request):
    """Página de acceso: botón Invitado + formulario Admin."""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('catalogo:panel_dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('catalogo:panel_dashboard')
        error = 'Usuario o contraseña incorrectos, o sin permisos de administrador.'

    return render(request, 'catalogo/acceso.html', {'error': error})


def coleccion(request):
    categorias = Categoria.objects.all()
    categoria_slug = request.GET.get('categoria', '').strip()
    busqueda = request.GET.get('q', '').strip()

    productos = Producto.objects.select_related('categoria').filter(disponible=True)

    categoria_activa = None
    if categoria_slug:
        categoria_activa = Categoria.objects.filter(slug=categoria_slug).first()
        if categoria_activa:
            productos = productos.filter(categoria=categoria_activa)

    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    return render(request, 'catalogo/coleccion.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_activa': categoria_activa,
        'busqueda': busqueda,
        'total_resultados': productos.count(),
    })


def detalle(request, slug):
    producto = get_object_or_404(
        Producto.objects.select_related('categoria'),
        slug=slug, disponible=True,
    )
    relacionados = (
        Producto.objects
        .filter(categoria=producto.categoria, disponible=True)
        .exclude(pk=producto.pk)[:4]
    )

    imagen_url = producto.get_imagen_url()
    lineas = [
        f'Hola, me interesa este producto de *Premier Bodega Importadora*:',
        f'',
        f'*{producto.nombre}*',
        f'Precio: {producto.precio_formateado()}',
    ]
    if producto.referencia:
        lineas.append(f'Ref: {producto.referencia}')
    if producto.descripcion_corta:
        lineas += ['', producto.descripcion_corta]
    if imagen_url and imagen_url.startswith('http'):
        lineas += ['', f'Imagen: {imagen_url}']

    whatsapp_url = (
        f'https://wa.me/{settings.WHATSAPP_NUMBER}'
        f'?text={quote(chr(10).join(lineas))}'
    )

    return render(request, 'catalogo/detalle.html', {
        'producto': producto,
        'relacionados': relacionados,
        'whatsapp_url': whatsapp_url,
    })


# ── Panel admin ──────────────────────────────────────────────────────────────

def panel_login(request):
    return redirect('catalogo:acceso')


def panel_logout(request):
    logout(request)
    return redirect('catalogo:landing')


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_dashboard(request):
    productos = Producto.objects.select_related('categoria').order_by('-creado')
    categorias = Categoria.objects.all()
    busqueda = request.GET.get('q', '').strip()
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
    return render(request, 'panel/dashboard.html', {
        'productos': productos,
        'categorias': categorias,
        'total': productos.count(),
        'busqueda': busqueda,
    })


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_producto_nuevo(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        producto = form.save()
        _guardar_imagenes_multiples(request, producto)
        messages.success(request, 'Producto creado correctamente.')
        return redirect('catalogo:panel_dashboard')
    return render(request, 'panel/producto_form.html', {
        'form': form, 'titulo': 'Nuevo Producto', 'accion': 'Crear',
    })


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        producto = form.save()
        _guardar_imagenes_multiples(request, producto)
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('catalogo:panel_dashboard')
    return render(request, 'panel/producto_form.html', {
        'form': form, 'producto': producto,
        'imagenes': producto.imagenes.all(),
        'titulo': f'Editar: {producto.nombre}', 'accion': 'Guardar cambios',
    })


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_imagen_eliminar(request, pk, img_pk):
    imagen = get_object_or_404(ProductoImagen, pk=img_pk, producto__pk=pk)
    if request.method == 'POST':
        imagen.delete()
        messages.success(request, 'Imagen eliminada.')
    return redirect('catalogo:panel_producto_editar', pk=pk)


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'"{nombre}" eliminado.')
        return redirect('catalogo:panel_dashboard')
    return render(request, 'panel/producto_confirmar_eliminar.html', {'producto': producto})


@login_required(login_url='catalogo:acceso')
@user_passes_test(es_staff, login_url='catalogo:acceso')
def panel_categoria_nueva(request):
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Categoría creada.')
        return redirect('catalogo:panel_dashboard')
    return render(request, 'panel/categoria_form.html', {'form': form, 'titulo': 'Nueva Categoría'})
