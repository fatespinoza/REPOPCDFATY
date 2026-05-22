class Producto:

    def __init__(
        self,
        sku,
        nombre,
        categoria,
        precio,
        stock,
        stock_minimo
    ):

        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)
        self.stock_minimo = int(stock_minimo)

    def necesita_reorden(self):

        return self.stock < self.stock_minimo