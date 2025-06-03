from modelo.algoritmo.recorrido_algoritmo import RecorridoAlgoritmo

class ResultadosAlgoritmo:
    def __init__(self, recorrido: RecorridoAlgoritmo | None):
        if recorrido is None:
            self._asignar_valores_por_defecto()
        else:
            self._nro_paso: int = recorrido.obtener_paso_actual().nro
            self._objetivo_alcanzado: bool = recorrido.verificar_objetivo_alcanzado()
            self._ruta: list[str] = recorrido.obtener_ruta() or []
            self._costo_total: float = recorrido.obtener_costo_ruta() or 0.0
            self._cantidad_nodos_explorados: int = recorrido.obtener_cantidad_nodos_explorados() or 0
            self._tiempo_total: float = recorrido.tiempo_total or 0.0

    def _asignar_valores_por_defecto(self):
        self._nro_paso: int = 0
        self._objetivo_alcanzado: bool = False
        self._ruta: list[str] = []
        self._costo_total: float = 0.0
        self._cantidad_nodos_explorados: int = 0
        self._tiempo_total: float = 0.0

    @property
    def nro_paso(self):
        return self._nro_paso

    @property
    def objetivo_alcanzado(self):
        return self._objetivo_alcanzado

    @property
    def ruta(self):
        return self._ruta

    @property
    def costo_total(self):
        return self._costo_total

    @property
    def cantidad_nodos_explorados(self):
        return self._cantidad_nodos_explorados

    @property
    def tiempo_total(self):
        return self._tiempo_total

    def __str__(self):
        ruta_str = " -> ".join(n for n in self._ruta) if self._ruta else "Sin ruta"
        return (
            f"[Resultados Algoritmo]\n"
            f" Paso actual: {self.nro_paso}\n"
            f" Objetivo alcanzado: {'Sí' if self.objetivo_alcanzado else 'No'}\n"
            f" Ruta: {ruta_str}\n"
            f" Costo total: {self.costo_total:.2f}\n"
            f" Nodos explorados: {self.cantidad_nodos_explorados}\n"
            f" Tiempo total: {self.tiempo_total:.4f} segundos"
        )
