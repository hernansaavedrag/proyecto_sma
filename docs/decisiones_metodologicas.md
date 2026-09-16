\# Decisiones metodológicas del proyecto SMA



\## Fuente de datos



El proyecto utiliza el conjunto de datos de procedimientos sancionatorios de la Superintendencia del Medio Ambiente (SMA).



La copia utilizada fue descargada el 09 de septiembre de 2026 y se conserva sin modificaciones en:



`data/raw/Sancionatorios.xlsx`



\## Definición del universo analítico



El conjunto original contiene 3.537 registros.



Para el análisis de magnitud de multas se seleccionaron inicialmente los registros cuyo estado corresponde a `Terminado - Sanción`.



Este subconjunto contiene 1.094 registros.



De ellos, 984 presentan un valor informado en `MultaTotalUTA`.



Los 110 registros sin multa informada no fueron imputados como cero, debido a que ausencia de información y multa igual a cero representan situaciones conceptualmente diferentes.



\## Decisión sobre valores extremos



La distribución de `MultaTotalUTA` presenta una marcada asimetría positiva.



Mediante el criterio IQR se identificaron 149 registros potencialmente atípicos. Estos valores no fueron eliminados automáticamente, debido a que pueden representar sanciones reales de elevada magnitud y son relevantes para la pregunta de investigación.



Por esta razón, la mediana se utiliza como medida descriptiva principal y la media y el máximo como medidas complementarias.



\## Decisiones pendientes



Antes de la etapa de modelamiento deberá definirse explícitamente la unidad de análisis.



El conjunto procesado contiene registros donde un mismo `ProcesoSancionId` puede aparecer asociado a más de una unidad fiscalizable. Por lo tanto, el número de filas no debe interpretarse automáticamente como número de procedimientos únicos.



Esta situación deberá evaluarse antes del análisis inferencial para evitar que procedimientos asociados a múltiples unidades tengan una representación desproporcionada.

## Reproducibilidad, trazabilidad y documentación

En este proyecto se distinguen tres conceptos complementarios que cumplen funciones diferentes dentro del flujo de trabajo científico.

### Reproducibilidad

La reproducibilidad corresponde a la capacidad de reconstruir el entorno y volver a ejecutar el análisis. Para ello se utiliza un entorno virtual de Python, el archivo `requirements.txt`, rutas relativas, notebooks ejecutables y una copia fija del conjunto de datos original.

Como verificación práctica, el repositorio fue clonado en un computador diferente al utilizado inicialmente. A partir de `requirements.txt` se reconstruyó el entorno virtual y se inició JupyterLab correctamente.

### Trazabilidad

La trazabilidad corresponde al registro de la evolución del proyecto. Git permite identificar los cambios mediante commits y GitHub mantiene el historial compartido del equipo.

El trabajo colaborativo se organiza mediante ramas individuales y la posterior integración de los cambios mediante Pull Requests.

### Documentación

La documentación explica las decisiones tomadas durante el desarrollo. Las celdas Markdown de los notebooks justifican las decisiones metodológicas, mientras que el README describe la fuente de datos, la estructura del repositorio y las instrucciones necesarias para reproducir el proyecto.

De esta forma, el entorno permite reproducir, Git permite rastrear los cambios y la documentación permite comprender las decisiones adoptadas.

