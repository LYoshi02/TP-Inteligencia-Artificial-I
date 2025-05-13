from dataclasses import dataclass

@dataclass
class InfoHeuristica:
    nombre: str
    texto: str

class HEURISTICAS:
    distancia_linea_recta = InfoHeuristica("linea_recta", "Línea Recta")
    distancia_manhattan = InfoHeuristica("manhattan", "Manhattan")
