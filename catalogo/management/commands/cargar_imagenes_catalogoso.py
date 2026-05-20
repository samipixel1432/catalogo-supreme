# -*- coding: utf-8 -*-
"""
Carga las imágenes de la carpeta Catalogoso a la base de datos,
creando categorías, productos y entradas ProductoImagen.

Uso:
    python manage.py cargar_imagenes_catalogoso
    python manage.py cargar_imagenes_catalogoso --limpiar
    python manage.py cargar_imagenes_catalogoso --carpeta "C:/ruta/a/Catalogoso"
"""

import base64
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from catalogo.models import Categoria, Producto, ProductoImagen


CARPETA_DEFAULT = os.path.join(os.path.dirname(settings.BASE_DIR), 'Catalogoso')

# category name → (orden, descripcion)
CATEGORIAS_META = {
    'Hogar': (1, 'Artículos esenciales para el hogar: limpieza, organización y confort.'),
    'Cocina': (2, 'Utensilios y electrodomésticos para facilitar la preparación de alimentos.'),
    'Ventiladores': (3, 'Ventiladores de diferentes capacidades para ambientes frescos y confortables.'),
    'Armarios': (4, 'Armarios y organizadores de ropa para toda la familia.'),
    'Belleza': (5, 'Herramientas y equipos de belleza profesionales para el cuidado personal.'),
    'Ejercicio': (6, 'Equipos y accesorios para el ejercicio físico y el bienestar en casa.'),
    'Mascotas': (7, 'Accesorios y productos esenciales para el cuidado de tus mascotas.'),
    'Mosquitos': (8, 'Soluciones eficaces para el control de mosquitos en el hogar.'),
    'Termos': (9, 'Termos y recipientes térmicos de alta calidad para tus bebidas.'),
    'Licuadora': (10, 'Licuadoras portátiles y de alta potencia para bebidas y alimentos.'),
    'Picatodo': (11, 'Picatodos manuales y eléctricos para facilitar la preparación de alimentos.'),
    'Rallador': (12, 'Ralladores multiusos en diferentes presentaciones para la cocina.'),
    'Machacador': (13, 'Machacadores y trituradores para uso culinario diario.'),
    'Recipiente Plastico': (14, 'Recipientes plásticos herméticos para almacenar alimentos.'),
    'Relojes': (15, 'Relojes inteligentes y clásicos con funciones avanzadas.'),
    'Tecnología': (16, 'Gadgets, cámaras, comunicación y electrónica avanzada.'),
    'Herramientas': (17, 'Herramientas eléctricas y manuales para el hogar y el trabajo.'),
    'Juguetes': (18, 'Juguetes y juegos para niños y jóvenes.'),
    'Bebé': (19, 'Accesorios y productos esenciales para bebés.'),
}

