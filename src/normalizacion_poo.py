from abc import ABC, abstractmethod

import pandas as pd

from .normalizacion_regiones import REGIONES_OFICIALES


class NormalizadorRegion(ABC):
    """Clase base para normalizar nombres de regiones."""

    def __init__(self, regiones_oficiales=REGIONES_OFICIALES):
        self.__regiones_oficiales = tuple(regiones_oficiales)
        self.__diccionario_regiones = {
            self._clave_region(region): region
            for region in self.__regiones_oficiales
        }

    @staticmethod
    def _clave_region(texto):
        """Genera una clave comparable para un nombre de región."""
        return str(texto).strip().casefold()

    def _validar_entrada(self, serie):
        """Valida que la entrada sea una Serie de pandas."""
        if not isinstance(serie, pd.Series):
            raise TypeError(
                f"Se esperaba una pandas.Series y se recibió {type(serie).__name__}"
            )

    @property
    def diccionario_regiones(self):
        """Entrega el diccionario de regiones sin permitir modificar el interno."""
        return self.__diccionario_regiones.copy()

    @abstractmethod
    def normalizar(self, serie):
        """Normaliza los nombres de regiones."""
        pass


class NormalizadorIterativo(NormalizadorRegion):
    """Normalización mediante recorrido elemento por elemento."""

    def normalizar(self, serie):
        self._validar_entrada(serie)

        resultado = []

        for valor in serie:
            if pd.isna(valor):
                resultado.append(valor)
                continue

            clave = self._clave_region(valor)

            if clave not in self.diccionario_regiones:
                raise ValueError(
                    f"Región no reconocida: {valor!r}"
                )

            resultado.append(self.diccionario_regiones[clave])

        return pd.Series(
            resultado,
            index=serie.index,
            name=serie.name,
            dtype="object"
        )


class NormalizadorVectorizado(NormalizadorRegion):
    """Normalización mediante operaciones vectorizadas de pandas."""

    def normalizar(self, serie):
        self._validar_entrada(serie)

        claves = serie.astype("string").str.strip().str.casefold()

        resultado = claves.map(self.diccionario_regiones)

        no_reconocidas = resultado.isna() & serie.notna()

        if no_reconocidas.any():
            ejemplos = serie[no_reconocidas].unique()[:5].tolist()
            raise ValueError(
                f"Región no reconocida. Ejemplos: {ejemplos}"
            )

        return resultado.astype("object").rename(serie.name)