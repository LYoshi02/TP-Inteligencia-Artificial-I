class Nodo:
    def __init__(self, nombre: str, costo: float = float("inf"), heuristica: float = 0):
        self._nombre = nombre
        # g: costo desde el nodo inicial hasta este nodo
        self._costo: float = costo
        # h: costo aproximado desde este nodo hasta el nodo objetivo
        self._heuristica: float = heuristica
        # f: funcion heuristica
        # self._f: float = self.costo + heuristica
        # Nodo padre para construir el camino hacia el nodo objetivo
        self.nodo_padre: Nodo | None = None

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, costo: float):
        self._costo = costo

    @property
    def heuristica(self):
        return self._heuristica

    @heuristica.setter
    def heuristica(self, heuristica: float):
        self._heuristica = heuristica

    @property
    def f(self):
        return self._costo + self._heuristica

    def __eq__(self, nodo):
        if isinstance(nodo, Nodo):
            return self.nombre == nodo.nombre
        return False

    # Tuve que poner esto como criterio de desempate en la cola de prioridad
    def __lt__(self, nodo):
        return self.nombre < nodo.nombre

    def __hash__(self):
        return hash(self.nombre)

    def __str__(self):
        return f"Nodo(nombre={self.nombre}, g={self.costo}, h={self.heuristica})"

    def __repr__(self):
        return f"Nodo(nombre={self.nombre}, g={self.costo}, h={self.heuristica})"
