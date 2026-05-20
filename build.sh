#!/bin/bash
set -e

echo "=== Instalando dependencias ==="
pip install -r requirements.txt

echo "=== Aplicando migraciones ==="
python manage.py migrate --noinput

echo "=== Creando superusuario samuel1312 (si no existe) ==="
python manage.py shell -c "
from django.contrib.auth import get_user_model
U = get_user_model()
if not U.objects.filter(username='samuel1312').exists():
    U.objects.create_superuser('samuel1312', '', 'samuel1312')
    print('Superusuario creado.')
else:
    print('Superusuario ya existe.')
"

echo "=== Recolectando archivos estáticos ==="
python manage.py collectstatic --noinput

echo "=== Build completo ==="
