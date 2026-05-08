# =========================================
# VALIDADORES
# =========================================

from pathlib import Path


def validar_archivo(ruta):
    """
    Verifica que el archivo exista.
    """

    return Path(ruta).exists()


def validar_csv(ruta):
    """
    Verifica que el archivo sea CSV.
    """

    return ruta.endswith(".csv")