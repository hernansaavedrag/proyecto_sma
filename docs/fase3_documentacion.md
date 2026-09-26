# Documentación de la Fase 3

## 1. Objetivo

La Fase 3 del proyecto tiene como objetivo diseñar, implementar y evaluar estrategias
algorítmicas en Python para el procesamiento y análisis del conjunto de datos de
procedimientos sancionatorios de la Superintendencia del Medio Ambiente (SMA).

El análisis considera criterios de eficiencia temporal, consumo de memoria,
modularidad, reutilización de código y reproducibilidad.

## 2. Estructura del proyecto

La Fase 3 utiliza una organización modular que separa el notebook principal de las
funciones de procesamiento, normalización, medición y validación.

La estructura relacionada con la fase es:

F3/
└── F3_Algoritmos_Complejidad.ipynb

src/
├── mediciones.py
├── procesamiento.py
├── validaciones.py
├── verificar_dataset.py
├── normalizacion_regiones.py
├── normalizacion_poo.py
└── comparar_normalizacion_regiones.py

La separación de estos módulos responde a una decisión de diseño basada en la
separación de responsabilidades. El notebook se utiliza como punto de coordinación
del análisis, mientras que las operaciones reutilizables se mantienen en módulos
independientes.

Esta organización permite modificar una operación específica sin tener que modificar
todo el notebook y facilita la comparación de distintas estrategias sobre un mismo
conjunto de datos.

## 3. Módulos principales

### procesamiento.py

Contiene funciones relacionadas con la preparación y transformación de los datos.

Entre ellas se encuentra la construcción del universo analítico y el cálculo de la
duración de los procedimientos sancionatorios.

Se mantiene separado de los algoritmos de normalización para evitar mezclar la
preparación de los datos con las estrategias que posteriormente serán evaluadas.

### mediciones.py

Contiene funciones utilizadas para medir tiempo de ejecución y consumo de memoria.

Este módulo se mantiene independiente para aplicar los mismos criterios de medición
a las diferentes implementaciones y permitir una comparación reproducible.

### validaciones.py

Contiene funciones destinadas a verificar condiciones de consistencia de los datos
y resultados.

Su separación permite validar los resultados sin incorporar las validaciones dentro
de cada implementación algorítmica.

### verificar_dataset.py

Permite ejecutar controles básicos sobre el dataset procesado.

Su función es comprobar las condiciones necesarias del conjunto de datos antes de
utilizarlo en los análisis posteriores.

### normalizacion_regiones.py

Contiene las implementaciones utilizadas para normalizar la variable `RegionNombre`.

La separación de este módulo permite evaluar diferentes estrategias de procesamiento
sobre la misma variable y comprobar que las implementaciones produzcan resultados
equivalentes.

### normalizacion_poo.py

Contiene la implementación de las estrategias de normalización mediante
programación orientada a objetos.

Este módulo permite comparar la organización mediante funciones con una alternativa
basada en clases, manteniendo separada esta implementación del resto del flujo.

### comparar_normalizacion_regiones.py

Contiene funciones utilizadas para realizar la comparación experimental entre las
implementaciones iterativa y vectorizada de la normalización de `RegionNombre`.

Se mantiene separado de los módulos de implementación para evitar mezclar la lógica
del algoritmo con la lógica utilizada para medir y comparar su desempeño.

Esta separación permite incorporar nuevas estrategias de normalización en futuras
pruebas sin modificar el procesamiento general de los datos.

## 4. Decisiones de arquitectura

La arquitectura se diseñó buscando una separación clara de responsabilidades.

El procesamiento de datos se mantiene separado de las implementaciones algorítmicas
porque los algoritmos deben poder evaluarse utilizando el mismo conjunto de entrada.

Las funciones de medición se mantienen independientes porque las distintas
implementaciones deben ser evaluadas utilizando los mismos criterios de tiempo y
memoria.

Las funciones de validación también se mantienen separadas para comprobar la
equivalencia de los resultados sin depender de una implementación específica.

Esta organización reduce el acoplamiento entre los componentes y facilita la
reutilización de las funciones desarrolladas.

Además, permite que una modificación en un algoritmo no obligue a modificar el
procesamiento de los datos, las mediciones o las validaciones.

## 5. Reproducibilidad

El proyecto mantiene separados los datos originales, los datos procesados, el
código fuente y los notebooks de análisis.

La utilización de Git y GitHub permite registrar los cambios realizados durante el
desarrollo y mantener trazabilidad sobre las diferentes versiones del proyecto.

El notebook de la Fase 3 integra las funciones desarrolladas en `src/`, permitiendo
reproducir las mediciones y comparaciones realizadas.

## 6. Trabajo colaborativo

El desarrollo de la Fase 3 se realiza mediante ramas independientes y Pull Requests.

Cada integrante puede desarrollar una parte específica del proyecto sin modificar
directamente la rama principal `main`.

Posteriormente, los cambios son revisados e integrados mediante GitHub.

Este flujo permite mantener trazabilidad de los cambios y reducir conflictos entre
los integrantes durante el desarrollo.

## 7. Evidencias experimentales

La Fase 3 incorpora mediciones de tiempo de ejecución y consumo de memoria.

También se realizan comparaciones entre diferentes estrategias de implementación,
verificando previamente que los resultados obtenidos sean equivalentes.

Las mediciones permiten analizar cómo cambia el comportamiento de las
implementaciones según el tamaño del conjunto de datos.

## 8. Relación con las fases anteriores

La Fase 3 utiliza como entrada los datos procesados durante las fases anteriores,
manteniendo la separación entre los datos originales, los datos transformados y el
código fuente.

Esto permite mantener la trazabilidad y facilitar la reproducción de los análisis
realizados.

El procesamiento desarrollado en las fases anteriores constituye la entrada para
las funciones y algoritmos evaluados durante la Fase 3.

## 9. Proyección hacia la Fase 4

La arquitectura permite incorporar nuevas estrategias de análisis sin modificar
completamente el flujo existente.

Por ejemplo, una nueva implementación algorítmica podría incorporarse como un
módulo independiente y utilizar las funciones existentes de procesamiento,
medición y validación.

De esta manera, la organización actual permite extender el proyecto manteniendo la
separación de responsabilidades, la reutilización del código y la trazabilidad de
los resultados.



