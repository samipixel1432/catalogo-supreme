# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from slugify import slugify

from catalogo.models import Categoria, Producto


CATEGORIAS = {
    'Sandalias': (1, 'Sandalias, slides y calzado abierto.'),
    'Guayos de Futbol': (2, 'Guayos y zapatillas para futbol en cancha.'),
    'Botas y Botines': (3, 'Botas, botines y tenis de cana alta.'),
    'Tenis Nike': (4, 'Tenis deportivos y casuales estilo Nike.'),
    'Tenis Adidas': (5, 'Tenis deportivos y casuales estilo Adidas.'),
    'Tenis Jordan': (6, 'Tenis y botines estilo Jordan.'),
    'Tenis Puma': (7, 'Tenis deportivos y casuales estilo Puma.'),
    'Tenis New Balance': (8, 'Tenis deportivos y casuales estilo New Balance.'),
    'Tenis Reebok': (9, 'Tenis casuales estilo Reebok.'),
    'Tenis Lacoste': (10, 'Tenis casuales estilo Lacoste.'),
    'Tenis Diesel': (11, 'Tenis casuales estilo Diesel.'),
    'Tenis Casual de Marca': (12, 'Tenis casuales de diferentes marcas y estilos.'),
    'Tenis Deportivos': (13, 'Tenis deportivos, running y entrenamiento.'),
}


def seq(*items):
    values = set()
    for item in items:
        if isinstance(item, range):
            values.update(item)
        else:
            values.add(item)
    return values


SANDALIAS = seq(
    range(5, 11), 12, 13, 14, 15,
    range(173, 207), 218,
)

GUAYOS = seq(
    18, 26, 27, 32, 33, range(39, 45), range(55, 59), 61,
    range(64, 68), 69, range(72, 81), range(85, 102),
    range(110, 132), range(207, 218), range(219, 282),
    range(413, 440), 442, 448, 450, 451, 456,
)

BOTINES = seq(
    1, 2, 3, 30, 60, 109, 140, 141, 145, 146, 148, 155,
    164, 337, 338, range(380, 384), 391, range(397, 400),
    409, 411, 412, 417, 418, 457,
)


BRANDS = {
    'Adidas': seq(
        11, 18, 25, 26, 27, 32, 34, range(40, 43), 48, 49, 54, 55,
        61, 62, range(65, 68), 76, range(78, 82), 85, range(96, 102),
        range(110, 118), range(120, 131), 134, 135, 168,
        range(208, 214), range(221, 226), range(229, 235), 240, 241,
        244, 245, 247, 251, 252, range(260, 266), range(268, 271),
        279, 281, range(340, 344), 348, 349, 385, range(403, 407),
        423, 456,
    ),
    'Puma': seq(
        136, range(191, 200), 207, 250, 278, range(302, 305),
        range(350, 355), range(394, 397), range(407, 410),
    ),
    'Jordan': seq(
        60, 109, 140, 141, 145, 146, 148, 155, 164, range(344, 348),
        range(380, 384), 391, 411, 412, 417, 418, 457,
    ),
    'New Balance': seq(54, 220, 235, 243, 246, 266, 271, 282, 283, 286, 342, 343),
    'Reebok': seq(range(287, 291)),
    'Lacoste': seq(305, range(318, 321), 339, 355),
    'Diesel': seq(range(328, 331), range(374, 377), 392, 393),
    'Tommy Jeans': seq(296, range(331, 334)),
    'Hugo Boss': seq(284, 285, 312, 313, 326, 327),
    'Louis Vuitton': seq(294, 295, 297, 298, 321, 378, 379),
    'Le Coq Sportif': seq(range(157, 160), range(394, 397)),
    'Under Armour': seq(range(182, 186), range(437, 440)),
    'Asics': seq(51, 62, range(400, 403), 410),
    'On Running': seq(151),
}


ESTILOS = {
    'Sandalias': ['tipo slide', 'de descanso', 'urbanas', 'con correa ancha'],
    'Guayos de Futbol': ['para futbol', 'de cancha', 'rapidos', 'con tacos'],
    'Botas y Botines': ['cana alta', 'urbanos', 'premium', 'deportivos'],
    'Tenis': ['casuales', 'deportivos', 'urbanos', 'running', 'premium'],
}


