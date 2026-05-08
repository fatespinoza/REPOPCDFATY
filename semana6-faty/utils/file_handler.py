# =========================================
# MANEJO DE CSV
# =========================================

import csv


def leer_csv(ruta_archivo):
    """
    Lee datos desde CSV.
    """

    datos = []

    with open(
        ruta_archivo,
        mode="r",
        encoding="utf-8"
    ) as archivo:

        lector = csv.reader(archivo)
        filas = [fila for fila in lector if fila]

    if not filas:
        return []

    if len(filas[0]) == 1:
        return [{"codigo": fila[0].strip()} for fila in filas if fila[0].strip()]

    encabezados = [celda.strip() for celda in filas[0]]
    datos = []

    for fila in filas[1:]:
        if len(fila) != len(encabezados):
            continue
        datos.append({encabezados[i]: fila[i].strip() for i in range(len(encabezados))})

    return datos