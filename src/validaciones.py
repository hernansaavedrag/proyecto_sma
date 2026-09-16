"""
Funciones de validación para el proyecto SMA.
"""


def validar_multas_no_negativas(df):
    """Verifica que MultaTotalUTA no contenga valores negativos."""
    return (df["MultaTotalUTA"].dropna() >= 0).all()


def validar_ids_no_nulos(df):
    """Verifica que ProcesoSancionId no contenga valores nulos."""
    return df["ProcesoSancionId"].notna().all()


def validar_latitudes(df):
    """Verifica que las latitudes informadas estén entre -90 y 90."""
    valores = df["Latitud"].dropna()
    return valores.between(-90, 90).all()


def validar_longitudes(df):
    """Verifica que las longitudes informadas estén entre -180 y 180."""
    valores = df["Longitud"].dropna()
    return valores.between(-180, 180).all()

