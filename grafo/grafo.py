from grafo.arista import Arista
from grafo.nodo import Nodo


class Grafo:
    def __init__(self):
        # Este atributo es un diccionario donde las llaves son los nodos y los
        # valores son las aristas que lo conectan con otros nodos.
        self._nodos: dict[Nodo, set[Arista]] = {}

    # Devuelve el nodo que tiene el nombre recibido, si es que existe
    def obtener_nodo(self, nombre: str) -> Nodo | None:
        for key in self._nodos.keys():
            if key == Nodo(nombre):
                return key
        print(f"obtener_nodo - No se encontró el nodo con el nombre '{nombre}'")
        return None

    # Agrega un nuevo nodo al diccionario
    def agregar_nodo(self, nodo: Nodo):
        if nodo in self._nodos:
            print(f"agregar_nodo - El nodo '{nodo.nombre}' ya existe en el diccionario")
            return

        self._nodos[nodo] = set()

    # Elimina el nodo del diccionario y elimina todas las aristas de otros nodos
    # que conecten con el nodo que se quiere eliminar
    def eliminar_nodo(self, nodo_eliminar: Nodo):
        if nodo_eliminar not in self._nodos:
            print(
                f"eliminar_nodo - El nodo '{nodo_eliminar.nombre}' que se quiere eliminar no existe en el diccionario")
            return

        self._nodos.pop(nodo_eliminar)
        for (nodo, aristas) in self._nodos.items():
            arista_eliminar = Arista(nodo, nodo_eliminar)
            if arista_eliminar in aristas:
                aristas.remove(arista_eliminar)

    def obtener_aristas_nodo(self, nodo: Nodo) -> set[Arista] | None:
        if nodo not in self._nodos:
            print(f"obtener_aristas_nodo - El nodo '{nodo.nombre}' no se encuentra en el grafo")
            return None

        return self._nodos.get(nodo)

    # Agrega una nueva arista a ambos nodos dentro del diccionario
    def agregar_arista(self, nodo_origen: Nodo, nodo_destino: Nodo, distancia: float):
        if nodo_origen not in self._nodos:
            print(f"agregar_arista - El nodo '{nodo_origen.nombre}' no se encuentra en el grafo")
            return
        elif nodo_destino not in self._nodos:
            print(f"agregar_arista - El nodo '{nodo_destino.nombre}' no se encuentra en el grafo")
            return
        elif nodo_origen == nodo_destino:
            print(f"agregar_arista - Los nodos son iguales")
            return

        self._nodos[nodo_origen].add(Arista(nodo_origen, nodo_destino, distancia))
        self._nodos[nodo_destino].add(Arista(nodo_destino, nodo_origen, distancia))

    # Verifica si la arista que se quiere eliminar existe y la elimina de ambos nodos
    # dentro del diccionario
    def eliminar_arista(self, nodo_origen: Nodo, nodo_destino: Nodo):
        if nodo_origen not in self._nodos:
            print(f"eliminar_arista - El nodo '{nodo_origen.nombre}' no se encuentra en el grafo")
            return
        elif nodo_destino not in self._nodos:
            print(f"eliminar_arista - El nodo '{nodo_destino.nombre}' no se encuentra en el grafo")
            return

        arista_eliminar = Arista(nodo_origen, nodo_destino)
        if arista_eliminar in self._nodos[nodo_origen]:
            self._nodos[nodo_origen].remove(Arista(nodo_origen, nodo_destino))
            self._nodos[nodo_destino].remove(Arista(nodo_destino, nodo_origen))
        else:
            print(
                f"eliminar_arista - No existe la arista '{nodo_origen.nombre}---{nodo_destino.nombre}' que se quiere eliminar")

    # Imprimir nodos y aristas del grafo
    def __str__(self):
        resultado = ""
        for nodo in self._nodos:
            resultado += f"Nodo: {nodo.nombre}\n"
            resultado += f"* Aristas: {list(dict.fromkeys(self._nodos.get(nodo)))}\n"
        return resultado
