import json
import math
import random

from constantes.heuristicas import HEURISTICAS
from modelo.algoritmo.heuristica.distancia_manhattan import DistanciaManhattan
from modelo.algoritmo.heuristica.distancia_linea_recta import DistanciaLineaRecta
from modelo.algoritmo.heuristica.heuristica import Heuristica
from modelo.algoritmo.recorrido_algoritmo import RecorridoAlgoritmo
from modelo.grafo.arista import Arista
from modelo.grafo.grafo import Grafo
from modelo.grafo.nodo import Nodo


class Controlador:
    def __init__(self):
        self._grafo = Grafo()
        self._nodo_inicio: Nodo | None = None
        self._nodo_objetivo: Nodo | None = None
        self._procesos_busqueda: dict[str, RecorridoAlgoritmo] = {}

    # Operaciones con Grafo
    def obtener_grafo(self):
        return self._grafo

    def obtener_grafo_busqueda(self, heuristica: str):
        return self._procesos_busqueda[heuristica].grafo

    def restablecer_grafo(self):
        self._grafo = Grafo()
        self._nodo_inicio = None
        self._nodo_objetivo = None
        self._procesos_busqueda = {}

    def generar_grafo_aleatorio(self, cant_nodos: int, ancho: float, alto: float) -> Grafo:
        self.restablecer_grafo()
        centro_x = ancho / 6
        centro_y = alto / 6
        radio = min(ancho, alto) / 4
        for i in range(cant_nodos):
            nombre = chr(65 + i)
            angulo = 2 * math.pi * i / cant_nodos
            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)
            try:
                self.agregar_nodo(nombre, x, y)
            except Exception as e:
                print(f"Error al agregar nodo {nombre}: {e}")

        nodos_creados = list(self._grafo.obtener_nodos())

        for nodo_origen in nodos_creados:
            posibles_destinos = [n for n in nodos_creados if n != nodo_origen]

            if posibles_destinos:
                nodo_destino_1 = random.choice(posibles_destinos)
                peso_1 = random.randint(1, 99)
                try:
                    self.agregar_arista(nodo_origen, nodo_destino_1, peso_1)
                except Exception as e:
                    print(f"Error al agregar la primer arista de {nodo_origen} a {nodo_destino_1}: {e}")

                restantes = [n for n in posibles_destinos if n != nodo_destino_1]
                if restantes:
                    nodo_destino_2 = random.choice(restantes)
                    peso_2 = random.randint(1, 99)
                    try:
                        self.agregar_arista(nodo_origen, nodo_destino_2, peso_2)
                    except Exception as e:
                        print(f"Error al agregar la segunda arista de {nodo_origen} a {nodo_destino_2}: {e}")

        return self._grafo

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

    def actualizar_nodo(self, nombre: str, x: float, y: float) -> Grafo:
        nodo_actualizado: Nodo = Nodo(nombre, x, y)
        print("Actualizando nodo", nodo_actualizado)
        self._grafo.actualizar_nodo(nodo_actualizado)
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
    def comenzar_algoritmo(self, heuristica: str) -> RecorridoAlgoritmo:
        if self._nodo_inicio == None or self._nodo_objetivo == None:
            print("No se establecieron los nodos de inicio y/o objetivo")
            return

        tecnica_heuristica = self.__obtener_tecnica_heuristica(heuristica)
        self._procesos_busqueda[heuristica] = RecorridoAlgoritmo(self._grafo, self._nodo_inicio, self._nodo_objetivo, tecnica_heuristica)

        return self._procesos_busqueda[heuristica]

    def __obtener_tecnica_heuristica(self, heuristica: str):
        tecnica_heuristica: Heuristica
        if heuristica == HEURISTICAS.distancia_linea_recta.nombre:
            tecnica_heuristica = DistanciaLineaRecta()
        elif heuristica == HEURISTICAS.distancia_manhattan.nombre:
            tecnica_heuristica = DistanciaManhattan()
        # TODO: ver como manejar este caso
        else:
            tecnica_heuristica = DistanciaLineaRecta()

        return tecnica_heuristica

    def avanzar_paso(self, heuristica: str) -> RecorridoAlgoritmo:
        self._procesos_busqueda[heuristica].avanzar_paso()
        return self._procesos_busqueda[heuristica]

    def retroceder_paso(self, heuristica: str) -> RecorridoAlgoritmo:
        self._procesos_busqueda[heuristica].retroceder_paso()
        return self._procesos_busqueda[heuristica]

    # Operaciones de archivos
    def cargar_archivo_grafo(self, ruta_archivo: str) -> bool:
        if not ruta_archivo:
            return False

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                grafo = Grafo.from_dict(data)
                if not grafo:
                    return False

                self._grafo = grafo
                return True
        except Exception as e:
            return False

    def guardar_archivo_grafo(self, ruta_archivo: str) -> bool:
        if not ruta_archivo:
            return False

        if not hasattr(self, "_grafo") or self._grafo is None:
            return False

        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(self._grafo.to_dict(), archivo, indent=4)

            return True
        except Exception as e:
            return False