# TODO: borrar al terminar el proyecto
from modelo.cola.cola_prioridad import ColaPrioridad
from modelo.grafo.grafo import Grafo
from modelo.grafo.nodo import Nodo


def a_estrella(grafo: Grafo, nodo_inicio: Nodo, nodo_objetivo: Nodo):
    iteracion = 0

    cola_prioridad_abiertos: ColaPrioridad[Nodo] = ColaPrioridad()  # Nodos aun no evaluados priorizados por costo
    conjunto_cerrados: set[Nodo] = set()  # Nodos evaluados

    nodo_inicio.costo_desde_inicio = 0
    cola_prioridad_abiertos.encolar_elemento(nodo_inicio, nodo_inicio.costo_total)
    print("ENTRADAS:")
    print(f"Nodo inicio: {nodo_inicio}")
    print(f"Nodo objetivo: {nodo_objetivo}")
    print("%%%%%%%%%%%%%%")
    print("")

    while not cola_prioridad_abiertos.vacio():
        iteracion += 1
        print(f"ITERACION: {iteracion}")
        print(cola_prioridad_abiertos)
        nodo_actual = cola_prioridad_abiertos.desencolar_elemento()
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

            costo_tentativo = nodo_actual.costo_desde_inicio + arista.distancia

            if not cola_prioridad_abiertos.tiene_elemento(nodo_adyacente):
                # Actualizo la info del nodo adyacente
                nodo_adyacente.costo_desde_inicio = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                print("Se agrega al conjunto de abiertos")
                cola_prioridad_abiertos.encolar_elemento(nodo_adyacente, nodo_adyacente.costo_total)
                print(f"Nodo adyacente actualizado: {nodo_adyacente}")
                print("------------")
            elif costo_tentativo < nodo_adyacente.costo_desde_inicio:
                print(f"Resultado: Se encontró un mejor camino hacia {nodo_adyacente.nombre} "
                      f"({costo_tentativo} < anterior {nodo_adyacente.costo_desde_inicio})")
                # Actualizo la info del nodo adyacente
                nodo_adyacente.costo_desde_inicio = costo_tentativo
                nodo_adyacente.nodo_padre = nodo_actual
                # Se actualiza costo del nodo adyacente en la cola de prioridad
                cola_prioridad_abiertos.encolar_elemento(nodo_adyacente, nodo_adyacente.costo_total)
                print("------------")
                continue

        print("%%%%%%%%%%%%%%")
        print("")

    return "Resultado: camino no encontrado"


# HELPERS
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
