\# Clasificación de variables — SNIFA Sancionatorios



Dataset: `data/raw/Sancionatorios.xlsx` (3.537 filas, 19 columnas). Clasificación elaborada por Lenin en la rama `feature/seleccion-variables`, como insumo para el análisis de severidad de multas ambientales.



\## 1. Variable objetivo



\*\*MultaTotalUTA\*\*: es el resultado que el equipo busca explicar (severidad de la multa, expresada en UTA). Tiene un 63,3% de valores nulos sobre el total de 3.537 registros, pero baja a 10,05% dentro de la sub-base de procesos con estado "Terminado - Sanción". Un valor nulo aquí no es un dato perdido: significa que ese proceso no terminó en una multa asignada (proceso en curso, o terminó con Programa de Cumplimiento satisfactorio en vez de sanción).



\## 2. Variables potencialmente explicativas



\- \*\*RegionNombre\*\* y \*\*ComunaNombre\*\*: ubicación geográfica de la unidad fiscalizada. Región es un catálogo cerrado de 16-18 valores, manejable como categórica. Comuna es mucho más granular (cientos de valores posibles en Chile) y necesitará agruparse o tratarse con cuidado antes de usarse como predictor directo, pero aporta detalle geográfico que Región no captura.

\- \*\*CategoriaEconomicaNombre\*\* y \*\*SubCategoriaEconomicaNombre\*\*: rubro económico de la empresa fiscalizada, a dos niveles de detalle. Categoría es un catálogo cerrado de 16 valores; Subcategoría es más fina y probablemente supere el umbral de 15 categorías manejables, por lo que también requiere agrupación.

\- \*\*ProcesoSancionTipoNombre\*\*: tipo de proceso sancionatorio — una de las variables explicativas ya declaradas en la problemática del equipo.

\- \*\*FechaInicio\*\* y \*\*FechaTermino\*\*: por sí solas son variables temporales, pero son la base para derivar variables como la duración del proceso. `FechaTermino` vacía indica un proceso todavía en curso, lo que hay que declarar como limitación si se usa para construir variables de severidad.

\- \*\*ProcesoSancionEstado\*\* y \*\*ConfirmaPdC\*\*: no son explicativas de la severidad en sí, pero definen qué subconjunto de procesos tiene una multa asignable (delimitan el universo de análisis, ligado directamente al sesgo de procesos abiertos).



\## 3. Variables de identificación/trazabilidad



\*\*ProcesoSancionId\*\*, \*\*Expediente\*\*, \*\*UnidadFiscalizableId\*\*, \*\*LinkSNIFA\*\* y \*\*LinkSNIFA\_UF\*\* identifican de forma única (o casi única) cada proceso, unidad fiscalizable o ficha en el sistema SNIFA. Sirven para trazar, verificar o enlazar registros con la fuente original, no para alimentar un modelo o análisis estadístico.



\## 4. Variables que no deberían utilizarse directamente como predictores



\- \*\*LinkSNIFA\*\* y \*\*LinkSNIFA\_UF\*\*: son URLs a la ficha individual de cada fiscalización; no tienen contenido analítico por sí mismas, solo sirven para trazabilidad (ver punto 3).

\- \*\*Nombre\*\* (empresa fiscalizada): tiene alta cardinalidad (3.183 de 3.537 valores únicos). Usarla directamente como predictor categórico generaría sobreajuste; su valor analítico está en derivar de ella variables como "número de sanciones previas de la misma empresa", no en usarla tal cual.

\- \*\*FechaActualizacion\*\*: es la misma fecha (12-09-2026) en las 3.537 filas — un metadato del snapshot completo del dataset, no una variable que varíe por registro. No aporta información para diferenciar casos.

## Criterios para la selección de variables

| Variable | Rol | Decisión | Justificación |
|---|---|---|---|
| MultaTotalUTA | Variable objetivo | Utilizar | Representa la magnitud de la sanción económica medida en UTA. |
| RegionNombre | Explicativa territorial | Utilizar | Permite estudiar diferencias territoriales en la magnitud de las multas. |
| ComunaNombre | Explicativa territorial | Evaluar | Presenta mayor cardinalidad y deberá evaluarse su utilidad según el análisis posterior. |
| CategoriaEconomicaNombre | Explicativa económica | Utilizar | Permite comparar la magnitud de las multas entre actividades económicas. |
| SubCategoriaEconomicaNombre | Explicativa económica | Evaluar | Aporta mayor detalle, pero presenta mayor cardinalidad. |
| ProcesoSancionTipoNombre | Explicativa administrativa | Utilizar | Identifica el origen o tipo del procedimiento sancionatorio. |
| DuracionDias | Explicativa temporal | Utilizar | Permite estudiar una posible asociación entre duración del procedimiento y magnitud de la multa. |
| ProcesoSancionId | Identificación | No utilizar como predictor | Identifica procedimientos y permite revisar registros repetidos. |
| Expediente | Identificación | No utilizar como predictor | Permite mantener trazabilidad con el procedimiento administrativo. |
| LinkSNIFA | Trazabilidad | No utilizar como predictor | Corresponde a un enlace de consulta y no a una característica explicativa. |
| LinkSNIFA_UF | Trazabilidad | No utilizar como predictor | Corresponde a un enlace asociado a la unidad fiscalizable. |

La exclusión de una variable del modelamiento no implica necesariamente eliminarla del conjunto procesado. Las variables de identificación y trazabilidad pueden conservarse para revisar y relacionar los registros con la fuente institucional, aunque no sean utilizadas como predictores.