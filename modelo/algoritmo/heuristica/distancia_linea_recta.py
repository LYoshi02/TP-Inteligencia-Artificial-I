import math

from modelo.algoritmo.heuristica.heuristica import Heuristica

class DistanciaLineaRecta(Heuristica):
    def calcular(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)