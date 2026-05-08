# =========================================
# VALIDADOR DE CÓDIGOS
# =========================================

import re

from utils.regex_patterns import (
    PRODUCT_CODE_PATTERN
)


def validar_codigo_producto(codigo):
    """
    Valida códigos tipo:
    PROD-1234
    """

    return bool(
        re.match(
            PRODUCT_CODE_PATTERN,
            codigo
        )
    )