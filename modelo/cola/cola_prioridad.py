import heapq
from typing import TypeVar, Generic

T = TypeVar('T')


class ColaPrioridad(Generic[T]):
    def __init__(self):
        # Lista usada como cola de prioridad
        self._elementos: list[list[float | int | T]] = []
        # Diccionario para facilitar el acceso a los elementos de la cola
        self._indice_entradas: dict[T, list[float | int | T]] = {}
        # Etiqueta para marcar un elemento como eliminado
        self._ELEMENTO_ELIMINADO = '<elemento-eliminado>'
        # Contador usado como criterio de desempate en caso de que haya prioridades de igual valor
        self._contador = 0

    def encolar_elemento(self, elemento: T, prioridad: float) -> None:
        if elemento in self._indice_entradas:
            self.eliminar_elemento(elemento)

        self._contador += 1
        entrada = [prioridad, self._contador, elemento]
        self._indice_entradas[elemento] = entrada
        heapq.heappush(self._elementos, entrada)

    def eliminar_elemento(self, elemento: T) -> None:
        # Marca una elemento como eliminado (sin sacarlo del heap todavía)
        entrada = self._indice_entradas.pop(elemento)
        entrada[-1] = self._ELEMENTO_ELIMINADO

    def desencolar_elemento(self) -> T | None:
        while self._elementos:
            prioridad, _, elemento = heapq.heappop(self._elementos)
            if elemento != self._ELEMENTO_ELIMINADO:
                del self._indice_entradas[elemento]
                return elemento

        print("No se puede desencolar el elemento: la cola está vacía.")

    def tiene_elemento(self, elemento: T) -> bool:
        entrada = self._indice_entradas.get(elemento)
        if entrada is None:
            return False
        return entrada[2] != self._ELEMENTO_ELIMINADO

    def vacio(self) -> bool:
        for _, _, elemento in self._elementos:
            if elemento != self._ELEMENTO_ELIMINADO:
                return False
        return True

    def __iter__(self):
        # Devuelve un iterador sobre los elementos válidos en orden de prioridad
        elementos_validos = [entrada for entrada in self._elementos if entrada[2] != self._ELEMENTO_ELIMINADO]
        for entrada in sorted(elementos_validos):  # Ordena por prioridad y contador
            yield entrada[2]

    def __str__(self) -> str:
        # Representación visual de la cola sin tareas eliminadas
        return str([entrada for entrada in self._elementos if entrada[2] != self._ELEMENTO_ELIMINADO])
