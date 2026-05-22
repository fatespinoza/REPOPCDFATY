import sys
import math
from pathlib import Path


def main():

    # Diccionario para almacenar estadísticas
    productos = {}

    primera_linea = True

    script_dir = Path(__file__).parent
    archivo_path = script_dir / "entrada_facil.txt"

    if sys.stdin.isatty():
        if not archivo_path.exists():
            print("No se encontró 'entrada_facil.txt' en la carpeta del script.")
            print("Ejecuta el programa dentro de 'semana3-faty' o crea el archivo de datos allí.")
            raise SystemExit(1)

        lineas = archivo_path.read_text(encoding="utf-8").splitlines()
    else:
        lineas = [line.rstrip("\n") for line in sys.stdin]

    for linea in lineas:

        linea = linea.strip()

        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue

        # Saltar líneas vacías
        if not linea:
            continue

        # Separar columnas
        partes = linea.split(",")

        # Validar número de columnas
        if len(partes) != 4:
            continue

        fecha = partes[0]
        producto = partes[1]

        # Convertir datos numéricos
        try:

            cantidad = float(partes[2])
            precio = float(partes[3])

            if not math.isfinite(cantidad) or not math.isfinite(precio):
                raise ValueError("valor no finito")

            if cantidad < 0 or precio < 0:
                raise ValueError("valor negativo")

            cantidad = int(cantidad)

        except (ValueError, TypeError):
            continue

        # Crear producto si no existe
        if producto not in productos:

            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        # Acumular datos
        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    # Calcular precio promedio
    for producto in productos:

        unidades = productos[producto]["unidades"]
        ingreso = productos[producto]["ingreso"]

        if unidades > 0:
            promedio = ingreso / unidades
        else:
            promedio = 0

        productos[producto]["promedio"] = promedio

    # Ordenar por ingreso descendente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    salida_path = script_dir / "salida.csv"
    lineas_salida = ["producto,unidades_vendidas,ingreso_total,precio_promedio"]

    for nombre, datos in productos_ordenados:
        lineas_salida.append(
            f"{nombre},"
            f"{datos['unidades']},"
            f"{datos['ingreso']:.2f},"
            f"{datos['promedio']:.2f}"
        )

    # Guardar CSV de salida
    salida_path.write_text("\n".join(lineas_salida) + "\n", encoding="utf-8")

    # Imprimir resultados en pantalla también
    print(f"CSV de salida guardado en: {salida_path}")
    print("\n".join(lineas_salida))

# Ejecutar programa
if __name__ == "__main__":
    main()