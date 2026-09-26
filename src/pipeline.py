class Pipeline:
    """Ejecuta una estrategia de normalización de regiones."""

    def __init__(self, normalizador):
        self._normalizador = normalizador

    def ejecutar(self, serie):
        """Aplica el normalizador recibido a una serie."""
        return self._normalizador.normalizar(serie)