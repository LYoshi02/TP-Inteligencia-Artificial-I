from algoritmo2.recorrido_algoritmo import RecorridoAlgoritmo
from grafo.arista import Arista
from grafo.grafo import Grafo
from grafo.nodo import Nodo


class Controlador:
    def __init__(self):
        self._grafo = Grafo()
        self._nodo_inicio: Nodo | None = None
        self._nodo_objetivo: Nodo | None = None
        self._recorrido_algoritmo: RecorridoAlgoritmo | None = None

    # Operaciones con Grafo
    def obtener_grafo(self):
        return self._grafo

    def restablecer_grafo(self):
        self._grafo = Grafo()
        self._nodo_inicio = None
        self._nodo_objetivo = None
        self._recorrido_algoritmo = None

    # Operaciones con Nodos
    def obtener_nodo(self, nombre: str) -> Nodo | None:
        return self._grafo.obtener_nodo(nombre)

    def obtener_nodos(self):
        return self._grafo.obtener_nodos()

    def agregar_nodo(self, nombre: str, x: float, y: float) -> Grafo:
        nodo: Nodo = Nodo(nombre, x, y)
        print("Agregando nodo", nodo)
        self._grafo.agregar_nodo(nodo)
        print("Nodos actuales en el grafo:", self._grafo.obtener_nodos())
        return self._grafo

    def eliminar_nodo(self, nombre: str, x: float, y: float) -> Grafo:
        nodo: Nodo = Nodo(nombre, x, y)
        self._grafo.eliminar_nodo(nodo)
        return self._grafo

    def establecer_nodo_inicio(self, nodo: Nodo):
        self._nodo_inicio = nodo
        print("Estado Inicial: ", self._nodo_inicio)

    def establecer_nodo_objetivo(self, nodo: Nodo):
        self._nodo_objetivo = nodo
        print("Estado Objetivo: ", self._nodo_objetivo)

    # Operaciones con Aristas
    def agregar_arista(self, nodo_origen: Nodo, nodo_destino: Nodo, distancia: float) -> Grafo:
        print("Agregando arista:", nodo_origen, nodo_destino, distancia)
        self._grafo.agregar_arista(nodo_origen, nodo_destino, distancia)
        return self._grafo

    def eliminar_arista(self, nodo_origen: Nodo, nodo_destino: Nodo) -> Grafo:
        self._grafo.eliminar_arista(nodo_origen, nodo_destino)
        return self._grafo

    def obtener_aristas_nodo(self, nodo: Nodo) -> set[Arista] | None:
        return self._grafo.obtener_aristas_nodo(nodo)

    # Operaciones del Algoritmo
    def comenzar_algoritmo(self) -> RecorridoAlgoritmo:
        if self._nodo_inicio == None or self._nodo_objetivo == None:
            print("No se establecieron los nodos de inicio y/o objetivo")
            return

        self._recorrido_algoritmo = RecorridoAlgoritmo(self._grafo, self._nodo_inicio, self._nodo_objetivo)
        return self._recorrido_algoritmo

    def avanzar_paso(self) -> RecorridoAlgoritmo:
        self._recorrido_algoritmo.avanzar_paso()
        return self._recorrido_algoritmo

    def retroceder_paso(self) -> RecorridoAlgoritmo:
        self._recorrido_algoritmo.retroceder_paso()
        return self._recorrido_algoritmo
