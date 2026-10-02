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

def construir_universo_procedimientos(df):
    """
    Construye el universo analítico a nivel de procedimiento sancionatorio.

    Cada ProcesoSancionId representa un procedimiento. Cuando un procedimiento
    aparece asociado a varias unidades fiscalizables, se consolidan los valores
    de las variables analíticas. Los valores informados se conservan cuando
    existen datos faltantes en otras filas.

    Si una variable presenta más de un valor informado para el mismo
    procedimiento, se genera un error para evitar una consolidación ambigua.
    """

    columnas_requeridas = [
        "ProcesoSancionId",
        "MultaTotalUTA",
        "CategoriaEconomicaNombre",
        "RegionNombre",
        "ProcesoSancionTipoNombre",
    ]

    faltantes = [
        columna
        for columna in columnas_requeridas
        if columna not in df.columns
    ]

    if faltantes:
        raise ValueError(
            f"Faltan columnas requeridas: {faltantes}"
        )

    columnas_analisis = [
        "MultaTotalUTA",
        "CategoriaEconomicaNombre",
        "RegionNombre",
        "ProcesoSancionTipoNombre",
    ]

    def consolidar_grupo(grupo):
        resultado = {}

        for columna in columnas_analisis:
            valores = grupo[columna].dropna().unique()

            if len(valores) > 1:
                raise ValueError(
                    f"Valores inconsistentes para ProcesoSancionId "
                    f"{grupo.name} en {columna}: {valores.tolist()}"
                )

            resultado[columna] = valores[0] if len(valores) == 1 else pd.NA

        resultado["ProcesoSancionId"] = grupo.name

        return pd.Series(resultado)

    universo = (
        df.groupby("ProcesoSancionId", sort=True)
        .apply(consolidar_grupo, include_groups=False)
        .reset_index(drop=True)
    )

    return universo