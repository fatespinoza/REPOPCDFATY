# models/__init__.py
models_init = '''
"""Modelos de dominio del sistema de inventario."""
from .producto import Producto
'''

# utils/__init__.py
utils_init = '''
"""Utilidades del sistema de inventario."""
from .validators import validar_sku, validar_precio, validar_stock
from .io import leer_inventario, escribir_reporte
'''

print("=== models/__init__.py ===")
print(models_init)
print("\n=== utils/__init__.py ===")
print(utils_init)