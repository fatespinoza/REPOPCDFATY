# =========================================
# PROGRAMA PRINCIPAL
# =========================================

# Importamos la clase Producto
from models.producto import Producto

# Importamos funciones de validación
from utils.validators import (
    validar_sku,
    validar_nombre,
    validar_precio,
    validar_stock,
    validar_stock_minimo
)

# Importamos funciones de archivos
from utils.io import (
    leer_inventario,
    generar_reporte
)
# =========================================
# Función para crear objetos Producto
# =========================================


def crear_productos(datos_csv):

    lista_productos = []

    # Recorremos datos del CSV
    for fila in datos_csv:

        # Validar que tenga exactamente 6 columnas
        if len(fila) != 6:
            print(f"Fila incompleta (columnas esperadas: 6, encontradas: {len(fila)}): {fila}")
            continue

        # Extraemos datos
        sku = fila[0]
        nombre = fila[1]
        categoria = fila[2]
        precio_str = fila[3]
        stock_str = fila[4]
        stock_minimo_str = fila[5]

        # =================================
        # VALIDACIONES
        # ================================
        if not validar_sku(sku):
            print(f"SKU inválido: {sku}")
            continue

        if not validar_nombre(nombre):
            print(f"Nombre inválido: {nombre}")
            continue

        if not validar_precio(precio_str):
            print(f"Precio inválido: {precio_str}")
            continue

        if not validar_stock(stock_str):
            print(f"Stock inválido: {stock_str}")
            continue

        if not validar_stock_minimo(stock_minimo_str):
            print(f"Stock mínimo inválido: {stock_minimo_str}")
            continue

        # Convertir a tipos correctos solo después de validar
        try:
            precio = float(precio_str)
            stock = int(stock_str)
            stock_minimo = int(stock_minimo_str)
        except ValueError:
            print(f"Error en conversión de datos para SKU {sku}")
            continue

        # ================================
        # CREAR OBJETO PRODUCTO
        # ================================

        producto = Producto(
            sku,
            nombre,
            categoria,
            precio,
            stock,
            stock_minimo
        )

        # Agregamos objeto a la lista
        lista_productos.append(producto)

    return lista_productos
# =========================================
# FUNCIÓN PRINCIPAL
# =========================================


def main():

    print("=== SISTEMA DE INVENTARIO ===\n")

    # =====================================
    # LEER CSV
    # =====================================

    datos_csv = leer_inventario("data/inventario.csv")

    # =====================================
    # CREAR OBJETOS PRODUCTO
    # =====================================

    productos = crear_productos(datos_csv)
     # =====================================
    # MOSTRAR PRODUCTOS
    # =====================================

    print("PRODUCTOS CARGADOS:\n")

    for producto in productos:

        print(producto)

    # =====================================
    # DETECTAR STOCK BAJO
    # =====================================

    productos_reorden = []

    print("\n=== PRODUCTOS CON STOCK BAJO ===\n")

    for producto in productos:

        if producto.necesita_reorden():

            productos_reorden.append(producto)
            print(
                f"{producto.nombre} -> "
                f"Faltan {producto.unidades_faltantes()} unidades"
            )

    # =====================================
    # CALCULAR VALOR TOTAL INVENTARIO
    # =====================================

    valor_total = 0

    for producto in productos:

        valor_total += producto.valor_inventario()

    print(f"\nVALOR TOTAL INVENTARIO: ${valor_total}")

    # =====================================
    # GENERAR REPORTE
    # =====================================

    generar_reporte(
        "reporte_inventario.txt",
        productos,
        productos_reorden,
        valor_total
    )

    print("\nReporte generado correctamente")


# =========================================
# Ejecutar programa
# =========================================

if __name__ == "__main__":

    main()