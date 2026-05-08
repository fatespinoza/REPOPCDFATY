# =========================================
# VALIDADORES
# =========================================

# Verifica que el SKU no este vacio

def validar_sku(sku):

    return bool(sku.strip())


# Verifica que el nombre no este vacio

def validar_nombre(nombre):

    return bool(nombre.strip())


# Verifica que el precio sea valido (numerico y no negativo)

def validar_precio(precio):
    try:
        valor = float(precio)
        return valor >= 0
    except (ValueError, TypeError):
        return False


# Verifica que el stock sea valido (entero y no negativo)

def validar_stock(stock):
    try:
        valor = int(stock)
        return valor >= 0
    except (ValueError, TypeError):
        return False


# Verifica que el stock minimo sea valido (entero y no negativo)

def validar_stock_minimo(stock_minimo):
    try:
        valor = int(stock_minimo)
        return valor >= 0
    except (ValueError, TypeError):
        return False
