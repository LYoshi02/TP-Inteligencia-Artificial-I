from cola.cola_prioridad import ColaPrioridad
from grafo.arista import Arista
from grafo.nodo import Nodo


class Paso:
    def __init__(self, nro_paso: int, nodo_actual: Nodo, aristas_nodo_actual: set[Arista],
                 nodos_abiertos: ColaPrioridad[Nodo], nodos_cerrados: set[Nodo], camino: list[Nodo],
                 fin: bool = False):
        self._nro: int = nro_paso
        self._nodo_actual: Nodo = nodo_actual
        self._aristas_nodo_actual: set[Arista] = aristas_nodo_actual
        self._nodos_abiertos: ColaPrioridad[Nodo] = nodos_abiertos
        self._nodos_cerrados: set[Nodo] = nodos_cerrados
        self._camino: list[Nodo] = camino
        self._fin: bool = fin

    @property
    def nro(self):
        return self._nro

    @property
    def nodo_actual(self):
        return self._nodo_actual

    @property
    def aristas_nodo_actual(self):
        return self._aristas_nodo_actual

    @property
    def nodos_abiertos(self):
        return self._nodos_abiertos

    @property
    def nodos_cerrados(self):
        return self._nodos_cerrados

    @property
    def camino(self):
        return self._camino

    @property
    def fin(self):
        return self._fin

    def __imprimir_camino(self) -> str:
        resultado = ""
        for nodo in self._camino:
            if nodo.nodo_padre is None:
                resultado += f"{nodo.nombre}"
            else:
                resultado += f" -> {nodo.nombre}"
        return resultado

    def __str__(self):
        resultado = ""
        resultado += f"Paso: {self._nro}\n"
        resultado += f"Nodo Actual: {self._nodo_actual}\n"
        resultado += f"Aristas: {self._aristas_nodo_actual}\n"
        resultado += f"Nodos Abiertos: {self._nodos_abiertos}\n"
        resultado += f"Nodos Cerrados: {self._nodos_cerrados}\n"
        resultado += f"Camino: {self.__imprimir_camino()}\n"
        resultado += f"Búsqueda finalizada: {self._fin}\n"
        return resultado
