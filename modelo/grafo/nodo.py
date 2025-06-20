class Nodo:
    def __init__(self, nombre: str, x: float, y: float, costo_desde_inicio: float = float("inf"), heuristica: float = 0):
        self._nombre = nombre
        # g: costo desde el nodo inicial hasta este nodo
        self._costo_desde_inicio: float = costo_desde_inicio
        # h: costo aproximado desde este nodo hasta el nodo objetivo
        self._heuristica: float = heuristica
        # Nodo padre para construir el camino hacia el nodo objetivo
        self._nodo_padre: Nodo | None = None
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
    def nodo_padre(self):
        return self._nodo_padre

    @nodo_padre.setter
    def nodo_padre(self, nodo: 'Nodo'):
        if isinstance(nodo, Nodo):
            self._nodo_padre = nodo
        else:
            raise ValueError("Debe ser una instancia de Nodo")

    @property
    def costo_total(self):
        return self._costo_desde_inicio + self._heuristica

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def to_dict(self) -> dict:
        return {
            "nombre": self._nombre,
            "x": self._x,
            "y": self._y,
        }

    @staticmethod
    def from_dict(data: dict) -> 'Nodo':
        if not isinstance(data, dict):
            raise Exception("El archivo no contiene un objeto JSON válido")
        elif not "nombre" in data or not "x" in data or not "y" in data:
            raise Exception("El archivo no contiene un objeto JSON válido")

        nombre = data["nombre"]
        x = data["x"]
        y = data["y"]
        return Nodo(nombre, x, y)

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
