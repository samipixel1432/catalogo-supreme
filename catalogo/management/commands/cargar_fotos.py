"""
Comando: python manage.py cargar_fotos <directorio>

Lee todas las imágenes JPEG/PNG de <directorio> (y subdirectorios),
convierte cada una a base64 y crea un Producto en la DB.

- Evita duplicados usando el nombre de archivo como 'referencia'.
- Si el producto ya existe (misma referencia), lo omite.
- Puede correrse múltiples veces (Drive, zip, etc.) sin repetir.

Uso:
  python manage.py cargar_fotos "C:/Users/PC/Downloads/fotos_supreme_temp/Fotos "
  python manage.py cargar_fotos "C:/Users/PC/Downloads/fotos_drive/" --categoria "Tenis"
"""

import base64
import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from catalogo.models import Producto, Categoria


EXTENSIONES = {'.jpg', '.jpeg', '.png', '.webp'}


class Command(BaseCommand):
    help = 'Carga imágenes de una carpeta como productos (evita duplicados)'

    def add_arguments(self, parser):
        parser.add_argument('directorio', type=str, help='Ruta a la carpeta con imágenes')
        parser.add_argument(
            '--categoria',
            type=str,
            default='',
            help='Nombre de la categoría (la crea si no existe)',
        )
        parser.add_argument(
            '--recursivo',
            action='store_true',
            default=True,
            help='Buscar imágenes en subcarpetas también',
        )

    def handle(self, *args, **options):
        directorio = Path(options['directorio'])
        nombre_categoria = options['categoria'].strip()
        recursivo = options['recursivo']

        if not directorio.exists():
            self.stderr.write(f'❌ Directorio no encontrado: {directorio}')
            return

        # Obtener o crear categoría
        categoria = None
        if nombre_categoria:
            categoria, creada = Categoria.objects.get_or_create(nombre=nombre_categoria)
            if creada:
                self.stdout.write(f'[OK] Categoria creada: {nombre_categoria}')

        # Recopilar imágenes
        patron = '**/*' if recursivo else '*'
        imagenes = [
            p for p in directorio.glob(patron)
            if p.is_file() and p.suffix.lower() in EXTENSIONES
        ]
        imagenes.sort(key=lambda p: p.name)

        total = len(imagenes)
        self.stdout.write(f'[INFO] {total} imagenes encontradas en {directorio}')

        # Referencias ya existentes en la DB
        refs_existentes = set(
            Producto.objects.filter(referencia__isnull=False)
            .exclude(referencia='')
            .values_list('referencia', flat=True)
        )
        self.stdout.write(f'[INFO] {len(refs_existentes)} referencias ya en la DB (se omitiran)')

        creados = 0
        omitidos = 0
        errores = 0

        for i, ruta in enumerate(imagenes, 1):
            referencia = ruta.stem  # nombre sin extensión, ej: "4269"

            # Verificar duplicado
            if referencia in refs_existentes:
                omitidos += 1
                if i % 50 == 0 or i == total:
                    self.stdout.write(f'  [{i}/{total}] omitidos={omitidos}', ending='\r')
                continue

            try:
                # Leer y convertir a base64
                with open(ruta, 'rb') as f:
                    datos = f.read()

                ext = ruta.suffix.lower().replace('.', '')
                if ext == 'jpg':
                    ext = 'jpeg'
                b64 = f'data:image/{ext};base64,{base64.b64encode(datos).decode()}'

                with transaction.atomic():
                    Producto.objects.create(
                        nombre=f'Producto {referencia}',
                        referencia=referencia,
                        imagen_data=b64,
                        categoria=categoria,
                        disponible=True,
                        destacado=False,
                    )

                refs_existentes.add(referencia)
                creados += 1

            except Exception as e:
                errores += 1
                self.stderr.write(f'\n  [ERROR] {ruta.name}: {e}')

            if i % 20 == 0 or i == total:
                self.stdout.write(
                    f'  [{i}/{total}] creados={creados}  omitidos={omitidos}  errores={errores}',
                    ending='\r' if i < total else '\n'
                )

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'\nListo -- creados: {creados} | omitidos: {omitidos} | errores: {errores}'
        ))
