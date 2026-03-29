import os
import shutil
import json

# JSON de selecciones proporcionado por el usuario
selecciones_json = {
  "INSTRUCCIONES": "⚠️ IMPORTANTE: Por favor envía este archivo por WhatsApp al 4779203776",
  "whatsapp": "4779203776",
  "nombre": "Valentina Rivera Olmedo",
  "fecha_evento": "18 de octubre de 2025",
  "fecha_exportacion": "2025-11-01T14:44:25.118Z",
  "total_fotos": 142,
  "estadisticas": {
    "ampliacion": 1,
    "impresion": 50,
    "invitacion": 0,
    "redes_sociales": 18,
    "descartada": 0,
    "sinClasificar": 77
  },
  "selecciones": [
    {"numero_foto": 1, "archivo": "images/foto_001.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 2, "archivo": "images/foto_002.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 3, "archivo": "images/foto_003.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 6, "archivo": "images/foto_006.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 12, "archivo": "images/foto_012.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 13, "archivo": "images/foto_013.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 14, "archivo": "images/foto_014.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 15, "archivo": "images/foto_015.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 16, "archivo": "images/foto_016.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 17, "archivo": "images/foto_017.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 18, "archivo": "images/foto_018.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 19, "archivo": "images/foto_019.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 20, "archivo": "images/foto_020.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 21, "archivo": "images/foto_021.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 22, "archivo": "images/foto_022.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 23, "archivo": "images/foto_023.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 24, "archivo": "images/foto_024.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 25, "archivo": "images/foto_025.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 29, "archivo": "images/foto_029.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 30, "archivo": "images/foto_030.webp", "ampliacion": False, "impresion": True, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 34, "archivo": "images/foto_034.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 38, "archivo": "images/foto_038.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 39, "archivo": "images/foto_039.webp", "ampliacion": False, "impresion": True, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 41, "archivo": "images/foto_041.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 42, "archivo": "images/foto_042.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 46, "archivo": "images/foto_046.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 47, "archivo": "images/foto_047.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 48, "archivo": "images/foto_048.webp", "ampliacion": False, "impresion": True, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 49, "archivo": "images/foto_049.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 50, "archivo": "images/foto_050.webp", "ampliacion": True, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 51, "archivo": "images/foto_051.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 52, "archivo": "images/foto_052.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 55, "archivo": "images/foto_055.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 57, "archivo": "images/foto_057.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 58, "archivo": "images/foto_058.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 59, "archivo": "images/foto_059.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 60, "archivo": "images/foto_060.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 62, "archivo": "images/foto_062.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 63, "archivo": "images/foto_063.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 65, "archivo": "images/foto_065.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 68, "archivo": "images/foto_068.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 70, "archivo": "images/foto_070.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 76, "archivo": "images/foto_076.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 77, "archivo": "images/foto_077.webp", "ampliacion": False, "impresion": False, "redes_sociales": True, "invitacion": False, "descartada": False},
    {"numero_foto": 79, "archivo": "images/foto_079.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 81, "archivo": "images/foto_081.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 82, "archivo": "images/foto_082.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 87, "archivo": "images/foto_087.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 105, "archivo": "images/foto_105.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 120, "archivo": "images/foto_120.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 121, "archivo": "images/foto_121.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 122, "archivo": "images/foto_122.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 123, "archivo": "images/foto_123.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 124, "archivo": "images/foto_124.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 125, "archivo": "images/foto_125.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 126, "archivo": "images/foto_126.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 127, "archivo": "images/foto_127.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 128, "archivo": "images/foto_128.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 129, "archivo": "images/foto_129.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 130, "archivo": "images/foto_130.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 131, "archivo": "images/foto_131.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 132, "archivo": "images/foto_132.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 135, "archivo": "images/foto_135.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 141, "archivo": "images/foto_141.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False},
    {"numero_foto": 142, "archivo": "images/foto_142.webp", "ampliacion": False, "impresion": True, "redes_sociales": False, "invitacion": False, "descartada": False}
  ]
}

# Directorios
carpeta_origen = r"F:\2025\10\18\luz\remii\descomprimidas"
carpeta_destino_base = r"F:\2025\10\18\luz\remii\clasificadas"

# Crear carpetas de destino
categorias = ["ampliacion", "impresion", "redes_sociales", "invitacion", "descartada", "sin_clasificar"]
for categoria in categorias:
    carpeta = os.path.join(carpeta_destino_base, categoria)
    os.makedirs(carpeta, exist_ok=True)
    print(f"Carpeta creada: {carpeta}")

# Crear diccionario de selecciones indexado por número de foto
selecciones_dict = {}
for sel in selecciones_json["selecciones"]:
    selecciones_dict[sel["numero_foto"]] = sel

# Procesar todas las 142 fotos
total_fotos = selecciones_json["total_fotos"]
contador = {"ampliacion": 0, "impresion": 0, "redes_sociales": 0, "invitacion": 0, "descartada": 0, "sin_clasificar": 0}

print(f"\n>> Procesando {total_fotos} fotos...\n")

for i in range(1, total_fotos + 1):
    # Nombre del archivo original
    nombre_original = f"foto7_{i:04d}.jpg"
    ruta_origen = os.path.join(carpeta_origen, nombre_original)

    # Verificar si el archivo existe
    if not os.path.exists(ruta_origen):
        print(f"[!] Advertencia: No se encontro {nombre_original}")
        continue

    # Verificar si la foto tiene clasificación
    if i in selecciones_dict:
        sel = selecciones_dict[i]

        # Determinar la(s) categoría(s) de la foto
        categorias_foto = []
        if sel["ampliacion"]:
            categorias_foto.append("ampliacion")
        if sel["impresion"]:
            categorias_foto.append("impresion")
        if sel["redes_sociales"]:
            categorias_foto.append("redes_sociales")
        if sel["invitacion"]:
            categorias_foto.append("invitacion")
        if sel["descartada"]:
            categorias_foto.append("descartada")

        # Si no tiene ninguna categoría, clasificar como sin_clasificar
        if not categorias_foto:
            categorias_foto.append("sin_clasificar")

        # Copiar la foto a cada categoría correspondiente
        for categoria in categorias_foto:
            ruta_destino = os.path.join(carpeta_destino_base, categoria, nombre_original)
            shutil.copy2(ruta_origen, ruta_destino)
            contador[categoria] += 1
            print(f"[OK] {nombre_original} -> {categoria}")
    else:
        # Foto sin clasificación
        ruta_destino = os.path.join(carpeta_destino_base, "sin_clasificar", nombre_original)
        shutil.copy2(ruta_origen, ruta_destino)
        contador["sin_clasificar"] += 1
        print(f"[ ] {nombre_original} -> sin_clasificar")

# Resumen final
print("\n" + "="*60)
print("RESUMEN DE CLASIFICACION")
print("="*60)
print(f"Total de fotos procesadas: {total_fotos}")
print(f"\nFotos por categoria:")
for categoria, cantidad in contador.items():
    print(f"  - {categoria.ljust(20)}: {cantidad:3d} fotos")
print("\n[OK] Clasificacion completada!")
print(f"Carpeta de destino: {carpeta_destino_base}")
print("="*60)
