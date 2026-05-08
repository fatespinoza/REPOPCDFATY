# =========================================
# ESTADÍSTICAS
# =========================================


class DatasetStatistics:

    def __init__(self, dataframe):

        self.df = dataframe

    # =====================================
    # RESUMEN ESTADÍSTICO
    # =====================================

    def resumen_estadistico(self):

        return self.df.describe()

    # =====================================
    # PROMEDIOS
    # =====================================

    def promedios(self):

        return self.df.mean(numeric_only=True)

    # =====================================
    # MÍNIMOS
    # =====================================

    def minimos(self):

        return self.df.min(numeric_only=True)

    # =====================================
    # MÁXIMOS
    # =====================================

    def maximos(self):

        return self.df.max(numeric_only=True)