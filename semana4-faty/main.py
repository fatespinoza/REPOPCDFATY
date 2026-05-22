from utils.io import (
    leer_inventario,
    guardar_reporte
)


def main():

    productos = leer_inventario(
        "data/entrada_facil.txt"
    )

    productos_bajos = []

    for producto in productos:

        if producto.necesita_reorden():

            productos_bajos.append(producto)

    guardar_reporte(
        productos_bajos,
        "outputs/reporte_inventario.csv"
    )

    print("Reporte generado correctamente")


if __name__ == "__main__":
    main()