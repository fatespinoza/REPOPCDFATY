##Elaboro: Fatima Espinoza Garcia PCD
import sys

def limpiar_valor(valor):
    valor = valor.strip()

    caracteres_validos = "0123456789.-"
    limpio = ""

    for char in valor:
        if char in caracteres_validos:
            limpio += char

    return limpio

def convertir_a_entero(texto):
    if texto == "":
        return 0
    try:
        numero = float(texto)
        return int(numero)  # TRUNCAR
    except ValueError:
        return 0

def procesar_linea(linea):
    linea = linea.strip()
    
    if linea == "":
        return 0
    
    valores = linea.split(",")
    suma = 0

    for valor in valores:
        limpio = limpiar_valor(valor)
        numero = convertir_a_entero(limpio)
        suma += numero

    return suma


def main():
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()
    
    
