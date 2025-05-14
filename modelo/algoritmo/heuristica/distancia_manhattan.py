from modelo.algoritmo.heuristica.heuristica import Heuristica

class DistanciaManhattan(Heuristica):
    def calcular(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return abs(x2 - x1) + abs(y2 - y1)