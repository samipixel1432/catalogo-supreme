# -*- coding: utf-8 -*-
"""
Lee INVENTARIO NUEVO #1.xlsx desde la raiz del proyecto
y puebla la BD con categorias y productos.

Uso:
    python manage.py cargar_inventario
    python manage.py cargar_inventario --limpiar
"""

import os
import unicodedata
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from catalogo.models import Categoria, Producto

try:
    import openpyxl
except ImportError:
    raise CommandError('Instala openpyxl: pip install openpyxl')


DESCRIPCIONES_CAT = {
    'ARMARIOS': 'Armarios y organizadores de ropa para toda la familia, en diferentes tamanos y estilos.',
    'RELOJES': 'Relojes inteligentes y clasicos con funciones avanzadas de monitoreo y conectividad.',
    'BELLEZA': 'Herramientas y equipos de belleza profesionales para el cuidado personal.',
    'HOGAR': 'Articulos esenciales para el hogar: limpieza, organizacion y confort.',
    'VENTILADORES': 'Ventiladores de diferentes capacidades para mantener ambientes frescos y confortables.',
    'EJERCICIO': 'Equipos y accesorios para el ejercicio fisico y el bienestar en casa.',
    'MOSQUITOS': 'Soluciones eficaces para el control y eliminacion de mosquitos en el hogar.',
    'TERMOS': 'Termos y recipientes termicos de alta calidad para conservar la temperatura de tus bebidas.',
    'LICUADORA': 'Licuadoras portatiles y de alta potencia para preparar bebidas y alimentos.',
    'PICATODO': 'Picatodos manuales y electricos para facilitar la preparacion de alimentos.',
    'RALLADOR': 'Ralladores multiusos en diferentes presentaciones para la cocina.',
    'MACHACADOR': 'Machacadores y trituradores para uso culinario diario.',
    'RECIPIENTE PLASTICO': 'Recipientes plasticos hermeticos para almacenar y conservar alimentos.',
    'COCINA': 'Utensilios y accesorios de cocina para facilitar la preparacion de alimentos.',
    'MASCOTAS': 'Accesorios y productos esenciales para el cuidado y bienestar de tus mascotas.',
}

