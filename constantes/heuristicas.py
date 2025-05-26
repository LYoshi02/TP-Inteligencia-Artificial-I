from dataclasses import dataclass

@dataclass
class InfoHeuristica:
    nombre: str
    texto: str

class HEURISTICAS:
    distancia_euclidiana = InfoHeuristica("euclidiana", "Euclidiana")
    distancia_manhattan = InfoHeuristica("manhattan", "Manhattan")
