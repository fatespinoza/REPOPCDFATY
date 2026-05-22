# Reto 5 - Perfilador de Datasets

## Descripción

Este proyecto analiza datasets CSV y genera un perfil automático de calidad de datos.

El programa detecta:

- tipos de datos
- valores nulos
- porcentaje de nulos
- valores únicos
- porcentaje de unicidad

---

## Instalación

Crear ambiente virtual:

```bash
python -m venv .venv
```

Activar ambiente virtual:

### Windows

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

```bash
python main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

---

## Ejemplo de salida

```csv
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
```

---

## Autor

Fátima Espi