# filename → (product_name, category_name)
# Images of the same product share identical product_name + category_name
IMAGEN_MAP = {
    # ── COCINA ──────────────────────────────────────────────────────────────
    'IMG-20260517-WA0076.jpg': ('Máquina de Crispetas Eléctrica', 'Cocina'),
    'IMG-20260517-WA0082.jpg': ('Batidora Sokany 400W', 'Cocina'),
    'IMG-20260517-WA0140.jpg': ('Batidora Sokany 400W', 'Cocina'),
    'IMG-20260517-WA0083.jpg': ('Olla de Vidrio Tapa Osito', 'Cocina'),
    'IMG-20260517-WA0153.jpg': ('Olla de Vidrio Tapa Osito', 'Cocina'),
    'IMG-20260517-WA0089.jpg': ('Parrilla Eléctrica Sokany Grill Maker SK-223', 'Cocina'),
    'IMG-20260517-WA0173.jpg': ('Parrilla Eléctrica Sokany Grill Maker SK-223', 'Cocina'),
    'WhatsApp Image 2026-05-17 at 2.52.57 PM.jpeg': ('Parrilla Eléctrica Sokany Grill Maker SK-223', 'Cocina'),
    'IMG-20260517-WA0113.jpg': ('Estufa Doble a Gas Sokany', 'Cocina'),
    'IMG-20260517-WA0172.jpg': ('Estufa de Gas Portátil Sokany SK-07005', 'Cocina'),
    'IMG-20260517-WA0123.jpg': ('Máquina de Hielo Portátil', 'Cocina'),
    'IMG-20260517-WA0135.jpg': ('Sellador al Vacío de Alimentos', 'Cocina'),
    'IMG-20260517-WA0146.jpg': ('Hervidora de Huevos Eléctrica', 'Cocina'),
    'IMG-20260517-WA0147.jpg': ('Hervidora de Huevos Eléctrica', 'Cocina'),
    'IMG-20260517-WA0151.jpg': ('Tabla de Corte en Acero Inoxidable', 'Cocina'),
    'IMG-20260517-WA0162.jpg': ('Donut Maker Eléctrico', 'Cocina'),
    'IMG-20260517-WA0163.jpg': ('Exprimidor de Cítricos USB Recargable', 'Cocina'),
    'IMG-20260517-WA0165.jpg': ('Crepera Eléctrica Antiadherente', 'Cocina'),
    'IMG-20260517-WA0171.jpg': ('Extractor de Jugos Sokany 800W', 'Cocina'),

    # ── TECNOLOGÍA ──────────────────────────────────────────────────────────
    'IMG-20260517-WA0079.jpg': ('Gafas con Cámara HD', 'Tecnología'),
    'IMG-20260517-WA0084.jpg': ('Mini Cámara WiFi A9', 'Tecnología'),
    'IMG-20260517-WA0085.jpg': ('Lentes G58 con Audio Bluetooth', 'Tecnología'),
    'IMG-20260517-WA0141.jpg': ('Lentes G58 con Audio Bluetooth', 'Tecnología'),
    'IMG-20260517-WA0087.jpg': ('Gafas Inteligentes AI AiMB-S1', 'Tecnología'),
    'IMG-20260517-WA0132.jpg': ('Cámara de Seguridad Tipo Bombillo', 'Tecnología'),
    'IMG-20260517-WA0136.jpg': ('Radio Baofeng BF-888S', 'Tecnología'),
    'IMG-20260517-WA0137.jpg': ('Radio Baofeng BF-888S', 'Tecnología'),
    'IMG-20260517-WA0152.jpg': ('Megáfono de Alto Alcance', 'Tecnología'),
    'IMG-20260517-WA0167.jpg': ('Auricular Inalámbrico para Moto Bluetooth', 'Tecnología'),
    'IMG-20260517-WA0169.jpg': ('Cámara de Seguridad Solar Smart Home', 'Tecnología'),
    'IMG-20260517-WA0170.jpg': ('Candado Disc Lock con Alarma para Moto', 'Tecnología'),

    # ── BELLEZA ─────────────────────────────────────────────────────────────
    'IMG-20260517-WA0081.jpg': ('Kit de Higiene Dental Eléctrico', 'Belleza'),
    'IMG-20260517-WA0088.jpg': ('Cortadora de Cabello Profesional', 'Belleza'),
    'IMG-20260517-WA0115.jpg': ('DermaWand Pro Rejuvenecedor Facial', 'Belleza'),
    'IMG-20260517-WA0118.jpg': ('Máquina de Alta Frecuencia ZL-006A', 'Belleza'),
    'IMG-20260517-WA0120.jpg': ('Alstow NS-308 Rizador Alisador 3 en 1', 'Belleza'),
    'IMG-20260517-WA0131.jpg': ('Geemy GM-3074 Estilizador 4 en 1', 'Belleza'),
    'IMG-20260517-WA0134.jpg': ('Cortadora Recargable Kemei', 'Belleza'),

    # ── EJERCICIO ───────────────────────────────────────────────────────────
    'IMG-20260517-WA0090.jpg': ('Almohada Masajeadora Car & Home', 'Ejercicio'),
    'IMG-20260517-WA0091.jpg': ('Chaleco Corrector de Postura', 'Ejercicio'),
    'IMG-20260517-WA0092.jpg': ('Cinturón Waist Training Neopreno', 'Ejercicio'),
    'IMG-20260517-WA0095.jpg': ('Toalla de Enfriamiento Deportiva', 'Ejercicio'),
    'IMG-20260517-WA0097.jpg': ('Báscula Inteligente 180kg Bluetooth', 'Ejercicio'),
    'IMG-20260517-WA0125.jpg': ('Báscula Inteligente 180kg Bluetooth', 'Ejercicio'),
    'IMG-20260517-WA0104.jpg': ('Entrenador de Suelo Pélvico', 'Ejercicio'),
    'IMG-20260517-WA0105.jpg': ('Banda Deportiva para Cabeza', 'Ejercicio'),
    'IMG-20260517-WA0108.jpg': ('Pedal Exerciser Portátil', 'Ejercicio'),
    'IMG-20260517-WA0110.jpg': ('Almohada de Viaje Cuello U', 'Ejercicio'),
    'IMG-20260517-WA0111.jpg': ('Gorro para Migrañas y Tensión', 'Ejercicio'),
    'IMG-20260517-WA0129.jpg': ('Faja Unisex Hot Shapers', 'Ejercicio'),
    'IMG-20260517-WA0142.jpg': ('Masajeador de Cabeza Eléctrico', 'Ejercicio'),
    'IMG-20260517-WA0143.jpg': ('Cojín Ergonómico para Caderas', 'Ejercicio'),
    'IMG-20260517-WA0148.jpg': ('Set de Bandas de Resistencia', 'Ejercicio'),
    'IMG-20260517-WA0149.jpg': ('Set de Bandas de Resistencia', 'Ejercicio'),
    'IMG-20260517-WA0150.jpg': ('Set de Bandas de Resistencia', 'Ejercicio'),
    'IMG-20260517-WA0156.jpg': ('Rueda Abdominal con Rebote Automático', 'Ejercicio'),

    # ── MASCOTAS ────────────────────────────────────────────────────────────
    'IMG-20260517-WA0096.jpg': ('Correa Doble LED para Mascotas', 'Mascotas'),
    'IMG-20260517-WA0119.jpg': ('Cepillo Spray para Mascotas', 'Mascotas'),
    'IMG-20260517-WA0126.jpg': ('Funda Protectora de Sofá para Mascotas', 'Mascotas'),
    'IMG-20260517-WA0133.jpg': ('Comedero Doble con Temporizador', 'Mascotas'),

    # ── HOGAR ───────────────────────────────────────────────────────────────
    'IMG-20260517-WA0077.jpg': ('Porta Llaves LED para Auto', 'Hogar'),
    'IMG-20260517-WA0078.jpg': ('Inflador de Neumáticos Portátil', 'Hogar'),
    'IMG-20260517-WA0086.jpg': ('Bomba de Globos Manual', 'Hogar'),
    'IMG-20260517-WA0093.jpg': ('Toalla Magnética Multiusos', 'Hogar'),
    'IMG-20260517-WA0094.jpg': ('Martillo con Base Magnética', 'Hogar'),
    'IMG-20260517-WA0100.jpg': ('Pistola de Agua Extensible', 'Hogar'),
    'IMG-20260517-WA0101.jpg': ('Esquinero Organizador de Baño', 'Hogar'),
    'IMG-20260517-WA0102.jpg': ('Esquinero Organizador de Baño', 'Hogar'),
    'IMG-20260517-WA0103.jpg': ('Cepillo UV Esterilizador para Botellas', 'Hogar'),
    'IMG-20260517-WA0109.jpg': ('Pilas Recargables AA', 'Hogar'),
    'IMG-20260517-WA0117.jpg': ('Cesta Plegable para Ropa Sucia', 'Hogar'),
    'IMG-20260517-WA0127.jpg': ('Cesta Plegable para Ropa Sucia', 'Hogar'),
    'IMG-20260517-WA0128.jpg': ('Zapatero Organizador 4 Niveles', 'Hogar'),
    'IMG-20260517-WA0130.jpg': ('Soporte UV Cepillos Dientes Solar', 'Hogar'),
    'IMG-20260517-WA0138.jpg': ('Secador de Zapatos Eléctrico', 'Hogar'),
    'IMG-20260517-WA0139.jpg': ('Dispensador Cepillo Dental con Pasta', 'Hogar'),
    'IMG-20260517-WA0144.jpg': ('Ducha Portátil Recargable Outdoor', 'Hogar'),
    'IMG-20260517-WA0154.jpg': ('Secadora Eléctrica Portátil de Ropa', 'Hogar'),
    'IMG-20260517-WA0155.jpg': ('Inflador Eléctrico de Globos', 'Hogar'),
    'IMG-20260517-WA0157.jpg': ('Set de Limpieza para Vehículos', 'Hogar'),
    'IMG-20260517-WA0164.jpg': ('Kit de Limpieza para Zapatos', 'Hogar'),
    'IMG-20260517-WA0166.jpg': ('Bolsa de Lavado para Zapatos', 'Hogar'),

    # ── HERRAMIENTAS ────────────────────────────────────────────────────────
    'IMG-20260517-WA0098.jpg': ('Taladro Inalámbrico Boashi 21V', 'Herramientas'),
    'IMG-20260517-WA0099.jpg': ('Pulidora Inalámbrica 12V', 'Herramientas'),
    'IMG-20260517-WA0112.jpg': ('Taladro Inalámbrico Boashi 24V', 'Herramientas'),
    'IMG-20260517-WA0116.jpg': ('Set de Destornilladores de Precisión', 'Herramientas'),
    'IMG-20260517-WA0145.jpg': ('Arrancador Portátil para Vehículos', 'Herramientas'),
    'IMG-20260517-WA0158.jpg': ('Pulidor Inalámbrico Compacto para Auto', 'Herramientas'),
    'IMG-20260517-WA0159.jpg': ('Pulidor Inalámbrico Compacto para Auto', 'Herramientas'),
    'IMG-20260517-WA0160.jpg': ('Kit Taladro Inalámbrico con Maletín', 'Herramientas'),
    'IMG-20260517-WA0161.jpg': ('Pistola Eléctrica para Pintar', 'Herramientas'),

    # ── JUGUETES ────────────────────────────────────────────────────────────
    'IMG-20260517-WA0080.jpg': ('Spray Pen Artístico para Niños', 'Juguetes'),
    'IMG-20260517-WA0107.jpg': ('Game Box Consola Portátil', 'Juguetes'),
    'IMG-20260517-WA0121.jpg': ('Walkie-Talkies para Niños', 'Juguetes'),
    'IMG-20260517-WA0122.jpg': ('Walkie-Talkies para Niños', 'Juguetes'),

    # ── TERMOS ──────────────────────────────────────────────────────────────
    'IMG-20260517-WA0106.jpg': ('Smart Cup Termo con Display LED', 'Termos'),
    'IMG-20260517-WA0168.jpg': ('Set Termo Premium Vacuum Flask con Tazas', 'Termos'),

    # ── BEBÉ ────────────────────────────────────────────────────────────────
    'IMG-20260517-WA0114.jpg': ('Extractor de Leche Eléctrico MZ-608T', 'Bebé'),

    # WA0124 is intentionally omitted — it is the company's bank account card, not a product
}


