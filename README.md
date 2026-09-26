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

La lógica de la Fase 3 se encuentra separada en módulos Python ubicados en `src/`,
siguiendo una separación de responsabilidades entre procesamiento, normalización,
medición y validación.

- `src/procesamiento.py`: funciones relacionadas con la preparación y transformación
  de los datos y la construcción del universo analítico.
- `src/mediciones.py`: funciones utilizadas para medir tiempo de ejecución y consumo
  de memoria.
- `src/validaciones.py`: funciones destinadas a verificar la consistencia y
  equivalencia de los resultados.
- `src/verificar_dataset.py`: controles básicos sobre el dataset procesado.
- `src/normalizacion_regiones.py`: implementaciones iterativa y vectorizada para
  normalizar la variable `RegionNombre`.
- `src/normalizacion_poo.py`: implementación de la normalización mediante
  programación orientada a objetos.
- `src/comparar_normalizacion_regiones.py`: comparación experimental de las
  implementaciones iterativa y vectorizada.

Esta separación permite que cada módulo tenga una responsabilidad específica.
El notebook coordina el análisis, mientras que las funciones reutilizables se
mantienen fuera del notebook.

La organización permite modificar o incorporar una estrategia algorítmica sin
tener que modificar el procesamiento, las mediciones o las validaciones del
proyecto.

## Evaluación experimental

La Fase 3 incorpora mediciones experimentales para complementar el análisis
teórico de complejidad.

Las mediciones de tiempo se realizan mediante `time.perf_counter()` y las
mediciones de memoria mediante `tracemalloc`.

Se realizaron las siguientes evaluaciones:

1. Construcción del universo analítico y cálculo de duración de los procedimientos.
2. Comparación entre una implementación iterativa y una implementación vectorizada
   mediante Pandas para la normalización de `RegionNombre`.
3. Evaluación de las implementaciones utilizando distintos tamaños de entrada.
4. Comparación del consumo de tiempo y memoria entre las estrategias.

La equivalencia funcional de las implementaciones fue verificada mediante `assert`
y mediante la comparación con los resultados obtenidos durante la Fase 2.

La evaluación de la recursividad se realizó como parte del análisis de alternativas
algorítmicas. Sin embargo, el problema de los procedimientos sancionatorios no
presenta una estructura jerárquica o una dependencia entre registros que justifique
su utilización como estrategia principal. Por esta razón, la solución del proyecto
prioriza las implementaciones iterativa y vectorizada, que son coherentes con la
naturaleza tabular del conjunto de datos.

Los resultados experimentales se interpretan considerando las condiciones
específicas de ejecución, el tamaño del conjunto de datos y las características
de las implementaciones utilizadas.

## Criterios de optimización

La evaluación de las estrategias considera los siguientes criterios:

- **Tiempo de ejecución:** comparación de los tiempos obtenidos para distintos
  tamaños de entrada.
- **Consumo de memoria:** medición del uso de memoria durante la ejecución.
- **Escalabilidad:** análisis del comportamiento de las estrategias al aumentar
  el número de registros.
- **Modularidad:** separación de responsabilidades para facilitar el mantenimiento
  y extensión del proyecto.
- **Reutilización:** utilización de funciones independientes en diferentes
  evaluaciones.
- **Reproducibilidad:** ejecución de las comparaciones bajo los mismos datos y
  criterios de medición.

Los resultados mostraron que para el conjunto inicial de 984 registros la
implementación iterativa presentó un menor tiempo de ejecución. Al aumentar el
tamaño de entrada a 3.936 y 15.744 registros, la implementación vectorizada
presentó menores tiempos.

Este comportamiento puede explicarse por el costo fijo asociado a las operaciones
de Pandas. En conjuntos pequeños, dicho costo puede representar una proporción
importante del tiempo total. Al aumentar el volumen de datos, las operaciones
vectorizadas permiten procesar los datos mediante operaciones internas optimizadas,
reduciendo el costo relativo de recorrer los registros individualmente.

En términos de memoria, la implementación iterativa presentó un menor consumo
máximo en las tres pruebas realizadas. Por ello, la evaluación de eficiencia
considera conjuntamente tiempo de ejecución, consumo de memoria y comportamiento
frente al aumento del tamaño de entrada.

## Arquitectura y proyección

La arquitectura mantiene separados el procesamiento de datos, las estrategias
algorítmicas, las mediciones y las validaciones.

Esta organización reduce el acoplamiento entre los componentes y permite incorporar
nuevas estrategias de análisis sin modificar completamente el flujo existente.

La estructura desarrollada constituye una base para la Fase 4, ya que permite
incorporar nuevos algoritmos o análisis utilizando las funciones de procesamiento,
medición y validación existentes.

## Reproducibilidad del entorno

El proyecto utiliza un entorno virtual de Python y las dependencias se encuentran registradas en `requirements.txt`.

Para reconstruir el entorno desde la raíz del proyecto:

```bash
python -m venv .venv