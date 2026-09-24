import pandas as pd


def construir_universo_analitico(df):
    """
    Construye el universo analítico considerando unidades fiscalizables únicas.
    """
    
    universo = (
        df.groupby("UnidadFiscalizableId")
        .agg(
            cantidad_procesos=("ProcesoSancionId", "count"),
            multa_total=("MultaTotalUTA", "sum")
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
