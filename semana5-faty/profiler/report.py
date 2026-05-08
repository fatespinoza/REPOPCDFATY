# =========================================
# GENERADOR DE REPORTES
# =========================================

from datetime import datetime


class ReportGenerator:

    def __init__(self, profiler, statistics):

        self.profiler = profiler
        self.statistics = statistics

    # =====================================
    # GENERAR REPORTE TXT
    # =====================================

    def generar_reporte(self, ruta_salida):

        with open(ruta_salida, "w", encoding="utf-8") as archivo:

            archivo.write("=== PERFILADOR DE DATASETS ===\n\n")

            archivo.write(
                f"Fecha: {datetime.now()}\n\n"
            )

            # =================================
            # INFORMACIÓN GENERAL
            # =================================

            archivo.write("=== INFORMACIÓN GENERAL ===\n\n")

            archivo.write(
                f"Filas: {self.profiler.total_filas()}\n"
            )

            archivo.write(
                f"Columnas: {self.profiler.total_columnas()}\n"
            )

            archivo.write(
                f"Duplicados: {self.profiler.duplicados()}\n\n"
            )

            # =================================
            # COLUMNAS
            # =================================

            archivo.write("=== COLUMNAS ===\n\n")

            for columna in self.profiler.nombres_columnas():

                archivo.write(f"- {columna}\n")

            archivo.write("\n")

            # =================================
            # TIPOS DE DATOS
            # =================================

            archivo.write("=== TIPOS DE DATOS ===\n\n")

            archivo.write(
                str(self.profiler.tipos_datos())
            )

            archivo.write("\n\n")

            # =================================
            # VALORES NULOS
            # =================================

            archivo.write("=== VALORES NULOS ===\n\n")

            archivo.write(
                str(self.profiler.valores_nulos())
            )

            archivo.write("\n\n")

            # =================================
            # ESTADÍSTICAS
            # =================================

            archivo.write("=== RESUMEN ESTADÍSTICO ===\n\n")

            archivo.write(
                str(
                    self.statistics.resumen_estadistico()
                )
            )

            archivo.write("\n")