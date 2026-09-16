\# Definición de la unidad de análisis



\## Antecedente



Durante la validación del conjunto procesado se detectó que `ProcesoSancionId` no constituye una clave única a nivel de fila.



El conjunto analítico contiene 984 registros, pero algunos identificadores de procedimiento aparecen asociados a más de una unidad fiscalizable. Por esta razón, una fila del conjunto de datos no debe interpretarse automáticamente como un procedimiento sancionatorio único.



\## Evidencia observada



La revisión de los identificadores repetidos mostró casos donde un mismo `ProcesoSancionId` mantiene el mismo expediente y el mismo valor de `MultaTotalUTA`, pero aparece en varias filas asociadas a distintas unidades fiscalizables.



Entre los casos revisados se observaron:



\- `ProcesoSancionId 1192`: 18 registros, un expediente y un único valor de multa de 3.142 UTA.

\- `ProcesoSancionId 1569`: 3 registros, un expediente y un único valor de multa de 1.006 UTA.

\- `ProcesoSancionId 1471`: 2 registros, un expediente y un único valor de multa de 19 UTA.

\- `ProcesoSancionId 2610`: 2 registros, un expediente y un único valor de multa de 4,2 UTA.



Esto indica que la repetición del identificador no corresponde necesariamente a un error o duplicado accidental, sino que puede responder a la granularidad del conjunto publicado por la SMA.



\## Implicancia analítica



La pregunta del proyecto busca estudiar qué factores se asocian con multas de mayor magnitud.



Si se utilizara directamente cada fila como una observación independiente, un procedimiento asociado a múltiples unidades fiscalizables podría quedar representado varias veces con el mismo valor de multa.



Esto podría otorgar un peso desproporcionado a determinados procedimientos en análisis estadísticos o modelos posteriores.



\## Decisión metodológica



Para los análisis descriptivos desarrollados en la Fase 2 se mantiene el conjunto procesado a nivel de registro, conservando la información original y su relación con las unidades fiscalizables.



Sin embargo, antes de realizar análisis inferenciales o modelos predictivos, deberá construirse o evaluarse una vista a nivel de procedimiento, utilizando `ProcesoSancionId` como referencia y verificando la consistencia de las variables asociadas.



De esta manera se distingue entre:



\- \*\*nivel de registro:\*\* conserva la granularidad de la fuente SMA y las relaciones con unidades fiscalizables;

\- \*\*nivel de procedimiento:\*\* evita que un mismo procedimiento y su multa sean contabilizados repetidamente cuando el objetivo sea estudiar factores asociados a la magnitud de la sanción.



La transformación entre ambos niveles deberá documentarse explícitamente y no se eliminarán filas del conjunto original `data/raw/Sancionatorios.xlsx`.


## Criterio para etapas posteriores

La existencia de procedimientos repetidos a nivel de fila se considera una característica estructural relevante del conjunto de datos y no un error que deba corregirse mediante eliminación automática de duplicados.

Para futuras etapas de análisis o modelamiento se deberá comparar explícitamente el número de registros con el número de procedimientos únicos y definir el nivel de observación apropiado según la pregunta analítica.

Esta decisión permite evitar dos errores metodológicos: eliminar información válida asociada a distintas unidades fiscalizables o contabilizar repetidamente una misma multa cuando el análisis requiera trabajar a nivel de procedimiento.
