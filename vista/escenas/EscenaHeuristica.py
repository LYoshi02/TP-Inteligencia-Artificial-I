from algoritmo2.recorrido_algoritmo import RecorridoAlgoritmo
from controlador.controlador import Controlador
from vista.grafo.grafo_scene import GrafoScene

class EscenaHeuristica:
    def __init__(self, controlador: Controlador, escena_grafo: GrafoScene, heuristica: str):
        self._controlador = controlador
        self._escena_grafo = escena_grafo
        self._heuristica = heuristica

    def graficar_grafo(self, recorrido: RecorridoAlgoritmo) -> None:
        self._escena_grafo.graficar_grafo(self._controlador.obtener_grafo_busqueda(self._heuristica), recorrido)

    def avanzar_paso(self) -> None:
        recorrido = self._controlador.avanzar_paso(self._heuristica)
        self.graficar_grafo(recorrido)

    def retroceder_paso(self) -> None:
        recorrido = self._controlador.retroceder_paso(self._heuristica)
        self.graficar_grafo(recorrido)

    @property
    def heuristica(self):
        return self._heuristica