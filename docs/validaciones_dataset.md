\# Validaciones del dataset procesado



Las funciones reutilizables definidas en src/validaciones.py fueron aplicadas al conjunto procesado mediante src/verificar\_dataset.py.



La ejecución permitió comprobar:



\- identificadores de procedimiento no nulos: \*OK\*;

\- multas no negativas: \*OK\*;

\- latitudes informadas dentro del rango válido: \*OK\*;

\- longitudes informadas dentro del rango válido: \*OK\*.



Estas comprobaciones separan la lógica de validación de los notebooks y permiten reutilizar los controles en distintas etapas del proyecto.



Las validaciones no sustituyen las decisiones metodológicas. Por ejemplo, la repetición de ProcesoSancionId puede responder a la granularidad de la fuente y no debe interpretarse automáticamente como un error de calidad.

