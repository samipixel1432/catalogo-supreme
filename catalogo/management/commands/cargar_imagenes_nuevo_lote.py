# -*- coding: utf-8 -*-
import base64, os
from collections import defaultdict
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import Categoria, Producto, ProductoImagen

CARPETA_DEFAULT = r'C:\Users\PC\Downloads\OtroMas\Otro mas'

IMAGEN_MAP = {
    'IMG-20260517-WA0272.jpg': ('Oxímetro de Pulso Fingertip LK87',              'Ejercicio'),
    'IMG-20260517-WA0273.jpg': ('Almohada Térmica Inteligente USB',               'Ejercicio'),
    'IMG-20260517-WA0274.jpg': ('Almohada Masajeadora Car & Home',                'Ejercicio'),
    'IMG-20260517-WA0275.jpg': ('Estantería Rinconera Multi Corner Shelf',        'Hogar'),
    'IMG-20260517-WA0276.jpg': ('Combo Smartwatch Auriculares Consola 400 en 1', 'Tecnología'),
    'IMG-20260517-WA0277.jpg': ('Ultrasonic Ionic Skin Scrubber',                 'Belleza'),
    'IMG-20260517-WA0278.jpg': ('Airbrush Eléctrico Hobby & Fun',                 'Juguetes'),
    'IMG-20260517-WA0279.jpg': ('Cepillo Eléctrico Multifuncional NGTV-117',     'Hogar'),
    'IMG-20260517-WA0280.jpg': ('Rack Colgador de Ropa Doble Barra',              'Hogar'),
    'IMG-20260517-WA0281.jpg': ('Organizador de Especias Giratorio 12 Frascos',  'Cocina'),
    'IMG-20260517-WA0282.jpg': ('Rizador Automático de Cabello',                  'Belleza'),
    'IMG-20260517-WA0283.jpg': ('Aspiradora de Mano para Carros',                 'Hogar'),
    'IMG-20260517-WA0284.jpg': ('Rack Colgador de Ropa Doble Barra',              'Hogar'),
    'IMG-20260517-WA0285.jpg': ('Aspiradora de Mano para Carros',                 'Hogar'),
    'IMG-20260517-WA0286.jpg': ('Magic Mop con Cubo Giratorio',                   'Hogar'),
    'IMG-20260517-WA0287.jpg': ('Bandas de Resistencia con Manijas',              'Ejercicio'),
    'IMG-20260517-WA0288.jpg': ('Batidora Eléctrica Recargable',                  'Cocina'),
    'IMG-20260517-WA0289.jpg': ('Combo Termo y Pocillos Vacuum Flask',            'Cocina'),
    'IMG-20260517-WA0290.jpg': ('Aspiradora Vertical Vacuum Cleaner',             'Hogar'),
    'IMG-20260517-WA0291.jpg': ('Ventilador Doble con Spray USB LED',             'Hogar'),
    'IMG-20260517-WA0292.jpg': ('Masajeador Compacto Power',                      'Ejercicio'),
    'IMG-20260517-WA0293.jpg': ('Plancha Remington Shine Therapy',                'Belleza'),
    'IMG-20260517-WA0294.jpg': ('Xingchao Lint Remover',                          'Hogar'),
    'IMG-20260517-WA0295.jpg': ('Máquina Cortadora de Cabello Profesional 9 Piezas', 'Belleza'),
}


def _b64(ruta):
    ext = os.path.splitext(ruta)[1].lower()
    mime = 'image/jpeg' if ext in ('.jpg', '.jpeg') else 'image/png'
    with open(ruta, 'rb') as f:
        return f'data:{mime};base64,{base64.b64encode(f.read()).decode()}'


class Command(BaseCommand):
    help = 'Carga las imágenes WA0272-WA0295 a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('--carpeta', default=CARPETA_DEFAULT)
        parser.add_argument('--limpiar', action='store_true')

    def handle(self, *args, **options):
        carpeta = options['carpeta']
        if not os.path.isdir(carpeta):
            raise CommandError(f'Carpeta no encontrada: {carpeta}')

        grupos = defaultdict(list)
        for fname, key in IMAGEN_MAP.items():
            grupos[key].append(fname)

        prod_creados = img_creadas = img_omitidas = 0

        for (nombre, cat_nombre), filenames in grupos.items():
            cat, _ = Categoria.objects.get_or_create(nombre=cat_nombre)
            prod, creado = Producto.objects.get_or_create(
                nombre=nombre, categoria=cat,
                defaults={'disponible': True, 'destacado': False},
            )
            if creado:
                prod_creados += 1
            if options['limpiar']:
                prod.imagenes.all().delete()

            for orden, fname in enumerate(filenames):
                ruta = os.path.join(carpeta, fname)
                if not os.path.exists(ruta):
                    self.stdout.write(self.style.WARNING(f'No encontrado: {fname}'))
                    img_omitidas += 1
                    continue
                if prod.imagenes.filter(orden=orden).exists():
                    img_omitidas += 1
                    continue
                try:
                    ProductoImagen.objects.create(producto=prod, imagen_data=_b64(ruta), orden=orden)
                    img_creadas += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error {fname}: {e}'))
                    img_omitidas += 1

        self.stdout.write(self.style.SUCCESS(
            f'Productos creados: {prod_creados} | Imágenes: {img_creadas} | Omitidas: {img_omitidas}'
        ))
