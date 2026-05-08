# =========================================
# PATRONES REGEX
# =========================================

# Correo electrónico
EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Teléfono mexicano de 10 dígitos
PHONE_PATTERN = r"^[0-9]{10}$"

# Código de producto
# Ejemplo: PROD-1234 o EMP-ADM-2734
PRODUCT_CODE_PATTERN = r"^[A-Za-z]{3,4}(?:-[A-Za-z0-9]+)+$"

# Contraseña segura
# Mínimo:
# - 8 caracteres
# - una mayúscula
# - una minúscula
# - un número
PASSWORD_PATTERN = (
    r"^(?=.*[a-z])"
    r"(?=.*[A-Z])"
    r"(?=.*\\d)"
    r".{8,}$"
)