import sys
import re

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']

def detectar_tipo(codigo):
    """Detecta el tipo de codigo por su estructura usando regex flexible."""
    # Nota el uso de la 'r' antes de las comillas para usar "raw strings"
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$', codigo):
        return "producto"
    elif re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return "envio"
    elif re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return "empleado"
    elif re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return "factura"
    else:
        return "desconocido"

def validar_producto(codigo):
    """Valida que categoria y pais sean estrictamente mayusculas."""
    # Si hace match exacto con [A-Z] mayusculas, devuelve True
    return bool(re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$', codigo))

def validar_envio(codigo):
    """Valida rangos de fecha (año 2020-2030, mes 01-12, dia 01-31)."""
    # Usamos paréntesis para agrupar y capturar los bloques de fecha
    m = re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-\d{6}$', codigo)
    if m:
        anio = int(m.group(1)) # Extrae el primer par de paréntesis
        mes = int(m.group(2))  # Extrae el segundo par
        dia = int(m.group(3))  # Extrae el tercer par
        
        # Validamos los rangos lógicos
        if (2020 <= anio <= 2030) and (1 <= mes <= 12) and (1 <= dia <= 31):
            return True
    return False

def validar_empleado(codigo):
    """Valida departamento valido y que el numero no empiece con 0."""
    m = re.match(r'^EMP-([A-Za-z]{3})-(\d{4})$', codigo)
    if m:
        depto = m.group(1)
        numero = m.group(2)
        
        # Verificamos si el depto está en la lista y el primer dígito del número
        if depto in DEPARTAMENTOS_VALIDOS and numero[0] != '0':
            return True
    return False

def validar_factura(codigo):
    """Valida serie A-E en mayuscula."""
    # Usamos la clase de caracteres [A-E] para limitar las letras permitidas
    return bool(re.match(r'^FAC-[A-E]-\d{6}$', codigo))

def validar_codigo(codigo):
    """Detecta tipo y valida. Retorna (tipo, es_valido)."""
    tipo = detectar_tipo(codigo)
    
    if tipo == "producto":
        es_valido = validar_producto(codigo)
    elif tipo == "envio":
        es_valido = validar_envio(codigo)
    elif tipo == "empleado":
        es_valido = validar_empleado(codigo)
    elif tipo == "factura":
        es_valido = validar_factura(codigo)
    else:
        es_valido = False # Desconocido siempre es inválido
        
    return tipo, es_valido

def main():
    print("codigo,tipo,valido")
    for linea in sys.stdin:
        codigo = linea.strip() # Limpiamos espacios en blanco y saltos de línea
        if not codigo:
            continue # Ignoramos líneas vacías
            
        tipo, es_valido = validar_codigo(codigo)
        estado = "VALIDO" if es_valido else "INVALIDO"
        print(f"{codigo},{tipo},{estado}")

if __name__ == "__main__":
    main()