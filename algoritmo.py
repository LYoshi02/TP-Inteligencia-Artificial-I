import heapq

from grafo.grafo import Grafo
from grafo.nodo import Nodo


def a_estrella2(grafo: Grafo, nodo_inicio: Nodo, nodo_objetivo: Nodo):
    iteracion = 0
    nodo_inicio.costo = 0

    cola_prioridad_abiertos: list[tuple[float, Nodo]] = [(nodo_inicio.f, nodo_inicio)]
    conjunto_cerrados: set[Nodo] = set()  # Nodos evaluados

    print("ENTRADAS:")
    print(f"Nodo inicio: {nodo_inicio}")
    print(f"Nodo objetivo: {nodo_objetivo}")
    print("%%%%%%%%%%%%%%")
    print("")

    while cola_prioridad_abiertos:
        iteracion += 1
        print(f"ITERACION: {iteracion}")
        print(cola_prioridad_abiertos)
        _, nodo_actual = heapq.heappop(cola_prioridad_abiertos)
        print(f"Nodo actual: {nodo_actual}")

        if nodo_actual == nodo_objetivo:
            print("Resultado: nodo objetivo encontrado")
            return construir_camino(nodo_actual)

        conjunto_cerrados.add(nodo_actual)
        print(f"Accion: agregando nodo {nodo_actual.nombre} a conjunto de cerrados")
        print("------------")

        aristas_nodo_actual = grafo.obtener_aristas_nodo(nodo_actual)
        for arista in aristas_nodo_actual:
            nodo_adyacente: Nodo = arista.obtener_nodo_opuesto(nodo_actual)
            print(f"Nodo adyacente: {nodo_adyacente}")

            # Saltear nodo ya evaluado
            if nodo_adyacente in conjunto_cerrados:
                print("Resultado: el nodo ya fue evaluado")
                print("------------")
                continue

            costo_tentativo = nodo_actual.costo + arista._distancia

            if not nodo_adyacente in cola_prioridad_abiertos:
                # Actualizo la info del nodo vecino
                nodo_adyacente.costo = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                print("Se agrega al conjunto de abiertos")
                heapq.heappush(cola_prioridad_abiertos, (nodo_adyacente.f, nodo_adyacente))
                print(f"Nodo adyacente actualizado: {nodo_adyacente}")
                print("------------")
            elif costo_tentativo < nodo_adyacente.costo:
                print(f"Resultado: Se encontró un mejor camino {costo_tentativo} < {nodo_adyacente.costo}")
                # Actualizo la info del nodo vecino
                nodo_adyacente.costo = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                print("------------")
                continue

        print("%%%%%%%%%%%%%%")
        print("")

    return "Camino no encontrado"


def a_estrella(grafo: Grafo, nodo_inicio: Nodo, nodo_objetivo: Nodo):
    iteracion = 0
    nodo_inicio.costo = 0

    conjunto_abiertos: set[Nodo] = {nodo_inicio}  # Nodos a evaluar
    conjunto_cerrados: set[Nodo] = set()  # Nodos evaluados

    print("ENTRADAS:")
    print(f"Nodo inicio: {nodo_inicio}")
    print(f"Nodo objetivo: {nodo_objetivo}")
    print("%%%%%%%%%%%%%%")
    print("")

    while conjunto_abiertos:
        iteracion += 1
        print(f"ITERACION: {iteracion}")
        nodo_actual: Nodo = buscar_nodo_menor_costo(conjunto_abiertos)
        print(f"Nodo actual: {nodo_actual}")

        if nodo_actual == nodo_objetivo:
            print("Resultado: nodo objetivo encontrado")
            return construir_camino(nodo_actual)

        conjunto_abiertos.discard(nodo_actual)
        conjunto_cerrados.add(nodo_actual)
        print(f"Accion: agregando nodo {nodo_actual.nombre} a conjunto de cerrados")
        print("------------")

        aristas_nodo_actual = grafo.obtener_aristas_nodo(nodo_actual)
        for arista in aristas_nodo_actual:
            nodo_adyacente: Nodo = arista.obtener_nodo_opuesto(nodo_actual)
            print(f"Nodo adyacente: {nodo_adyacente}")

            # Saltear nodo ya evaluado
            if nodo_adyacente in conjunto_cerrados:
                print("Resultado: el nodo ya fue evaluado")
                print("------------")
                continue

            costo_tentativo = nodo_actual.costo + arista._distancia

            if not nodo_adyacente in conjunto_abiertos:
                # Actualizo la info del nodo vecino
                nodo_adyacente.nodo_padre = nodo_actual
                nodo_adyacente.costo = costo_tentativo
                print("Se agrega al conjunto de abiertos")
                conjunto_abiertos.add(nodo_adyacente)
                print(f"Nodo adyacente actualizado: {nodo_adyacente}")
                print("------------")
                conjunto_abiertos.add(nodo_adyacente)
            elif costo_tentativo < nodo_adyacente.costo:
                print(f"Resultado: Se encontró un mejor camino {costo_tentativo} < {nodo_adyacente.costo}")
                # Actualizo la info del nodo vecino
                nodo_adyacente.nodo_padre = nodo_actual
                nodo_adyacente.costo = costo_tentativo
                print("------------")
                continue

        print("%%%%%%%%%%%%%%")
        print("")

    return "Camino no encontrado"


# HELPERS
def buscar_nodo_menor_costo(conjunto_nodos: set[Nodo]) -> Nodo:
    nodo_menor_costo: Nodo = conjunto_nodos.pop()

    for nodo in conjunto_nodos:
        if nodo.f < nodo_menor_costo.f:
            nodo_menor_costo = nodo

    return nodo_menor_costo


def construir_camino(nodo_objetivo: Nodo) -> str:
    nodos_camino = []
    nodo_actual = nodo_objetivo
    resultado = ""

    while nodo_actual is not None:
        nodos_camino.append(nodo_actual)
        nodo_actual = nodo_actual.nodo_padre

    for nodo in nodos_camino[::-1]:
        if nodo.nodo_padre is None:
            resultado += f"{nodo.nombre}"
        else:
            resultado += f" -> {nodo.nombre}"

    return resultado
