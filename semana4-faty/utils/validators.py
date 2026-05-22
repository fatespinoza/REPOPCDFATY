def validar_precio(precio):

    if precio <= 0:
        raise ValueError("Precio invalido")


def validar_stock(stock):

    if stock < 0:
        raise ValueError("Stock invalido")


def validar_campos(datos):

    if len(datos) != 6:
        raise ValueError("Numero incorrecto de columnas")