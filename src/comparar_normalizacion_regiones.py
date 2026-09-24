"""
Caso A de la Fase 3: comparación de dos estrategias para normalizar RegionNombre.

Ejecutar desde la raíz del repositorio:

    python src/comparar_normalizacion_regiones.py

Pasos:
1. Reconstruye el universo analítico de la Fase 2 desde data/raw (984
   registros "Terminado - Sanción" con multa informada), conservando las
   escrituras originales de RegionNombre.
2. Aplica la estrategia iterativa y la vectorizada.
3. Comprueba con assert que ambas entregan el mismo resultado y que ese
   resultado coincide con la columna del CSV procesado en la Fase 2.
4. Mide tiempo (mínimo de varias repeticiones) y memoria (pico con
   tracemalloc) sobre tamaños crecientes, replicando el conjunto con pd.concat.
"""

import time
import tracemalloc
from pathlib import Path

import pandas as pd

from normalizacion_regiones import (
    normalizar_regiones_iterativa,
    normalizar_regiones_vectorizada,
)


RUTA_RAW = Path("data/raw/Sancionatorios.xlsx")
RUTA_PROCESADO = Path("data/processed/sancionatorios_procesados.csv")

ESTADO_SANCION = "Terminado - Sanción"
FACTORES = (1, 4, 16)   # 984, 3.936 y 15.744 registros
REPETICIONES = 5


def cargar_regiones_originales():
    """Devuelve RegionNombre del universo analítico, sin normalizar."""
    datos = pd.read_excel(RUTA_RAW)
    filtro = (
        (datos["ProcesoSancionEstado"] == ESTADO_SANCION)
        & datos["MultaTotalUTA"].notna()
    )
    return datos.loc[filtro, "RegionNombre"].reset_index(drop=True)


def medir_tiempo(funcion, serie, repeticiones=REPETICIONES):
    """Devuelve el tiempo mínimo en milisegundos de varias ejecuciones."""
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(serie)
        tiempos.append(time.perf_counter() - inicio)
    return min(tiempos) * 1000


def medir_memoria(funcion, serie):
    """Devuelve el pico de memoria asignada durante la ejecución, en KiB."""
    tracemalloc.start()
    try:
        funcion(serie)
        _, pico = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return pico / 1024


def main():
    regiones = cargar_regiones_originales()

    print("=" * 64)
    print("CASO A - Normalización de RegionNombre")
    print("=" * 64)
    print(f"Registros del universo analítico : {len(regiones)}")
    print(f"Valores distintos antes          : {regiones.nunique()}")

    iterativa = normalizar_regiones_iterativa(regiones)
    vectorizada = normalizar_regiones_vectorizada(regiones)
    print(f"Valores distintos después        : {vectorizada.nunique()}")

    # 1. Ambas estrategias entregan exactamente el mismo resultado.
    pd.testing.assert_series_equal(iterativa, vectorizada)
    print("assert iterativa == vectorizada  : OK")

    # 2. El resultado coincide con la columna procesada en la Fase 2.
    procesado = pd.read_csv(RUTA_PROCESADO)["RegionNombre"].astype("object")
    assert vectorizada.tolist() == procesado.tolist(), (
        "La normalización no coincide con el CSV procesado de la Fase 2"
    )
    print("assert resultado == CSV Fase 2   : OK")

    # 3. Medición de tiempo y memoria sobre tamaños crecientes.
    filas = []
    for factor in FACTORES:
        serie = pd.concat([regiones] * factor, ignore_index=True)
        t_iter = medir_tiempo(normalizar_regiones_iterativa, serie)
        t_vect = medir_tiempo(normalizar_regiones_vectorizada, serie)
        m_iter = medir_memoria(normalizar_regiones_iterativa, serie)
        m_vect = medir_memoria(normalizar_regiones_vectorizada, serie)
        filas.append({
            "n": len(serie),
            "iterativa_ms": round(t_iter, 2),
            "vectorizada_ms": round(t_vect, 2),
            "razon_tiempo": round(t_iter / t_vect, 2),
            "iterativa_KiB": round(m_iter, 1),
            "vectorizada_KiB": round(m_vect, 1),
        })

    resultados = pd.DataFrame(filas)
    print()
    print(f"Tiempo = mínimo de {REPETICIONES} repeticiones; "
          "memoria = pico con tracemalloc")
    print(resultados.to_string(index=False))
    print()
    print("razon_tiempo > 1 significa que la vectorizada es más rápida.")


if __name__ == "__main__":
    main()