def imagen_a_base64(ruta: str) -> str:
    ext = os.path.splitext(ruta)[1].lower()
    mime = 'image/jpeg' if ext in ('.jpg', '.jpeg') else 'image/png'
    with open(ruta, 'rb') as f:
        datos = base64.b64encode(f.read()).decode('utf-8')
    return f'data:{mime};base64,{datos}'


class Command(BaseCommand):
    help = 'Carga imágenes de la carpeta Catalogoso como ProductoImagen en la BD'

    def add_arguments(self, parser):
        parser.add_argument(
            '--carpeta',
            type=str,
            default=CARPETA_DEFAULT,
            help='Ruta a la carpeta con las imágenes (default: Catalogoso junto a BASE_DIR)',
        )
        parser.add_argument(
            '--limpiar',
            action='store_true',
            help='Elimina los ProductoImagen existentes de estos productos antes de cargar',
        )

    def handle(self, *args, **options):
        carpeta = options['carpeta']
        if not os.path.isdir(carpeta):
            raise CommandError(f'Carpeta no encontrada: {carpeta}')

        # Ensure all categories exist
        cats = {}
        for nombre, (orden, desc) in CATEGORIAS_META.items():
            cat, creada = Categoria.objects.get_or_create(
                nombre=nombre,
                defaults={'orden': orden, 'descripcion': desc},
            )
            cats[nombre] = cat
            if creada:
                self.stdout.write(f'  Nueva categoría: {nombre}')

        # Group filenames by (product_name, category_name) to assign orden
        from collections import defaultdict
        grupos: dict[tuple, list[str]] = defaultdict(list)
        for filename, key in IMAGEN_MAP.items():
            grupos[key].append(filename)

        if options['limpiar']:
            self.stdout.write(self.style.WARNING('Eliminando imágenes existentes de estos productos...'))

        prod_creados = 0
        img_creadas = 0
        img_omitidas = 0

        for (prod_nombre, cat_nombre), filenames in grupos.items():
            cat = cats[cat_nombre]
            prod, creado = Producto.objects.get_or_create(
                nombre=prod_nombre,
                categoria=cat,
                defaults={'disponible': True, 'destacado': False},
            )
            if creado:
                prod_creados += 1

            if options['limpiar']:
                prod.imagenes.all().delete()

            for orden, filename in enumerate(filenames):
                ruta = os.path.join(carpeta, filename)
                if not os.path.exists(ruta):
                    self.stdout.write(self.style.WARNING(f'  Archivo no encontrado: {filename}'))
                    img_omitidas += 1
                    continue

                # Skip if this exact file was already loaded (idempotency via orden)
                if prod.imagenes.filter(orden=orden).exists():
                    img_omitidas += 1
                    continue

                try:
                    imagen_data = imagen_a_base64(ruta)
                except Exception as exc:
                    self.stdout.write(self.style.ERROR(f'  Error leyendo {filename}: {exc}'))
                    img_omitidas += 1
                    continue

                ProductoImagen.objects.create(
                    producto=prod,
                    imagen_data=imagen_data,
                    orden=orden,
                )
                img_creadas += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nCarga completa:'
            f'\n  Productos creados  : {prod_creados}'
            f'\n  Imágenes cargadas  : {img_creadas}'
            f'\n  Omitidas/existentes: {img_omitidas}'
        ))
