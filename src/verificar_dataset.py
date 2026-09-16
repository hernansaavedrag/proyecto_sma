from pathlib import Path

import pandas as pd

from validaciones import (
    validar_ids_no_nulos,
    validar_latitudes,
    validar_longitudes,
    validar_multas_no_negativas,
)


RUTA_DATOS = Path("data/processed/sancionatorios_procesados.csv")


def main():
    """Ejecuta controles básicos sobre el dataset procesado."""
    datos = pd.read_csv(RUTA_DATOS)

    controles = {
        "IDs no nulos": validar_ids_no_nulos(datos),
        "Multas no negativas": validar_multas_no_negativas(datos),
        "Latitudes válidas": validar_latitudes(datos),
        "Longitudes válidas": validar_longitudes(datos),
    }

    for nombre, resultado in controles.items():
        estado = "OK" if resultado else "REVISAR"
        print(f"{nombre}: {estado}")


if __name__ == "__main__":
    main()