def brand_for(product_id):
    for brand, ids in BRANDS.items():
        if product_id in ids:
            return brand
    return 'Nike'


def categoria_for(product_id, brand):
    if product_id in SANDALIAS:
        return 'Sandalias'
    if product_id in GUAYOS:
        return 'Guayos de Futbol'
    if product_id in BOTINES:
        return 'Botas y Botines'
    brand_category = {
        'Nike': 'Tenis Nike',
        'Adidas': 'Tenis Adidas',
        'Jordan': 'Tenis Jordan',
        'Puma': 'Tenis Puma',
        'New Balance': 'Tenis New Balance',
        'Reebok': 'Tenis Reebok',
        'Lacoste': 'Tenis Lacoste',
        'Diesel': 'Tenis Diesel',
    }.get(brand)
    return brand_category or 'Tenis Casual de Marca'


def titulo_for(product_id, brand, categoria, index):
    if categoria == 'Sandalias':
        base = f'Sandalias {brand}'
        estilos = ESTILOS['Sandalias']
    elif categoria == 'Guayos de Futbol':
        base = f'Guayos {brand}'
        estilos = ESTILOS['Guayos de Futbol']
    elif categoria == 'Botas y Botines':
        base = f'Botines {brand}'
        estilos = ESTILOS['Botas y Botines']
    elif categoria == 'Tenis Deportivos':
        base = f'Tenis deportivos {brand}'
        estilos = ESTILOS['Tenis']
    else:
        base = f'Tenis {brand}'
        estilos = ESTILOS['Tenis']
    return f'{base} {estilos[index % len(estilos)]}'


def unique_slug(nombre, product_id):
    base = slugify(nombre) or f'producto-{product_id}'
    return f'{base}-item-{product_id}'


class Command(BaseCommand):
    help = 'Renombra el catalogo de zapatos, mueve los codigos a descripcion y crea categorias.'

    def add_arguments(self, parser):
        parser.add_argument('--apply', action='store_true', help='Guarda los cambios en la base de datos.')

    def handle(self, *args, **options):
        cats = {}
        for nombre, (orden, descripcion) in CATEGORIAS.items():
            cat, _ = Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={'orden': orden, 'descripcion': descripcion},
            )
            if cat.orden != orden or cat.descripcion != descripcion:
                cat.orden = orden
                cat.descripcion = descripcion
                if options['apply']:
                    cat.save(update_fields=['orden', 'descripcion'])
            cats[nombre] = cat

        productos = Producto.objects.order_by('id')
        total = 0
        previews = []

        for index, producto in enumerate(productos):
            codigo = (producto.referencia or '').strip()
            if not codigo and producto.nombre.lower().startswith('producto '):
                codigo = producto.nombre.split(' ', 1)[1].strip()

            brand = brand_for(producto.id)
            categoria_nombre = categoria_for(producto.id, brand)
            nombre = titulo_for(producto.id, brand, categoria_nombre, index)
            descripcion = (
                f'Codigo original del catalogo: {codigo or producto.nombre}. '
                f'Modelo identificado visualmente como {nombre.lower()}.'
            )
            descripcion_corta = f'{nombre}. Codigo original: {codigo or producto.nombre}.'

            previews.append((producto.id, producto.nombre, nombre, categoria_nombre))
            if options['apply']:
                producto.nombre = nombre
                producto.categoria = cats[categoria_nombre]
                producto.descripcion = descripcion
                producto.descripcion_corta = descripcion_corta
                if codigo:
                    producto.referencia = codigo
                producto.slug = unique_slug(nombre, producto.id)
                producto.save(update_fields=[
                    'nombre', 'categoria', 'descripcion', 'descripcion_corta',
                    'referencia', 'slug',
                ])
            total += 1

        for product_id, old, new, cat in previews[:20]:
            self.stdout.write(f'{product_id}: {old} -> {new} [{cat}]')

        accion = 'actualizados' if options['apply'] else 'simulados'
        self.stdout.write(self.style.SUCCESS(f'{total} productos {accion}.'))
