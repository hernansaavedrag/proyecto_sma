# Análisis del rubro económico — F4

Fuente: `F4/F4_Analisis_Resultados.ipynb`, sección 6 (tabla `resumen_rubro` y Figura 1, boxplot de
`MultaTotalUTA` por `CategoriaEconomicaNombre` en escala logarítmica). Unidad de análisis: procedimiento
sancionatorio (`ProcesoSancionId`), universo de 963 procedimientos.

## Resultado observado

La magnitud de las multas cambia bastante según el rubro económico. Las medianas van desde 3,1 UTA en
Equipamiento hasta 443,0 UTA en Minería, una diferencia de más de 100 veces entre el valor central del
rubro más alto y el del más bajo.

| Rubro | n | Mediana (UTA) | Q1 | Q3 |
|---|---:|---:|---:|---:|
| Minería | 40 | 443,0 | 48,0 | 2.403,8 |
| Energía | 17 | 345,0 | 76,0 | 809,0 |
| Infraestructura Hidráulica | 2 | 135,0 | 77,5 | 192,5 |
| Saneamiento Ambiental | 27 | 91,0 | 23,0 | 234,7 |
| Infraestructura de Transporte | 10 | 52,0 | 8,3 | 119,3 |
| Agroindustrias | 75 | 29,0 | 9,9 | 75,6 |
| Vivienda e Inmobiliarios | 150 | 27,0 | 3,8 | 62,0 |
| Infraestructura Portuaria | 8 | 21,6 | 4,2 | 93,8 |
| Transportes y almacenajes | 3 | 14,0 | 7,7 | 106,0 |
| Instalación fabril | 47 | 11,0 | 2,1 | 67,5 |
| Pesca y Acuicultura | 30 | 10,6 | 2,1 | 25,4 |
| Otras categorías | 17 | 6,0 | 2,5 | 28,0 |
| Forestal | 17 | 5,8 | 2,0 | 21,0 |
| ETFA | 4 | 4,2 | 2,6 | 29,6 |
| Equipamiento | 511 | 3,1 | 1,6 | 9,4 |

Valores tomados de `resumen_rubro`, redondeados a un decimal. La suma de `n` es 958: hay 5 procedimientos
sin `CategoriaEconomicaNombre` que `groupby` deja fuera de la tabla y de la figura.

En la Figura 1 se ven tres bloques:

- **Alto:** Minería y Energía. Sus medianas superan las 300 UTA y su Q1 (48 y 76 UTA) ya está por encima de
  la mediana de todos los rubros del bloque bajo.
- **Intermedio:** Saneamiento Ambiental, Infraestructura de Transporte, Agroindustrias y Vivienda e
  Inmobiliarios, con medianas entre 27 y 91 UTA.
- **Bajo:** Equipamiento, Forestal, Otras categorías, Pesca y Acuicultura e Instalación fabril, con medianas
  de 3 a 11 UTA.

Los rubros con menos de 10 procedimientos (Infraestructura Hidráulica, Transportes y almacenajes, ETFA e
Infraestructura Portuaria) no se asignan a ningún bloque; ver la sección sobre tamaño de los grupos.

## Principales diferencias

- **Minería frente a Equipamiento.** La mediana de Minería (443,0 UTA) es unas 140 veces la de Equipamiento
  (3,1 UTA). Además, las cajas no se tocan: el Q1 de Minería (48,0) supera con creces el Q3 de Equipamiento
  (9,4). La diferencia no depende de unos pocos casos extremos, sino que abarca la mitad central de ambas
  distribuciones.
- **Dispersión.** Minería tiene el rango intercuartílico más amplio (de 48 a 2.404 UTA). Dentro del mismo
  rubro conviven multas moderadas y multas muy altas. Equipamiento, en cambio, está concentrado entre
  1,6 y 9,4 UTA.
- **Mediana frente a promedio.** En casi todos los rubros el promedio supera ampliamente a la mediana. Pesca
  y Acuicultura es el caso más llamativo: mediana de 10,6 UTA y promedio de 478,6 UTA, porque tiene una multa
  máxima de 8.914 UTA. Esto confirma que conviene usar la mediana y los cuartiles para comparar rubros, como
  hace el notebook.
