import copy
import time

from modelo.algoritmo.heuristica.heuristica import Heuristica
from modelo.algoritmo.paso import Paso
from modelo.cola.cola_prioridad import ColaPrioridad
from modelo.grafo.grafo import Grafo
from modelo.grafo.nodo import Nodo

NRO_PASO_INICIAL: int = 0


class RecorridoAlgoritmo:
    def __init__(self, grafo: Grafo, nodo_inicio: Nodo, nodo_objetivo: Nodo, heuristica: Heuristica):
        self.__calcular_heuristicas(grafo, nodo_objetivo, heuristica)

        self._nro_paso_actual: int = NRO_PASO_INICIAL
        self._grafo: Grafo = copy.deepcopy(grafo)
        self._nodo_inicio: Nodo = nodo_inicio
        self._nodo_inicio.costo_desde_inicio = 0
        self._nodo_objetivo: Nodo = nodo_objetivo

        nodos_abiertos = ColaPrioridad()
        nodos_abiertos.encolar_elemento(nodo_inicio, nodo_inicio.costo_total)
        nodos_cerrados = set()
        paso_inicial = Paso(self._nro_paso_actual, nodo_inicio, self._grafo.obtener_aristas_nodo(nodo_inicio),
                            nodos_abiertos, nodos_cerrados, self.__construir_camino(nodo_inicio), False)
        self._pasos: dict[int, Paso] = {self._nro_paso_actual: paso_inicial}
        self._tiempos_por_paso: dict[int, float] = {}

    def __calcular_heuristicas(self, grafo: Grafo, nodo_objetivo: Nodo, heuristica: Heuristica) -> None:
        for nodo in grafo.obtener_nodos():
            valor_heuristica = heuristica.calcular(nodo.x, nodo.y, nodo_objetivo.x, nodo_objetivo.y)
            nodo.heuristica = valor_heuristica
            print(f"Heuristica Nodo {nodo.nombre}: {valor_heuristica:.2f}")

    def obtener_paso_actual(self) -> Paso:
        return self._pasos[self._nro_paso_actual]

    def retroceder_paso(self) -> None:
        if self._nro_paso_actual > NRO_PASO_INICIAL:
            self._nro_paso_actual -= 1

    def avanzar_paso(self) -> None:
        self._nro_paso_actual += 1

        paso_anterior: Paso = self.__obtener_paso_anterior()
        if paso_anterior.fin:
            # Se retrocede 1 paso, ya que la búsqueda finalizó y el paso actual no se procesa
            self._nro_paso_actual -= 1
            print("La busqueda ya finalizó")
            return

        # Solo se aplica el algoritmo si no se calculó anteriormente el siguiente paso
        if not self._nro_paso_actual in self._pasos:
            inicio = time.perf_counter()
            nuevo_paso = self.__aplicar_algoritmo(paso_anterior)
            fin = time.perf_counter()

            self.__agregar_paso(nuevo_paso)
            self._tiempos_por_paso[self._nro_paso_actual] = fin-inicio

    def ir_al_paso_inicial(self):
        while self.obtener_paso_actual().nro != NRO_PASO_INICIAL:
            self.retroceder_paso()

    def ir_a_ultimo_paso(self) -> None:
        while not self.obtener_paso_actual().fin:
            self.avanzar_paso()

    def __aplicar_algoritmo(self, paso_anterior: Paso) -> Paso:
        nuevo_paso: Paso
        fin_busqueda = False
        # Nodos aun no evaluados priorizados por costo
        cola_prioridad_abiertos: ColaPrioridad[Nodo] = copy.deepcopy(paso_anterior.nodos_abiertos)
        # Nodos ya evaluados
        conjunto_cerrados: set[Nodo] = copy.deepcopy(paso_anterior.nodos_cerrados)

        if cola_prioridad_abiertos.vacio():
            fin_busqueda = True
            nuevo_paso = self.__generar_nuevo_paso(None, cola_prioridad_abiertos, conjunto_cerrados,
                                                   fin_busqueda)
            return nuevo_paso

        nodo_actual = copy.deepcopy(cola_prioridad_abiertos.desencolar_elemento())
        if nodo_actual == self._nodo_objetivo:
            fin_busqueda = True
            nuevo_paso = self.__generar_nuevo_paso(nodo_actual, cola_prioridad_abiertos, conjunto_cerrados, fin_busqueda)
            return nuevo_paso

        conjunto_cerrados.add(nodo_actual)

        aristas_nodo_actual = self._grafo.obtener_aristas_nodo(nodo_actual)
        for arista in aristas_nodo_actual:
            nodo_adyacente: Nodo = arista.obtener_nodo_opuesto(nodo_actual)
            # Saltear nodo ya evaluado
            if nodo_adyacente in conjunto_cerrados:
                continue

            costo_tentativo = nodo_actual.costo_desde_inicio + arista.costo

            if not cola_prioridad_abiertos.tiene_elemento(nodo_adyacente):
                # Actualizo la info del nodo adyacente
                nodo_adyacente.costo_desde_inicio = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                cola_prioridad_abiertos.encolar_elemento(nodo_adyacente, nodo_adyacente.costo_total)
            elif costo_tentativo < nodo_adyacente.costo_desde_inicio:
                # Actualizo la info del nodo adyacente
                nodo_adyacente.costo_desde_inicio = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                # Se actualiza costo del nodo adyacente en la cola de prioridad
                cola_prioridad_abiertos.encolar_elemento(nodo_adyacente, nodo_adyacente.costo_total)
                continue

        nuevo_paso = self.__generar_nuevo_paso(nodo_actual, cola_prioridad_abiertos, conjunto_cerrados, fin_busqueda)
        return nuevo_paso

    def __generar_nuevo_paso(self, nodo_actual: Nodo | None, nodos_abiertos: ColaPrioridad[Nodo],
                             nodos_cerrados: set[Nodo], fin_busqueda: bool) -> Paso:
        aristas_nodo_actual = set()
        camino_busqueda = []
        if nodo_actual:
            aristas_nodo_actual = copy.deepcopy(self._grafo.obtener_aristas_nodo(nodo_actual))
            camino_busqueda = copy.deepcopy(self.__construir_camino(nodo_actual))

        nuevo_paso = Paso(self._nro_paso_actual, nodo_actual, aristas_nodo_actual, nodos_abiertos,
                          nodos_cerrados, camino_busqueda, fin_busqueda)
        return nuevo_paso

    def __obtener_paso_anterior(self) -> Paso:
        if self._nro_paso_actual == NRO_PASO_INICIAL:
            return self._pasos[self._nro_paso_actual]
        else:
            return self._pasos[self._nro_paso_actual - 1]

    def __agregar_paso(self, paso: Paso):
        self._pasos[self._nro_paso_actual] = paso

    def __construir_camino(self, nodo_objetivo: Nodo) -> list[Nodo]:
        nodos_camino = []
        nodo_actual = nodo_objetivo
        while nodo_actual is not None:
            nodos_camino.append(nodo_actual)
            nodo_actual = nodo_actual.nodo_padre

        return nodos_camino[::-1]

    #Resultados del recorrido
    def obtener_ruta(self) -> list[str]:
        paso_actual = self.obtener_paso_actual()
        return [nodo.nombre for nodo in paso_actual.camino] if paso_actual.camino else []

    def obtener_costo_ruta(self) -> float:
        paso_actual = self.obtener_paso_actual()
        if not paso_actual.camino:
            return float('inf')
        costo = getattr(paso_actual.camino[-1], 'costo_desde_inicio', float('inf'))
        return float(costo) if costo is not None else float('inf')

    def obtener_cantidad_nodos_explorados(self) -> int:
        return len(self.obtener_paso_actual().nodos_cerrados)

    def verificar_objetivo_alcanzado(self) -> bool:
        paso_actual = self.obtener_paso_actual()
        return (paso_actual.fin and
                bool(paso_actual.camino) and
                paso_actual.camino[-1].nombre == self._nodo_objetivo.nombre)

    @property
    def grafo(self):
        return self._grafo

    @property
    def nodo_inicio(self):
        return self._nodo_inicio

    @property
    def nodo_objetivo(self):
        return self._nodo_objetivo

    @property
    def tiempo_total(self) -> float:
        return sum(
            tiempo for paso, tiempo in self._tiempos_por_paso.items()
            if paso <= self._nro_paso_actual
        )