class Nodo:
    def __init__(self, nombre: str, x: float, y: float, costo_desde_inicio: float = float("inf"), heuristica: float = 0):
        self._nombre = nombre
        # g: costo desde el nodo inicial hasta este nodo
        self._costo_desde_inicio: float = costo_desde_inicio
        # h: costo aproximado desde este nodo hasta el nodo objetivo
        self._heuristica: float = heuristica
        # Nodo padre para construir el camino hacia el nodo objetivo
        self.nodo_padre: Nodo | None = None
        # Coordenadas del Nodo
        self._x: float = x
        self._y: float = y

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_desde_inicio(self):
        return self._costo_desde_inicio

    @costo_desde_inicio.setter
    def costo_desde_inicio(self, costo: float):
        self._costo_desde_inicio = costo

    @property
    def heuristica(self):
        return self._heuristica

    @heuristica.setter
    def heuristica(self, heuristica: float):
        self._heuristica = heuristica

    @property
    def costo_total(self):
        return self._costo_desde_inicio + self._heuristica

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
        #return f"Nodo(nombre={self.nombre}, g={self.costo_desde_inicio}, h={self.heuristica})"
        return f"Nodo nombre: {self.nombre}, posición: x: {self._x}, y: {self._y}"

    def __repr__(self):
        return f"Nodo(nombre={self.nombre}, g={self.costo_desde_inicio}, h={self.heuristica})"