DESC_CORTAS = {
    'ARMARIO': 'Armario de almacenamiento resistente, ideal para organizar ropa y accesorios.',
    'RELOJ': 'Reloj con funciones avanzadas, pantalla de alta resolucion y larga duracion de bateria.',
    'DRILL': 'Torno electrico para manicura y pedicura profesional con multiples velocidades.',
    'LAMPARA DE UNAS': 'Lampara UV/LED de curado rapido para esmaltes de gel.',
    'LAMPARA DE MOSQUITOS': 'Lampara UV atrapa mosquitos sin quimicos, segura para toda la familia.',
    'LAMPARA': 'Lampara LED de alta eficiencia para uso en el hogar.',
    'SECADOR': 'Secador de cabello de alta potencia con tecnologia de iones.',
    'PINZA': 'Herramienta de calor para estilizar y dar forma al cabello.',
    'PEINETA': 'Peineta termica para alisar y peinar el cabello con facilidad.',
    'CALLOS': 'Removedor de callosidades para un cuidado eficiente de los pies.',
    'CEPILLO FACIAL': 'Cepillo electrico facial para limpieza profunda y exfoliacion suave.',
    'CEPILLO DE ADULTO': 'Cepillo dental de adulto de alta durabilidad y suavidad.',
    'CEPILLO': 'Cepillo de alta durabilidad para limpieza efectiva en el hogar.',
    'ORAL IRRIGATOR': 'Irrigador oral electrico para una higiene dental completa.',
    'MOP': 'Mop giratorio con sistema de escurrido automatico para limpieza de pisos.',
    'LIMPIADOR': 'Kit de limpieza especial para espejos y superficies de vidrio.',
    'MOTOSIERRA': 'Motosierra electrica portatil para poda y corte de madera.',
    'HIDROLAVADORA': 'Hidrolavadora inalambrica de alta presion para limpieza exterior.',
    'ASPIRADORA': 'Aspiradora de alta potencia para limpieza profunda de espacios.',
    'PERCHERO': 'Perchero organizador de ropa de gran capacidad.',
    'CORTINAS': 'Cortinas decorativas resistentes al agua para bano.',
    'CANASTA': 'Canasta organizadora plegable en tela resistente.',
    'VENTILADOR': 'Ventilador de alto rendimiento con multiple velocidades y bajo consumo energetico.',
    'VANTILADOR': 'Ventilador de alto rendimiento con multiple velocidades y bajo consumo energetico.',
    'RUEDA': 'Rueda abdominal para ejercicios de core y fortalecimiento muscular.',
    'BANDAS': 'Set de bandas elasticas de diferentes resistencias para entrenamiento funcional.',
    'RODILLERA': 'Rodillera elastica con soporte compresivo para alivio del dolor.',
    'MASAJEADOR': 'Masajeador electrico con multiples cabezales para alivio muscular.',
    'LINTERNA': 'Linterna compacta con bateria recargable de larga duracion.',
    'RAQUETA': 'Raqueta electrica antimosquitos recargable, efectiva e higienica.',
    'TERMO': 'Termo de acero inoxidable con doble pared para mantener temperatura por horas.',
    'LICUADORA TERMO': 'Licuadora portatil con vaso termico, recargable via USB.',
    'LICUADORA': 'Licuadora de alta potencia para preparacion de bebidas y alimentos.',
    'VASO LICUADORA': 'Vaso adicional de repuesto compatible con licuadoras portatiles.',
    'PICATODO': 'Picatodo electrico multiusos para cortar y triturar alimentos en segundos.',
    'BATIDORA': 'Batidora y picatodo combo de alta potencia para uso domestico.',
    'MANUAL': 'Picatodo manual de alta resistencia, sin electricidad requerida.',
    'RALLADOR': 'Rallador multiuso en acero inoxidable con diferentes tamanos de corte.',
    'MACHACADOR': 'Machacador manual con base antideslizante para especias y alimentos.',
    'RECIPIENTE': 'Recipiente hermetico de plastico libre de BPA para conservar alimentos.',
    'CORTADOR': 'Cortador especial para crear papas fritas uniformes en segundos.',
    'SET DE CUCHARAS': 'Set de cucharas medidoras en acero inoxidable para precision en recetas.',
    'SANDWICHERA': 'Sandwichera electrica antiadherente de calentamiento rapido.',
    'TARROS ORGANIZADORES': 'Set de tarros hermeticos organizadores para despensa y cocina.',
    'FUENTE': 'Fuente electrica para chocolate fundido, perfecta para eventos.',
    'TRITURADORA': 'Maquina trituradora de hielo electrica para bebidas frias.',
    'GRAMERA': 'Bascula de precision para cocina y uso general.',
    'CEREAL': 'Dispensador hermetico para cereales y snacks secos.',
    'TARROS': 'Set de tarros hermeticos para organizar y conservar alimentos.',
    'PORTA TRAPOS': 'Organizador de trapos de cocina con soporte de pared.',
    'GRIFO': 'Grifo dosificador electrico para garrafones de agua.',
    'FILTRO': 'Sistema de filtracion de agua para consumo domestico.',
    'ESCURRIDOR': 'Escurridor de platos con bandeja recolectora de agua.',
    'BEBEDERO': 'Bebedero automatico con circulacion de agua para mascotas.',
    'TAZA LIMPIADORA': 'Taza limpiadora de patas de mascotas con cerdas suaves.',
    'MALETINES': 'Maletin transportador ventilado y comodo para mascotas pequenas.',
    'CEPILLO PARA MASCOTAS': 'Cepillo desmontable para remover pelo suelto de mascotas.',
    'CEPILLO VAPOR': 'Cepillo de vapor para limpieza y desinfeccion de superficies.',
    'DUO': 'Kit de plancha y secador de cabello en un solo set profesional.',
    'FUN': 'Termo compacto con diseno moderno para llevar bebidas a cualquier parte.',
    'STANLY': 'Termo de alta durabilidad estilo Stanley para uso outdoor.',
}

ORDEN_CATEGORIAS = {
    'HOGAR': 1,
    'COCINA': 2,
    'VENTILADORES': 3,
    'ARMARIOS': 4,
    'BELLEZA': 5,
    'EJERCICIO': 6,
    'MASCOTAS': 7,
    'MOSQUITOS': 8,
    'TERMOS': 9,
    'LICUADORA': 10,
    'PICATODO': 11,
    'RALLADOR': 12,
    'MACHACADOR': 13,
    'RECIPIENTE PLASTICO': 14,
    'RELOJES': 15,
}


