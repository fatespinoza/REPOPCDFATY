# =========================================
# VALIDADOR DE EMAILS
# =========================================

import re

from utils.regex_patterns import (
    EMAIL_PATTERN
)


def validar_email(email):
    """
    Valida formato de correo electrónico.
    """

    return bool(
        re.match(EMAIL_PATTERN, email)
    )