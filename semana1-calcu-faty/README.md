##ELABORO:ESPNOZA GARCIA FATIMA

# Calculadora de Sumas

Programa que procesa líneas de entrada con valores separados por comas y calcula la suma de los números válidos.

## Funcionalidades

- **limpiar_valor()**: Extrae solo los caracteres numéricos válidos (0-9, punto, guión)
- **convertir_a_entero()**: Convierte texto a número entero, truncando decimales
- **procesar_linea()**: Procesa una línea CSV y retorna la suma de valores

## Uso

```bash
echo "1,2,3" | python main.py
# Salida: 6
```

## Características

- Valida caracteres numéricos
- Maneja errores de conversión
- Trunca valores decimales
- Procesa entrada por línea

