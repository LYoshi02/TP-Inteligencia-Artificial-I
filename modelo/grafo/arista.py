from modelo.grafo.nodo import Nodo


class Arista:
    def __init__(self, nodo_origen: Nodo, nodo_destino: Nodo, costo: float = 0):
        self._nodo_origen = nodo_origen
        self._nodo_destino = nodo_destino
        self._costo = costo

    def obtener_nodo_opuesto(self, nodo: Nodo):
        if self._nodo_origen == nodo:
            return self._nodo_destino
        else:
            return self._nodo_origen

    @property
    def nodo_origen(self):
        return self._nodo_origen

    @property
    def nodo_destino(self):
        return self._nodo_destino

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, costo: float):
        self._costo = costo

    def to_dict(self) -> dict:
        return {
            "nodo_origen": self._nodo_origen.nombre,
            "nodo_destino": self._nodo_destino.nombre,
            "costo": self._costo
        }

    @staticmethod
    def from_dict(data: dict, nodos: dict[str, Nodo]) -> 'Arista':
        if not isinstance(data, dict):
            raise Exception("El archivo no contiene un objeto JSON válido")
        elif not "nodo_origen" in data or not "nodo_destino" in data:
            raise Exception("El archivo no contiene un objeto JSON válido")

        nodo_origen = nodos[data["nodo_origen"]]
        nodo_destino = nodos[data["nodo_destino"]]
        costo = data.get("costo", 0)
        return Arista(nodo_origen, nodo_destino, costo)

    def __eq__(self, arista):
        if isinstance(arista, Arista):
            return (self._nodo_origen == arista._nodo_origen and self._nodo_destino == arista._nodo_destino) or (
                    self._nodo_origen == arista._nodo_destino and self._nodo_destino == arista._nodo_origen)
        return False

    def __hash__(self):
        return hash(frozenset([self._nodo_origen, self._nodo_destino]))

    def __repr__(self):
        return f"{self._nodo_origen} --({self._costo})-- {self._nodo_destino}"
