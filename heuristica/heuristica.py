import math
from typing import Tuple

def heuristica_manhattan(nodo_actual: Tuple[float, float], nodo_objetivo: Tuple[float, float]) -> float:
    """
    Calcula la distancia Manhattan entre dos puntos.
    Parámetros:
        nodo_actual: Tupla con (x, y) del nodo actual.
        nodo_objetivo: Tupla con (x, y) del nodo objetivo.
    Retorna:
        Distancia Manhattan como float.
    """
    x1, y1 = nodo_actual
    x2, y2 = nodo_objetivo
    return abs(x2 - x1) + abs(y2 - y1)

def heuristica_linea_recta(nodo_actual: Tuple[float, float], nodo_objetivo: Tuple[float, float]) -> float:
    """
    Calcula la distancia Euclidiana (en línea recta) entre dos puntos.
    Parámetros:
        nodo_actual: Tupla con (x, y) del nodo actual.
        nodo_objetivo: Tupla con (x, y) del nodo objetivo.
    Retorna:
        Distancia Euclidiana como float.
    """
    x1, y1 = nodo_actual
    x2, y2 = nodo_objetivo
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def heuristica_ambas(nodo_actual: Tuple[float, float], nodo_objetivo: Tuple[float, float]) -> Tuple[float, float]:
    """
    Calcula ambas heurísticas (Manhattan y Euclidiana) entre dos puntos.
    Parámetros:
        nodo_actual: Tupla con (x, y) del nodo actual.
        nodo_objetivo: Tupla con (x, y) del nodo objetivo.
    Retorna:
        Tupla con (distancia_manhattan, distancia_linea_recta)
    """
    h_manhattan = heuristica_manhattan(nodo_actual, nodo_objetivo)
    h_linea_recta = heuristica_linea_recta(nodo_actual, nodo_objetivo)
    return h_manhattan, h_linea_recta
