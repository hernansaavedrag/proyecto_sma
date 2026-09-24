
# Documentación de la Fase 3

## 1. Objetivo
La Fase 3 del proyecto tiene como objetivo diseñar, implementar y evaluar estrategias algorítmicas en Python para el procesamiento y análisis del conjunto de datos de procedimientos sancionatorios de la Superintendencia del Medio Ambiente (SMA).

El análisis considera criterios de eficiencia temporal, consumo de memoria, modularidad, reutilización de código y reproducibilidad.

## 2. Estructura del proyecto

La Fase 3 incorpora una organización modular que separa el notebook principal de las funciones de procesamiento y medición.

La estructura relacionada con la fase es:

text
F3/
└── F3_Algoritmos_Complejidad.ipynb

src/
├── algoritmos.py
├── mediciones.py
├── procesamiento.py
├── validaciones.py
└── verificar_dataset.py
3. Módulos principales
procesamiento.py

Contiene funciones relacionadas con la preparación y transformación de los datos.

Entre ellas se encuentra la construcción del universo analítico y el cálculo de la duración de los procesos.

algoritmos.py

Contiene funciones destinadas al desarrollo y comparación de estrategias algorítmicas.

mediciones.py

Contiene funciones utilizadas para medir tiempo de ejecución y consumo de memoria.


validaciones.py

Contiene funciones destinadas a verificar condiciones de consistencia de los datos y resultados.

verificar_dataset.py

Permite ejecutar controles básicos sobre el dataset procesado.

4. Reproducibilidad

El proyecto mantiene separados los datos originales, los datos procesados, el código fuente y los notebooks de análisis.

La utilización de Git y GitHub permite registrar los cambios realizados durante el desarrollo y mantener trazabilidad sobre las diferentes versiones d>

5. Trabajo colaborativo

El desarrollo de la Fase 3 se realiza mediante ramas independientes y Pull Requests.

Cada integrante puede desarrollar una parte específica del proyecto sin modificar directamente la rama principal main.

Posteriormente, los cambios son revisados e integrados mediante GitHub.

6. Evidencias experimentales

La Fase 3 incorpora mediciones de tiempo de ejecución y consumo de memoria.

También se realizan comparaciones entre diferentes estrategias de implementación, verificando previamente que los resultados obtenidos sean equivalentes.

7. Relación con las fases anteriores

La Fase 3 utiliza como entrada los datos procesados durante las fases anteriores, manteniendo la separación entre los datos originales, los datos transformados y el código fuente.

Esto permite mantener la trazabilidad y facilitar la reproducción de los análisis realizados.