def ascii_seguro(texto: str) -> str:
    """Convierte texto con caracteres latinos especiales a ASCII puro."""
    mapa = {
        193: 'A', 225: 'a',  # A/a con acento
        201: 'E', 233: 'e',  # E/e con acento
        205: 'I', 237: 'i',  # I/i con acento
        211: 'O', 243: 'o',  # O/o con acento
        218: 'U', 250: 'u',  # U/u con acento
        209: 'N', 241: 'n',  # N/n con tilde
        220: 'U', 252: 'u',  # U/u dieresis
    }
    resultado = []
    for c in texto:
        cp = ord(c)
        if cp in mapa:
            resultado.append(mapa[cp])
        else:
            normalizado = unicodedata.normalize('NFD', c)
            sin_acento = ''.join(ch for ch in normalizado if unicodedata.category(ch) != 'Mn')
            resultado.append(sin_acento if sin_acento else c)
    return ''.join(resultado)


def get_desc_corta(nombre: str) -> str:
    nombre_upper = nombre.upper()
    for clave, desc in DESC_CORTAS.items():
        if clave in nombre_upper:
            return desc
    return f'{nombre.title()} de alta calidad para uso domestico y personal.'


class Command(BaseCommand):
    help = 'Carga el inventario desde INVENTARIO NUEVO #1.xlsx a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limpiar',
            action='store_true',
            help='Elimina todos los productos y categorias antes de cargar',
        )
        parser.add_argument(
            '--archivo',
            type=str,
            default='INVENTARIO NUEVO #1.xlsx',
            help='Nombre del archivo xlsx en la raiz del proyecto',
        )

    def handle(self, *args, **options):
        ruta = os.path.join(settings.BASE_DIR, options['archivo'])
        if not os.path.exists(ruta):
            raise CommandError(f'Archivo no encontrado: {ruta}')

        if options['limpiar']:
            Producto.objects.all().delete()
            Categoria.objects.all().delete()
            self.stdout.write(self.style.WARNING('Base de datos limpiada.'))

        wb = openpyxl.load_workbook(ruta, data_only=True)
        ws = wb.active

        categoria_actual = None
        cat_creadas = 0
        prod_creados = 0
        prod_existentes = 0

        for fila in ws.iter_rows(min_row=2, values_only=True):
            col_a = fila[0]
            col_b = fila[1] if len(fila) > 1 else None

            # Fila de categoria: col_a tiene valor, col_b vacia
            if col_a and str(col_a).strip() not in ('', ' ') and col_b is None:
                nombre_raw = ascii_seguro(str(col_a).strip()).upper()
                orden = ORDEN_CATEGORIAS.get(nombre_raw, 99)
                desc = DESCRIPCIONES_CAT.get(nombre_raw, '')
                nombre_titulo = nombre_raw.title()

                cat, creada = Categoria.objects.get_or_create(
                    nombre=nombre_titulo,
                    defaults={'descripcion': desc, 'orden': orden},
                )
                categoria_actual = cat
                if creada:
                    cat_creadas += 1
                    self.stdout.write(f'  Categoria: {cat.nombre}')
                continue

            # Fila de producto
            nombre_raw = col_b or col_a
            if not nombre_raw:
                continue
            nombre_limpio = ascii_seguro(str(nombre_raw).strip())
            if len(nombre_limpio) < 3 or nombre_limpio.strip() in ('NOMBRE', ' '):
                continue

            nombre_titulo = nombre_limpio.title()

            prod, creado = Producto.objects.get_or_create(
                nombre=nombre_titulo,
                categoria=categoria_actual,
                defaults={
                    'descripcion_corta': get_desc_corta(nombre_limpio),
                    'disponible': True,
                    'destacado': False,
                },
            )
            if creado:
                prod_creados += 1
            else:
                prod_existentes += 1

        # Destacar los primeros 2 de cada categoria
        for cat in Categoria.objects.all():
            for p in cat.productos.filter(disponible=True)[:2]:
                p.destacado = True
                p.save(update_fields=['destacado'])

        self.stdout.write(self.style.SUCCESS(
            f'\nCarga completa:'
            f'\n  Categorias creadas : {cat_creadas}'
            f'\n  Productos creados  : {prod_creados}'
            f'\n  Ya existian        : {prod_existentes}'
        ))
