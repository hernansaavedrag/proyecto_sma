# Proyecto SMA - Procedimientos Sancionatorios

Proyecto desarrollado en el marco del Magíster en Ciencia de Datos e Inteligencia Artificial.

El proyecto aplica herramientas de Ciencia de Datos al conjunto de datos abiertos de procedimientos sancionatorios de la Superintendencia del Medio Ambiente (SMA), con énfasis en la preparación de un flujo de trabajo reproducible, documentado y trazable.

## Pregunta de análisis

¿Qué factores se asocian a multas de mayor magnitud, medidas en UTA, considerando características territoriales, económicas y administrativas de los procedimientos sancionatorios?

## Fuente de datos

El proyecto utiliza el conjunto de datos de procedimientos sancionatorios publicado por la Superintendencia del Medio Ambiente (SMA).

- **Archivo:** `Sancionatorios.xlsx`
- **Fecha de descarga:** 09 de septiembre de 2026
- **Hora de descarga:** 10:00 hrs
- **Ubicación:** `data/raw/Sancionatorios.xlsx`
- **Estado:** copia original sin modificaciones
- **Fuente:** Superintendencia del Medio Ambiente (SMA)

La fecha de descarga se registra debido a que la fuente puede actualizarse posteriormente. La copia almacenada en `data/raw/` constituye la versión de referencia utilizada en este proyecto y permite identificar exactamente el conjunto de datos sobre el cual se realizaron los análisis.

## Universo analítico

El conjunto original contiene 3.537 registros.

Para estudiar la magnitud de las multas se identificaron 1.094 registros correspondientes a procedimientos con estado `Terminado - Sanción`.

De ellos, 984 poseen un valor informado en `MultaTotalUTA` y constituyen el universo analítico utilizado para el análisis de magnitud de multas.

Los 110 registros sin valor informado de multa no son interpretados como multas iguales a cero y se excluyen de este universo analítico.

## Estructura del proyecto

- `F1/`: definición del problema, objetivos, alcance, entorno y reconocimiento inicial del conjunto de datos.
- `F2/`: exploración, procesamiento, transformación y validación.
- `F3/`: diseño, implementación y evaluación experimental de algoritmos.
- `data/raw/`: copia original del conjunto de datos sin modificaciones.
- `data/processed/`: datos resultantes del procesamiento.
- `src/`: funciones y módulos reutilizables.
- `docs/`: documentación y evidencias complementarias.
- `requirements.txt`: dependencias necesarias para reproducir el entorno.
- `README.md`: descripción general e instrucciones de reproducción del proyecto.

## Archivos principales

### Fase 1

`F1/F1_Definicion.ipynb`

Documenta la definición del problema, objetivos, alcance, configuración del entorno y reconocimiento estructural inicial del conjunto de datos.

### Fase 2

`F2/F2_Procesamiento.ipynb`

Documenta las decisiones de procesamiento, definición del universo analítico, tratamiento de valores ausentes, conversión de variables, normalización de categorías, análisis de valores potencialmente atípicos y validaciones del conjunto procesado.

### Fase 3

`F3/F3_Algoritmos_Complejidad.ipynb`

Documenta el diseño, implementación y evaluación experimental de los algoritmos desarrollados para el análisis del conjunto de datos.

La Fase 3 complementa el análisis realizado en las etapas anteriores mediante la evaluación de diferentes estrategias de implementación, considerando:

- eficiencia temporal;
- consumo de memoria;
- claridad y modularidad del código;
- reutilización de funciones y módulos;
- comparación de distintas estrategias algorítmicas.

### Dataset procesado

`data/processed/sancionatorios_procesados.csv`

Resultado reproducible de las transformaciones y criterios documentados en la Fase 2. El archivo contiene 984 registros y 20 variables.

## Algoritmos y módulos

La lógica de procesamiento se encuentra separada en módulos Python ubicados en `src/`.

- `src/procesamiento.py`: funciones relacionadas con la preparación y transformación de los datos.
- `src/algoritmos.py`: funciones correspondientes a los algoritmos desarrollados para el análisis.
- `src/mediciones.py`: funciones utilizadas para medir tiempos de ejecución y consumo de memoria.
- `src/normalizacion_regiones.py`: implementación de la normalización de `RegionNombre`.
- `src/comparar_normalizacion_regiones.py`: comparación experimental entre las implementaciones iterativa y vectorizada.

Esta organización permite separar la lógica de procesamiento, los algoritmos y las funciones de medición, favoreciendo la reutilización, trazabilidad y mantenimiento del código.

## Evaluación experimental

La Fase 3 incorpora mediciones experimentales para complementar el análisis teórico de complejidad.

Las mediciones de tiempo se realizan mediante `time.perf_counter()` y las mediciones de memoria mediante `tracemalloc`.

Se realizaron las siguientes comparaciones:

1. Construcción del universo analítico y cálculo de duración de procedimientos.
2. Comparación entre programación estructurada y programación recursiva.
3. Comparación experimental entre una implementación iterativa y una implementación recursiva.
4. Comparación entre una implementación iterativa y una implementación vectorizada mediante Pandas para la normalización de `RegionNombre`.
5. Evaluación utilizando distintos tamaños de entrada.

Las comparaciones funcionales fueron verificadas mediante `assert` y mediante la comparación con resultados obtenidos durante la Fase 2.

Los resultados experimentales se interpretan considerando las condiciones específicas de ejecución, el tamaño del conjunto de datos y las características de las implementaciones utilizadas.

## Reproducibilidad del entorno

El proyecto utiliza un entorno virtual de Python y las dependencias se encuentran registradas en `requirements.txt`.

Para reconstruir el entorno desde la raíz del proyecto:

```bash
python -m venv .venv