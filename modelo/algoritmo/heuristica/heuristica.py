from abc import ABC, abstractmethod

class Heuristica(ABC):
    @abstractmethod
    def calcular(self, x1: float, y1: float, x2: float, y2: float) -> float:
        pass