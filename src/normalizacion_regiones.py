"""
Normalización de RegionNombre (Fase 3, caso A).

En la Fase 2 se detectó que una misma región aparece escrita de más de una
forma en la fuente SMA (por ejemplo "Región de La Araucanía" y
"Región de la Araucanía"). Aquí la regla se generaliza: cada valor se reduce
a una clave comparable (sin espacios al inicio o al final y sin distinguir
mayúsculas) y esa clave se busca en la lista de las 16 regiones oficiales.

Se implementan dos estrategias que aplican exactamente la misma regla:

- normalizar_regiones_iterativa: recorre la columna con un ciclo for y
  normaliza valor por valor.
- normalizar_regiones_vectorizada: usa los métodos .str y .map de pandas
  sobre la columna completa, sin ciclos escritos en Python.

En ambas, un valor ausente se conserva como ausente y un nombre que no
corresponde a ninguna región oficial produce ValueError, para que un
error de escritura nuevo no pase inadvertido.
"""

import pandas as pd


REGIONES_OFICIALES = (
    "Región de Arica y Parinacota",
    "Región de Tarapacá",
    "Región de Antofagasta",
    "Región de Atacama",
    "Región de Coquimbo",
    "Región de Valparaíso",
    "Región Metropolitana",
    "Región del Libertador General Bernardo O'Higgins",
    "Región del Maule",
    "Región de Ñuble",
    "Región del Biobío",
    "Región de la Araucanía",
    "Región de Los Ríos",
    "Región de los Lagos",
    "Región de Aysén del General Carlos Ibáñez del Campo",
    "Región de Magallanes y la Antártica Chilena",
)


def clave_region(texto):
    """
    Reduce un nombre de región a una clave comparable.

    Elimina espacios al inicio y al final y pasa a minúsculas con
    casefold(). Dos escrituras de la misma región producen la misma clave,
    por ejemplo "Región de La Araucanía" y "Región de la Araucanía".
    """
    return str(texto).strip().casefold()


# Diccionario clave -> nombre oficial. Se construye una sola vez al importar.
OFICIAL_POR_CLAVE = {clave_region(region): region for region in REGIONES_OFICIALES}


def _validar_entrada(serie):
    """Comprueba que la entrada sea una Serie de pandas."""
    if not isinstance(serie, pd.Series):
        raise TypeError(
            f"Se esperaba una pandas.Series y se recibió {type(serie).__name__}"
        )


def normalizar_regiones_iterativa(serie):
    """
    Estrategia 1 (iterativa): normaliza la columna valor por valor.

    Recorre las n filas con un ciclo for; en cada una calcula la clave y la
    busca en el diccionario de regiones oficiales.
    Complejidad temporal O(n); memoria adicional O(n) por la lista de salida.
    """
    _validar_entrada(serie)
    resultado = []
    for valor in serie:
        if pd.isna(valor):
            resultado.append(valor)
            continue
        clave = clave_region(valor)
        if clave not in OFICIAL_POR_CLAVE:
            raise ValueError(f"Región no reconocida: {valor!r}")
        resultado.append(OFICIAL_POR_CLAVE[clave])
    return pd.Series(resultado, index=serie.index, name=serie.name, dtype="object")


def normalizar_regiones_vectorizada(serie):
    """
    Estrategia 2 (vectorizada): normaliza la columna completa con pandas.

    Aplica .str.strip() y .str.casefold() sobre toda la columna y traduce
    las claves con .map usando el mismo diccionario. No hay ciclos escritos
    en Python: el recorrido lo hace pandas internamente.
    Complejidad temporal O(n); memoria adicional O(n) por las columnas
    intermedias que genera cada operación .str.
    """
    _validar_entrada(serie)
    claves = serie.str.strip().str.casefold()
    resultado = claves.map(OFICIAL_POR_CLAVE)

    no_reconocidas = resultado.isna() & serie.notna()
    if no_reconocidas.any():
        ejemplos = serie[no_reconocidas].unique()[:5].tolist()
        raise ValueError(f"Región no reconocida: {ejemplos}")

    return resultado.astype("object").rename(serie.name)
