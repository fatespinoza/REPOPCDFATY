# =========================================
# VALIDADOR DE CONTRASEÑAS
# =========================================

import re

from utils.regex_patterns import (
    PASSWORD_PATTERN
)


def validar_password(password):
    """
    Valida contraseñas seguras.
    """

    return bool(
        re.match(
            PASSWORD_PATTERN,
            password
        )
    )