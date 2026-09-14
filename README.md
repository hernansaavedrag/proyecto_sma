# Proyecto SMA - Procedimientos Sancionatorios

Proyecto desarrollado en el marco del Magíster en Ciencia de Datos e Inteligencia Artificial.

El proyecto aplica herramientas de Ciencia de Datos al conjunto de datos abiertos de procedimientos sancionatorios de la Superintendencia del Medio Ambiente (SMA), con énfasis en la preparación de un flujo de trabajo reproducible, documentado y trazable.

## Pregunta de análisis

¿Qué factores se asocian a multas de mayor magnitud, medidas en UTA, considerando características territoriales, económicas y administrativas de los procedimientos sancionatorios?

## Fuente de datos

El proyecto utiliza el conjunto de datos de procedimientos sancionatorios publicado por la Superintendencia del Medio Ambiente (SMA).

- **Archivo:** `Sancionatorios.xlsx`
- **Fecha de descarga:** 09 de septiembre de 2026
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

### Dataset procesado

`data/processed/sancionatorios_procesados.csv`

Resultado reproducible de las transformaciones y criterios documentados en la Fase 2. El archivo contiene 984 registros y 20 variables.

## Reproducibilidad del entorno

El proyecto utiliza un entorno virtual de Python y las dependencias se encuentran registradas en `requirements.txt`.

Para reconstruir el entorno desde la raíz del proyecto:

```bash
python -m venv .venv