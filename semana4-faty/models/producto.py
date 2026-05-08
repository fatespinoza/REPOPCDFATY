# =========================================
# CLASE PRODUCTO
# =========================================

class Producto:

    # Constructor
    # Inicializa el objeto con sus atributos
    def __init__(self, sku, nombre, categoria,
                 precio, stock, stock_minimo):

        # self representa al objeto actual

        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    # =====================================
    # Método que verifica si el producto
    # necesita reorden
    # =====================================
    def necesita_reorden(self):

        return self.stock < self.stock_minimo

    # =====================================
    # Calcula cuántas unidades faltan
    # =====================================

    def unidades_faltantes(self):

        if self.necesita_reorden():

            return self.stock_minimo - self.stock

        return 0

    # =====================================
    # Calcula valor total del inventario
    # =====================================

    def valor_inventario(self):

        return self.precio * self.stock
    
    
    # =====================================
    # Método especial __str__
    # Define cómo se imprime el objeto
    # =====================================

    def __str__(self):

        return (
            f"[{self.sku}] {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.stock}"
        )