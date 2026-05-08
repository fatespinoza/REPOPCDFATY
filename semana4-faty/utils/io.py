# =========================================
# MANEJO DE ARCHIVOS CSV
# =========================================

import csv


# =========================================
# Leer inventario desde CSV
# =========================================


def leer_inventario(ruta_archivo):

    productos = []

    # Abrimos el archivo
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:

        lector = csv.reader(archivo)
        # Saltamos el encabezado
        next(lector, None)
        # Recorremos cada fila
        for fila in lector:

            productos.append(fila)

    return productos


# =========================================
# Generar reporte txt
# =========================================


def generar_reporte(ruta_archivo, productos,
                     productos_reorden, valor_total):

    with open(ruta_archivo, mode="w", encoding="utf-8") as archivo:

        archivo.write("=== REPORTE DE INVENTARIO ===\n\n")

        archivo.write("PRODUCTOS:\n\n")
        
        # Mostrar todos los productos
        for producto in productos:

            archivo.write(str(producto) + "\n")

        archivo.write("\n")

        archivo.write("=== PRODUCTOS CON STOCK BAJO ===\n\n")

        # Mostrar productos con stock bajo
        for producto in productos_reorden:

            archivo.write(
                f"{producto.nombre} -> "
                f"Faltan {producto.unidades_faltantes()} unidades\n"
            )

        archivo.write("\n")

        archivo.write(f"VALOR TOTAL INVENTARIO: ${valor_total}\n")