class ResultadosAlgoritmo:
    def __init__(self, recorrido):
        if recorrido is None:
            self._asignar_valores_por_defecto()
        else:
            self.nro_paso = recorrido.obtener_paso_actual().nro
            self.objetivo_alcanzado = recorrido.verificar_objetivo_alcanzado()
            self.ruta = recorrido.obtener_ruta() or []
            self.costo_total = recorrido.obtener_costo_ruta() or 0.0
            self.cantidad_nodos_explorados = recorrido.obtener_cantidad_nodos_explorados() or 0
            self.tiempo_total = recorrido.tiempo_total or 0.0

    def _asignar_valores_por_defecto(self):
        self.nro_paso = 0
        self.objetivo_alcanzado = False
        self.ruta = []
        self.costo_total = 0.0
        self.cantidad_nodos_explorados = 0
        self.tiempo_total = 0.0

    def to_dict(self):
        return {
            "nro_paso": self.nro_paso,
            "objetivo_alcanzado": self.objetivo_alcanzado,
            "ruta": self.ruta,
            "costo_total": self.costo_total,
            "cantidad_nodos_explorados": self.cantidad_nodos_explorados,
            "tiempo_total": self.tiempo_total,
        }

    def __str__(self):
        ruta_str = " -> ".join(n.nombre for n in self.ruta) if self.ruta else "Sin ruta"
        return (
            f"[Resultados Algoritmo]\n"
            f" Paso actual: {self.nro_paso}\n"
            f" Objetivo alcanzado: {'Sí' if self.objetivo_alcanzado else 'No'}\n"
            f" Ruta: {ruta_str}\n"
            f" Costo total: {self.costo_total:.2f}\n"
            f" Nodos explorados: {self.cantidad_nodos_explorados}\n"
            f" Tiempo total: {self.tiempo_total:.4f} segundos"
        )
