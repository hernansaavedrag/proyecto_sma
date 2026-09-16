\# Matriz de variables para etapas posteriores



\## Criterio general



La selección de variables se realiza considerando la pregunta de análisis y distinguiendo entre variables explicativas, variables de identificación y variables destinadas principalmente a trazabilidad.



| Variable | Dimensión | Uso propuesto | Observación |

|---|---|---|---|

| MultaTotalUTA | Resultado | Variable objetivo | Magnitud de la multa expresada en UTA |

| RegionNombre | Territorial | Utilizar | Variable nominal normalizada a 16 regiones |

| ComunaNombre | Territorial | Evaluar | Mayor cardinalidad que la región |

| CategoriaEconomicaNombre | Económica | Utilizar | Permite estudiar diferencias entre sectores |

| SubCategoriaEconomicaNombre | Económica | Evaluar | Mayor nivel de detalle y cardinalidad |

| ProcesoSancionTipoNombre | Administrativa | Utilizar | Caracteriza el tipo de procedimiento |

| DuracionDias | Temporal | Utilizar | Resume la duración del procedimiento |

| ProcesoSancionId | Identificación | No utilizar directamente como predictor | Necesario para controlar la unidad de análisis |

| Expediente | Identificación | No utilizar como predictor | Permite relacionar el registro con el expediente |

| LinkSNIFA | Trazabilidad | No utilizar como predictor | Enlace hacia la fuente institucional |

| LinkSNIFA\_UF | Trazabilidad | No utilizar como predictor | Enlace de la unidad fiscalizable |



\## Conservación de columnas



Una variable que no sea utilizada como predictor no debe eliminarse automáticamente del conjunto procesado.



Las variables de identificación y trazabilidad pueden conservarse porque permiten auditar los registros, revisar casos particulares y mantener la relación con la fuente institucional.



La selección de variables para modelamiento constituye una operación distinta de la conservación de información en el dataset procesado.





\## Variables y unidad de análisis



La selección definitiva de variables dependerá también de la unidad de análisis adoptada.



Si el análisis se realiza a nivel de procedimiento, deberá verificarse qué variables permanecen constantes para cada ProcesoSancionId y cómo representar aquellas asociadas a múltiples unidades fiscalizables.



Por esta razón, la matriz presentada corresponde a una selección preliminar para etapas posteriores y no implica una eliminación física de columnas del conjunto procesado.

