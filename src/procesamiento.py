import pandas as pd


def construir_universo_analitico(df):
    """
    Construye el universo analítico a nivel de procedimiento sancionatorio.

    Un mismo ProcesoSancionId puede aparecer en varias filas (una por unidad
    fiscalizable) con la misma multa. Agrupar por procedimiento evita contar
    esa multa más de una vez (ver docs/unidad_analisis.md).
    """
    multas_por_proceso = df.groupby("ProcesoSancionId")["MultaTotalUTA"].nunique()
    if (multas_por_proceso > 1).any():
        raise ValueError("Hay procedimientos con más de un valor de MultaTotalUTA")

    universo = (
        df.groupby("ProcesoSancionId")
        .agg(
            cantidad_unidades=("UnidadFiscalizableId", "nunique"),
            multa_total=("MultaTotalUTA", "first")
        )
        .reset_index()
    )

    return universo


def calcular_duracion_proceso(df):
    """
    Calcula duración del procedimiento en días.
    """

    datos = df.copy()

    datos["FechaInicio"] = pd.to_datetime(datos["FechaInicio"])
    datos["FechaTermino"] = pd.to_datetime(datos["FechaTermino"])

    datos["DuracionDias"] = (
        datos["FechaTermino"] -
        datos["FechaInicio"]
    ).dt.days

    return datos
