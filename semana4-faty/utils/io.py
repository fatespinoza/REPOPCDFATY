from models.producto import Producto

from utils.validators import (
    validar_precio,
    validar_stock,
    validar_campos
)


def leer_inventario(ruta_archivo):

    productos = []

    from pathlib import Path

    ruta = Path(ruta_archivo)
    if not ruta.is_absolute():
        # resolver ruta relativa a la carpeta semana4-faty (dos niveles: utils -> semana4-faty)
        base = Path(__file__).parent.parent
        ruta = base / ruta_archivo

    with ruta.open("r", encoding="utf-8") as archivo:

        lineas = archivo.readlines()

        # saltar encabezado
        for linea in lineas[1:]:

            try:

                datos = linea.strip().split(",")

                validar_campos(datos)

                sku = datos[0]
                nombre = datos[1]
                categoria = datos[2]
                precio = float(datos[3])
                stock = int(datos[4])
                stock_minimo = int(datos[5])

                validar_precio(precio)
                validar_stock(stock)

                producto = Producto(
                    sku,
                    nombre,
                    categoria,
                    precio,
                    stock,
                    stock_minimo
                )

                productos.append(producto)

            except Exception as error:

                print(f"Error en linea: {linea.strip()}")
                print(f"Motivo: {error}")
                print()

    return productos


def guardar_reporte(productos, ruta_archivo):
    from pathlib import Path

    path = Path(ruta_archivo)
    if not path.is_absolute():
        base = Path(__file__).parent.parent
        path = base / ruta_archivo

    path.parent.mkdir(parents=True, exist_ok=True)

    # Filtrar solo productos que necesitan reorden (por seguridad)
    productos_reorden = [p for p in productos if p.necesita_reorden()]

    # Calcular unidades faltantes y valor de inventario
    lineas = [
        "sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario"
    ]

    # Preparar tuplas con unidades faltantes para ordenar
    filas = []

    for p in productos_reorden:
        stock_actual = int(p.stock)
        stock_minimo = int(p.stock_minimo)
        unidades_faltantes = stock_minimo - stock_actual
        valor_inventario = float(p.precio) * stock_actual

        filas.append((unidades_faltantes, p, stock_actual, stock_minimo, valor_inventario))

    # Ordenar por unidades_faltantes descendente
    filas.sort(key=lambda x: x[0], reverse=True)

    for unidades_faltantes, p, stock_actual, stock_minimo, valor_inventario in filas:
        lineas.append(
            f"{p.sku},{p.nombre},{p.categoria},{stock_actual},{stock_minimo},{unidades_faltantes},{valor_inventario:.2f}"
        )

    path.write_text("\n".join(lineas) + "\n", encoding="utf-8")