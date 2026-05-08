# =========================================
# PROGRAMA PRINCIPAL
# =========================================

# =========================================
# IMPORTS VALIDADORES
# =========================================

from validators.email_validator import (
    validar_email
)

from validators.phone_validator import (
    validar_telefono
)

from validators.code_validator import (
    validar_codigo_producto
)

import os

from validators.password_validator import (
    validar_password
)

# =========================================
# IMPORT CSV
# =========================================

from utils.file_handler import (
    leer_csv
)

# =========================================
# FUNCIÓN PRINCIPAL
# =========================================


def main():

    print("=== VALIDADOR DE CÓDIGOS ===\n")

    # =====================================
    # LEER DATOS CSV
    # =====================================

    ruta_csv = "data/datos.csv"

    datos = leer_csv(ruta_csv)

    if not datos:
        print("El archivo CSV está vacío o no contiene filas.")
        return

    campos_disponibles = set(datos[0].keys())
    validar_email_presente = "email" in campos_disponibles
    validar_telefono_presente = "telefono" in campos_disponibles
    validar_codigo_presente = "codigo" in campos_disponibles
    validar_password_presente = "password" in campos_disponibles

    if not any(
        [
            validar_email_presente,
            validar_telefono_presente,
            validar_codigo_presente,
            validar_password_presente
        ]
    ):
        print(
            "Error: El CSV no contiene ninguna columna válida para validar."
            "Debe incluir al menos 'codigo' o una combinación de"
            " 'email', 'telefono', 'password'."
        )
        return

    # =====================================
    # LISTA REPORTE
    # =====================================

    reporte = []

    # =====================================
    # RECORRER FILAS
    # =====================================

    for fila in datos:

        # =================================
        # OBTENER DATOS
        # =================================

        email = fila.get("email")
        telefono = fila.get("telefono")
        codigo = fila.get("codigo")
        password = fila.get("password")

        if validar_email_presente and email is not None:
            resultado_email = validar_email(email)
            mensaje = (
                f"EMAIL: {email} -> "
                f"{'VÁLIDO' if resultado_email else 'INVÁLIDO'}"
            )
            print(mensaje)
            reporte.append(mensaje)

        if validar_telefono_presente and telefono is not None:
            resultado_telefono = validar_telefono(telefono)
            mensaje = (
                f"TELÉFONO: {telefono} -> "
                f"{'VÁLIDO' if resultado_telefono else 'INVÁLIDO'}"
            )
            print(mensaje)
            reporte.append(mensaje)

        if validar_codigo_presente and codigo is not None:
            resultado_codigo = validar_codigo_producto(codigo)
            mensaje = (
                f"CÓDIGO: {codigo} -> "
                f"{'VÁLIDO' if resultado_codigo else 'INVÁLIDO'}"
            )
            print(mensaje)
            reporte.append(mensaje)

        if validar_password_presente and password is not None:
            resultado_password = validar_password(password)
            mensaje = (
                f"PASSWORD: {password} -> "
                f"{'VÁLIDO' if resultado_password else 'INVÁLIDO'}"
            )
            print(mensaje)
            reporte.append(mensaje)

        if not any(
            [
                validar_email_presente and email is not None,
                validar_telefono_presente and telefono is not None,
                validar_codigo_presente and codigo is not None,
                validar_password_presente and password is not None
            ]
        ):
            print("Fila sin datos válidos para validar.")

        print()

    # =====================================
    # GENERAR REPORTE TXT
    # =====================================

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/reporte_validaciones.txt",
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            "=== REPORTE VALIDACIONES ===\n\n"
        )

        for linea in reporte:

            archivo.write(linea + "\n")

    print(
        "Reporte generado correctamente"
    )


# =========================================
# EJECUCIÓN PRINCIPAL
# =========================================

if __name__ == "__main__":

    main()