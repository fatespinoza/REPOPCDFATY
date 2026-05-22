import argparse
import pandas as pd


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================

def es_valor_nulo(valor):
    """
    Verifica si un valor se considera nulo.
    """

    if pd.isna(valor):
        return True

    if isinstance(valor, str) and valor.strip() == "":
        return True

    return False


def es_numerico(valor):
    """
    Verifica si un valor es numérico.
    """

    try:
        float(valor)
        return True
    except:
        return False


def es_fecha(valor):
    """
    Verifica si un valor puede convertirse a fecha.
    """

    try:
        pd.to_datetime(valor)
        return True
    except:
        return False


def inferir_tipo(serie):
    """
    Detecta el tipo predominante de una columna.
    """

    valores_validos = [
        valor for valor in serie
        if not es_valor_nulo(valor)
    ]

    if len(valores_validos) == 0:
        return "desconocido"

    if all(es_numerico(v) for v in valores_validos):
        return "numerico"

    if all(es_fecha(v) for v in valores_validos):
        return "fecha"

    return "texto"


# ==========================================
# PERFILAR COLUMNA
# ==========================================

def perfilar_columna(nombre_columna, serie):
    """
    Genera el perfil estadístico de una columna.
    """

    total_registros = len(serie)

    valores_nulos = serie.apply(
        es_valor_nulo
    ).sum()

    porcentaje_nulos = round(
        (valores_nulos / total_registros) * 100,
        2
    )

    valores_validos = serie[
        ~serie.apply(es_valor_nulo)
    ]

    valores_unicos = valores_validos.nunique()

    porcentaje_unicos = round(
        (valores_unicos / total_registros) * 100,
        2
    )

    ejemplo_valor = (
        str(valores_validos.iloc[0])
        if not valores_validos.empty
        else "N/A"
    )

    tipo_inferido = inferir_tipo(serie)

    return {
        "nombre_columna": nombre_columna,
        "tipo_inferido": tipo_inferido,
        "total_registros": total_registros,
        "valores_nulos": valores_nulos,
        "porcentaje_nulos": porcentaje_nulos,
        "valores_unicos": valores_unicos,
        "porcentaje_unicos": porcentaje_unicos,
        "ejemplo_valor": ejemplo_valor
    }


# ==========================================
# GENERAR PERFIL DEL DATASET
# ==========================================

def generar_perfil(input_path, output_path):
    """
    Lee el CSV y genera el perfil del dataset.
    """

    try:

        print("\nLeyendo dataset...")

        df = pd.read_csv(input_path)

        perfiles = []

        print("Analizando columnas...\n")

        for columna in df.columns:

            perfil = perfilar_columna(
                columna,
                df[columna]
            )

            perfiles.append(perfil)

            print(f"Columna procesada: {columna}")

        resultado = pd.DataFrame(perfiles)

        # Asegurar que la carpeta de salida exista
        from pathlib import Path
        out_path = Path(output_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        resultado.to_csv(
            output_path,
            index=False
        )

        print("\nPerfil generado correctamente")
        print(f"Archivo guardado en: {output_path}")

    except FileNotFoundError:
        print("ERROR: archivo no encontrado")

    except Exception as error:
        print(f"ERROR: {error}")


# ==========================================
# MAIN
# ==========================================

def main():

    parser = argparse.ArgumentParser(
        description="Perfilador de datasets CSV"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Ruta del archivo CSV de entrada"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Ruta del archivo CSV de salida"
    )

    args = parser.parse_args()

    generar_perfil(
        args.input,
        args.output
    )


# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == "__main__":
    main()
