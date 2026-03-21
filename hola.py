import sys

# Convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

# Clasificar temperatura
def clasificar(temp):
    if temp < 0:
        return "Congelante"
    elif temp <= 15:
        return "Frio"
    elif temp <= 25:
        return "Templado"
    elif temp <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    # Imprimir encabezado
    print("ciudad,temperatura_celsius,clasificacion")

    # Leer línea por línea desde stdin
    for i, linea in enumerate(sys.stdin):
        # Saltar encabezado
        if i == 0:
            continue

        linea = linea.strip()

        # Saltar líneas vacías
        if not linea:
            continue

        partes = linea.split(",")

        # Validar que tenga 3 columnas
        if len(partes) != 3:
            continue

        ciudad, temp, unidad = partes

        # Intentar convertir temperatura
        try:
            temp = float(temp)
        except:
            continue

        unidad = unidad.strip().upper()

        # Validar unidad y convertir si es necesario
        if unidad == "F":
            temp = fahrenheit_a_celsius(temp)
        elif unidad != "C":
            continue

        # Clasificar
        categoria = clasificar(temp)

        # Imprimir resultado
        print(f"{ciudad},{temp:.1f},{categoria}")

# Ejecutar programa
if __name__ == "__main__":
    main()
    