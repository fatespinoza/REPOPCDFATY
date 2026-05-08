# =========================================
# PROGRAMA PRINCIPAL
# =========================================

from profiler.analyzer import DatasetProfiler

from profiler.statistics import DatasetStatistics

from profiler.report import ReportGenerator

from utils.validators import (
    validar_archivo,
    validar_csv
)

# =========================================
# FUNCIÓN PRINCIPAL
# =========================================


def main():

    print("=== PERFILADOR DE DATASETS ===\n")

    ruta = "data/empleados.csv"

    # =====================================
    # VALIDACIONES
    # =====================================

    if not validar_archivo(ruta):

        print("El archivo no existe")
        return

    if not validar_csv(ruta):

        print("El archivo no es CSV")
        return

    # =====================================
    # CREAR PROFILER
    # =====================================

    profiler = DatasetProfiler(ruta)

    # =====================================
    # ESTADÍSTICAS
    # =====================================

    statistics = DatasetStatistics(
        profiler.df
    )

    # =====================================
    # MOSTRAR INFORMACIÓN
    # =====================================

    print("INFORMACIÓN GENERAL\n")

    print(
        f"Filas: {profiler.total_filas()}"
    )

    print(
        f"Columnas: {profiler.total_columnas()}"
    )

    print(
        f"Duplicados: {profiler.duplicados()}"
    )

    # =====================================
    # VALORES NULOS
    # =====================================

    print("\nVALORES NULOS\n")

    print(
        profiler.valores_nulos()
    )

    # =====================================
    # ESTADÍSTICAS
    # =====================================

    print("\nRESUMEN ESTADÍSTICO\n")

    print(
        statistics.resumen_estadistico()
    )

    # =====================================
    # GENERAR REPORTE
    # =====================================

    reporte = ReportGenerator(
        profiler,
        statistics
    )

    reporte.generar_reporte(
        "reports/reporte_dataset.txt"
    )

    print(
        "\nReporte generado correctamente"
    )


# =========================================
# EJECUCIÓN PRINCIPAL
# =========================================

if __name__ == "__main__":

    main()
