import time


def medir_tiempo(funcion, datos):
    """
    Mide el tiempo de ejecución de una función sobre un conjunto de datos.

    Parámetros:
        funcion: función que se desea evaluar.
        datos: datos de entrada de la función.

    Retorna:
        resultado: resultado generado por la función.
        tiempo: tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()

    resultado = funcion(datos)

    fin = time.perf_counter()

    tiempo = fin - inicio

    return resultado, tiempo
