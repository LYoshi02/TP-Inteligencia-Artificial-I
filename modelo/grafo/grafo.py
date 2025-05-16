from modelo.grafo.arista import Arista
from modelo.grafo.nodo import Nodo


class Grafo:
    def __init__(self):
        # Este atributo es un diccionario donde las llaves son los nodos y los
        # valores son las aristas que lo conectan con otros nodos.
        self._nodos: dict[Nodo, set[Arista]] = {}

    # Devuelve el nodo que tiene el nombre recibido, si es que existe
    def obtener_nodo(self, nombre: str) -> Nodo | None:
        for key in self._nodos.keys():
            if key.nombre == nombre:
                return key
        print(f"obtener_nodo - No se encontró el nodo con el nombre '{nombre}'")
        return None

    #Retorna todos los nodos registrados en el grafo
    def obtener_nodos(self) -> list[Nodo]:
        return list(self._nodos.keys())

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

        nueva_arista = Arista(nodo_origen, nodo_destino)
        if nueva_arista in self._nodos[nodo_origen]:
            # Elimina la arista existente
            self._nodos[nodo_origen].discard(nueva_arista)
            self._nodos[nodo_destino].discard(nueva_arista)

        # Agrega una nueva arista al diccionario
        nueva_arista.distancia = distancia
        self._nodos[nodo_origen].add(nueva_arista)
        self._nodos[nodo_destino].add(nueva_arista)

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

    def to_dict(self):
        nodos_data = [nodo.to_dict() for nodo in self._nodos.keys()]

        aristas_guardadas = set()
        aristas_data = []
        for nodo, aristas in self._nodos.items():
            for arista in aristas:
                clave = frozenset([arista.nodo_origen.nombre, arista.nodo_destino.nombre])
                if clave not in aristas_guardadas:
                    aristas_data.append(arista.to_dict())
                    aristas_guardadas.add(clave)

        return {
            "nodos": nodos_data,
            "aristas": aristas_data,
        }

    @staticmethod
    def from_dict(data: dict):
        if not isinstance(data, dict):
            raise Exception("El archivo no contiene un objeto JSON válido")
        elif not "nodos" in data or not "aristas" in data:
            raise Exception("El archivo no contiene un objeto JSON válido")

        grafo = Grafo()
        nombre_a_nodo = {}

        for nodo_data in data["nodos"]:
            nodo = Nodo.from_dict(nodo_data)
            grafo.agregar_nodo(nodo)
            nombre_a_nodo[nodo.nombre] = nodo

        for arista_data in data["aristas"]:
            arista = Arista.from_dict(arista_data, nombre_a_nodo)
            grafo.agregar_arista(arista.nodo_origen, arista.nodo_destino, arista.distancia)

        return grafo

    # Imprimir nodos y aristas del grafo
    def __str__(self):
        resultado = ""
        for nodo in self._nodos:
            resultado += f"Nodo: {nodo.nombre}\n"
            resultado += f"* Aristas: {list(dict.fromkeys(self._nodos.get(nodo)))}\n"
        return resultado
