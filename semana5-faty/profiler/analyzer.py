# =========================================
# ANALIZADOR DE DATASETS
# =========================================

import pandas as pd


class DatasetProfiler:

    def __init__(self, ruta_archivo):

        # Guardamos ruta
        self.ruta_archivo = ruta_archivo

        # Leemos CSV con pandas
        self.df = pd.read_csv(ruta_archivo)

    # =====================================
    # TOTAL FILAS
    # =====================================

    def total_filas(self):

        return len(self.df)

    # =====================================
    # TOTAL COLUMNAS
    # =====================================

    def total_columnas(self):

        return len(self.df.columns)

    # =====================================
    # NOMBRES COLUMNAS
    # =====================================

    def nombres_columnas(self):

        return list(self.df.columns)

    # =====================================
    # TIPOS DE DATOS
    # =====================================

    def tipos_datos(self):

        return self.df.dtypes

    # =====================================
    # VALORES NULOS
    # =====================================

    def valores_nulos(self):

        return self.df.isnull().sum()

    # =====================================
    # DUPLICADOS
    # =====================================

    def duplicados(self):

        return self.df.duplicated().sum()

    # =====================================
    # INFORMACIÓN GENERAL
    # =====================================

    def informacion_general(self):

        return {
            "filas": self.total_filas(),
            "columnas": self.total_columnas(),
            "duplicados": self.duplicados()
        }