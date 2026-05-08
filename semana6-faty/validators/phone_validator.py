# =========================================
# VALIDADOR DE TELÉFONOS
# =========================================

import re

from utils.regex_patterns import (
    PHONE_PATTERN
)


def validar_telefono(telefono):
    """
    Valida teléfono de 10 dígitos.
    """

    return bool(
        re.match(PHONE_PATTERN, telefono)
    )