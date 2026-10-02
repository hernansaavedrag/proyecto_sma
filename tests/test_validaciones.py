"""
Pruebas reejecutables de validaciones del proyecto SMA.

Incluye:
- casos normales;
- casos límite;
- casos que deben generar excepciones.
"""

import pandas as pd

from src.procesamiento import construir_universo_procedimientos

from src.validaciones import (
    validar_fechas_consistentes,
    validar_ids_no_nulos,
    validar_multas_no_negativas,
)
from src.normalizacion_regiones import (
    normalizar_regiones_iterativa,
    normalizar_regiones_vectorizada,
)


def prueba_caso_normal():
    """Una entrada válida debe superar las validaciones."""

    datos = pd.DataFrame({
        "ProcesoSancionId": [1],
        "MultaTotalUTA": [10.5],
        "FechaInicio": ["2026-05-01"],
        "FechaTermino": ["2026-05-10"],
    })

    assert validar_ids_no_nulos(datos)
    assert validar_multas_no_negativas(datos)
    assert validar_fechas_consistentes(datos)

    print("OK - caso normal")


def prueba_caso_limite():
    """Una entrada mínima y válida debe ser aceptada."""

    datos = pd.DataFrame({
        "ProcesoSancionId": [1],
        "MultaTotalUTA": [0],
        "FechaInicio": ["2026-05-01"],
        "FechaTermino": ["2026-05-01"],
    })

    assert validar_ids_no_nulos(datos)
    assert validar_multas_no_negativas(datos)
    assert validar_fechas_consistentes(datos)

    print("OK - caso límite")

def prueba_consolidacion_procedimiento():
    """Un procedimiento repetido con datos consistentes debe consolidarse."""

    datos = pd.DataFrame({
        "ProcesoSancionId": [1, 1],
        "MultaTotalUTA": [4.2, 4.2],
        "CategoriaEconomicaNombre": [None, "Minería"],
        "RegionNombre": ["Región de Atacama", "Región de Atacama"],
        "ProcesoSancionTipoNombre": ["Fiscalización", "Fiscalización"],
    })

    resultado = construir_universo_procedimientos(datos)

    assert len(resultado) == 1
    assert resultado.iloc[0]["MultaTotalUTA"] == 4.2
    assert resultado.iloc[0]["CategoriaEconomicaNombre"] == "Minería"

    print("OK - consolidación de procedimiento")


def prueba_inconsistencia_procedimiento():
    """Dos valores informados diferentes deben generar ValueError."""

    datos = pd.DataFrame({
        "ProcesoSancionId": [1, 1],
        "MultaTotalUTA": [4.2, 4.2],
        "CategoriaEconomicaNombre": [
            "Minería",
            "Vivienda e Inmobiliarios",
        ],
        "RegionNombre": [
            "Región de Atacama",
            "Región de Atacama",
        ],
        "ProcesoSancionTipoNombre": [
            "Fiscalización",
            "Fiscalización",
        ],
    })

    try:
        construir_universo_procedimientos(datos)
        raise AssertionError("Se esperaba ValueError")
    except ValueError:
        print("OK - excepción por inconsistencia de procedimiento")

def prueba_fecha_invertida():
    """Una fecha de término anterior al inicio debe generar ValueError."""

    datos = pd.DataFrame({
        "FechaInicio": ["2026-05-10"],
        "FechaTermino": ["2026-05-01"],
    })

    try:
        validar_fechas_consistentes(datos)
        raise AssertionError("Se esperaba ValueError")
    except ValueError:
        print("OK - excepción por fecha invertida")


def prueba_region_no_reconocida():
    """Una región inexistente debe generar ValueError."""

    datos = pd.Series(["Región Inventada"])

    for funcion in (
        normalizar_regiones_iterativa,
        normalizar_regiones_vectorizada,
    ):
        try:
            funcion(datos)
            raise AssertionError("Se esperaba ValueError")
        except ValueError:
            pass

    print("OK - excepción por región no reconocida")


def prueba_columna_ausente():
    """La ausencia de una columna requerida debe generar KeyError."""

    datos = pd.DataFrame({
        "ProcesoSancionId": [1],
    })

    try:
        validar_multas_no_negativas(datos)
        raise AssertionError("Se esperaba KeyError")
    except KeyError:
        print("OK - excepción por columna ausente")


def main():
    """Ejecuta todas las pruebas."""

    prueba_caso_normal()
    prueba_caso_limite()
    prueba_consolidacion_procedimiento()
    prueba_inconsistencia_procedimiento()
    prueba_fecha_invertida()
    prueba_region_no_reconocida()
    prueba_columna_ausente()

    print("\nTodas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    main()