- **Rubros con muchos casos.** Vivienda e Inmobiliarios (n = 150) y Agroindustrias (n = 75) tienen medianas
  parecidas (27 y 29 UTA), ambas bastante por encima de Equipamiento (n = 511). Como son los grupos con más
  procedimientos, son también las comparaciones más estables de la tabla.

## Consideración sobre el tamaño de los grupos

Los rubros tienen tamaños muy distintos. Equipamiento reúne 511 procedimientos, más de la mitad del
universo, mientras que Infraestructura Hidráulica tiene 2, Transportes y almacenajes 3 y ETFA 4.

Con tan pocos casos, la mediana y los cuartiles dependen de uno o dos valores:

- En **Infraestructura Hidráulica** (n = 2), la "mediana" de 135 UTA es simplemente el promedio de sus dos
  multas. Por eso aparece en tercer lugar, por encima de rubros con decenas de casos. No conviene tratar esa
  posición como un resultado.
- En **Transportes y almacenajes** (n = 3) y **ETFA** (n = 4), los cuartiles se interpolan entre muy pocas
  observaciones, así que la caja del boxplot no describe una distribución.
- **Energía** (n = 17) e **Infraestructura de Transporte** (n = 10) tienen tamaños modestos. Sus valores son
  orientadores, y basta que entre o salga un procedimiento grande para que cambien de forma visible.

Para la interpretación conviene apoyarse en los rubros con al menos unos 10 procedimientos y presentar los
demás solo como referencia, indicando siempre su `n`.

## Interpretación

Descriptivamente, el rubro económico es el factor en que más se separan las magnitudes de multa dentro de
este universo. Los procedimientos de Minería y Energía se concentran en montos mucho mayores que los de
Equipamiento, Forestal u Otras categorías, y esa separación se mantiene aunque se mire la mediana en lugar
del promedio y aunque se dejen fuera los valores extremos. El contraste con las otras secciones del notebook
ayuda a dimensionarlo: entre regiones las medianas van de 2,3 a 17,15 UTA, y entre Denuncia y Fiscalización
casi no hay diferencia (7,0 frente a 7,4 UTA).

También se observa que un rubro con muchos procedimientos no tiene por qué concentrar las multas más altas.
Equipamiento es el rubro más frecuente y, al mismo tiempo, el de mediana más baja. Minería, con 40
procedimientos, tiene la mediana más alta.

Hay una posible explicación de contexto, que este análisis no pone a prueba: los rubros de mediana alta
suelen corresponder a proyectos de gran escala, con más componentes ambientales regulados. Esa es una
hipótesis para trabajos posteriores, no algo que se desprenda de la tabla.

## Limitación

Este análisis muestra diferencias y asociaciones descriptivas entre el rubro económico y la magnitud de las
multas. No permite afirmar que un rubro cause multas mayores. Las diferencias observadas pueden deberse a
otras variables que no se controlaron aquí, como el tamaño de la unidad fiscalizable, el número y la
gravedad de los cargos, la región, el tipo de proceso o el período. Tampoco se aplicaron pruebas
estadísticas ni modelos que consideren estas variables al mismo tiempo.

Además:

- Los 5 procedimientos sin rubro informado quedan fuera de esta comparación.
- Las categorías provienen de la clasificación de la SMA; por ejemplo, "Otras categorías" agrupa actividades
  heterogéneas.
- Los resultados corresponden al universo analítico definido en el proyecto (procedimientos terminados con
  multa informada) y no necesariamente se extienden a procedimientos abiertos o sin multa.

## Observación para revisión del notebook

En la sección 10 (Síntesis de resultados), la mediana de Minería aparece como **443,5 UTA**, pero la tabla
`resumen_rubro` muestra **443,0 UTA**. Con n = 40 la mediana es el promedio de los valores 20.º y 21.º
(398 y 488 UTA), es decir, 443,0. Sugiero corregir la cifra en la síntesis para que el texto coincida con la
tabla.
