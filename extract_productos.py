
import os, re, json, unicodedata, openpyxl
from collections import defaultdict

BASE_DIR  = r"C:\catalogo_bodega_premier"
XLSX_PATH = os.path.join(BASE_DIR, "INVENTARIO NUEVO #1.xlsx")
IMG_DIR   = os.path.join(BASE_DIR, "static", "img", "productos")
JSON_PATH = os.path.join(BASE_DIR, "productos_import.json")

os.makedirs(IMG_DIR, exist_ok=True)

def slugify(text):
    text = text.strip().lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    text = re.sub(r"\s+", "-", text.strip())
    return re.sub(r"-+", "-", text).strip("-")

def extract_reference(name):
    m = re.search(r"\(([^)]+)\)", name)
    if m:
        return re.sub(r"\s+", "", m.group(1).strip()).upper()
    return ""

DESCRIPTIONS = {
    "ARMARIOS":     u"Armario de tela resistente, ideal para organizar ropa y accesorios. Fácil de armar y desarmar.",
    "RELOJES":      u"Reloj de pared moderno con diseño elegante. Mecanismo de cuarzo silencioso de alta precisión.",
    "BELLEZA":      u"Herramienta profesional para el cuidado del cabello y la belleza. Resultados de salón en casa.",
    "HOGAR":        u"Artículo de hogar de alta calidad para decorar y organizar tu espacio.",
    "VENTILADORES": u"Ventilador de alto rendimiento con múltiples velocidades. Silencioso y eficiente.",
    "EJERCICIO":    u"Equipo de ejercicio resistente para entrenar en casa. Diseño ergonómico y seguro.",
    "MOSQUITOS":    u"Protección efectiva contra mosquitos y plagas. Fácil instalación.",
    "TERMOS":       u"Termo de acero inoxidable que mantiene la temperatura por horas. Libre de BPA.",
    "LICUADORA":    u"Licuadora de alta potencia para preparar batidos, sopas y salsas. Fácil de limpiar.",
    "PICATODO":     u"Picatodo multifuncional para cortar frutas, verduras y más en segundos.",
    "RALLADOR":     u"Rallador multiusos de acero inoxidable. Ralla queso, zanahoria, limón y más.",
    "MACHACADOR":   u"Machacador resistente para preparar purés, guacamole y más. Mango antideslizante.",
    "RECIPIENTE":   u"Recipiente plástico hermético para almacenar alimentos frescos por más tiempo.",
    "COCINA":       u"Artículo de cocina de alta calidad para facilitar la preparación de tus comidas.",
    "MASCOTAS":     u"Accesorio para mascotas de alta durabilidad. Diseño cómodo y seguro para tu mascota.",
}

def get_description(category):
    key = category.strip().upper()
    for k, v in DESCRIPTIONS.items():
        if k in key:
            return v
    return u"Producto de alta calidad. Excelente relación calidad-precio."

print("Opening:", XLSX_PATH)
wb = openpyxl.load_workbook(XLSX_PATH)
ws = wb.active
print("Sheet:", ws.title, " Rows:", ws.max_row, " Images:", len(ws._images))

row_to_images = defaultdict(list)
for img in ws._images:
    row_to_images[img.anchor._from.row + 1].append(img)

print("Unique rows with images:", len(row_to_images))

products = []
current_cat = "SIN CATEGORIA"
images_saved = 0
no_image_rows = []

for row_num in range(1, ws.max_row + 1):
    col_producto = ws.cell(row=row_num, column=1).value
    col_nombre   = ws.cell(row=row_num, column=2).value
    producto_val = str(col_producto).strip() if col_producto else ""
    nombre_val   = str(col_nombre).strip()   if col_nombre   else ""

    if row_num == 1:
        continue

    if producto_val and producto_val.strip() and not nombre_val:
        current_cat = producto_val.strip()
        continue

    if nombre_val:
        slug         = slugify(nombre_val)
        reference    = extract_reference(nombre_val)
        img_filename = "%s-%d.jpg" % (slug, row_num)
        img_path     = os.path.join(IMG_DIR, img_filename)

        if row_to_images[row_num]:
            img_obj = row_to_images[row_num].pop(0)
            try:
                img_data = img_obj._data()
                open(img_path, "wb").write(img_data)
                images_saved += 1
            except Exception as e:
                print("  [WARN] row %d (%s): %s" % (row_num, nombre_val, e))
                img_filename = ""
        else:
            img_filename = ""
            no_image_rows.append(row_num)

        products.append({
            "category":       current_cat,
            "name":           nombre_val,
            "reference":      reference,
            "slug":           slug,
            "image_filename": img_filename,
            "description":    get_description(current_cat),
        })

leftover = sum(len(v) for v in row_to_images.values())
if leftover:
    print("[INFO] %d image(s) with no matching product row." % leftover)

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("\n=== DONE ===")
print("Products in JSON      :", len(products))
print("Images saved          :", images_saved)
print("Products without image:", len(no_image_rows), "rows:", no_image_rows)
print("JSON written to       :", JSON_PATH)
print("Images saved to       :", IMG_DIR)
print()
print("First 5 JSON entries:")
for entry in products[:5]:
    print(json.dumps(entry, ensure_ascii=False, indent=2))
