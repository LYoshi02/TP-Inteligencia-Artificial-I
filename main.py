from algoritmo import a_estrella2
from grafo.grafo import Grafo
from grafo.nodo import Nodo


def main():
    grafo = generar_grafo()
    # print(grafo)

    nodo_inicio: Nodo = grafo.obtener_nodo("S")
    nodo_objetivo: Nodo = grafo.obtener_nodo("E")

    print(a_estrella2(grafo, nodo_inicio, nodo_objetivo))


def generar_grafo() -> Grafo:
    # Creacion de nodos
    nodo_S: Nodo = Nodo("S", heuristica=10)
    nodo_A: Nodo = Nodo("A", heuristica=9)
    nodo_B: Nodo = Nodo("B", heuristica=7)
    nodo_D: Nodo = Nodo("D", heuristica=8)
    nodo_H: Nodo = Nodo("H", heuristica=6)
    nodo_F: Nodo = Nodo("F", heuristica=6)
    nodo_G: Nodo = Nodo("G", heuristica=3)
    nodo_E: Nodo = Nodo("E", heuristica=0)

    # Carga de los nodos al grafo
    grafo = Grafo()
    grafo.agregar_nodo(nodo_S)
    grafo.agregar_nodo(nodo_A)
    grafo.agregar_nodo(nodo_B)
    grafo.agregar_nodo(nodo_D)
    grafo.agregar_nodo(nodo_H)
    grafo.agregar_nodo(nodo_F)
    grafo.agregar_nodo(nodo_G)
    grafo.agregar_nodo(nodo_E)

    # Agrega las aristas que unen a los nodos
    grafo.agregar_arista(nodo_S, nodo_A, 7)
    grafo.agregar_arista(nodo_S, nodo_B, 2)

    grafo.agregar_arista(nodo_A, nodo_B, 3)
    grafo.agregar_arista(nodo_A, nodo_D, 4)
    grafo.agregar_arista(nodo_A, nodo_S, 7)

    grafo.agregar_arista(nodo_B, nodo_A, 3)
    grafo.agregar_arista(nodo_B, nodo_D, 4)
    grafo.agregar_arista(nodo_B, nodo_H, 1)
    grafo.agregar_arista(nodo_B, nodo_S, 2)

    grafo.agregar_arista(nodo_D, nodo_A, 4)
    grafo.agregar_arista(nodo_D, nodo_B, 4)
    grafo.agregar_arista(nodo_D, nodo_F, 5)

    grafo.agregar_arista(nodo_H, nodo_B, 1)
    grafo.agregar_arista(nodo_H, nodo_F, 3)
    grafo.agregar_arista(nodo_H, nodo_G, 2)

    grafo.agregar_arista(nodo_F, nodo_D, 5)
    grafo.agregar_arista(nodo_F, nodo_H, 3)

    grafo.agregar_arista(nodo_G, nodo_H, 2)
    grafo.agregar_arista(nodo_G, nodo_E, 2)

    # grafo.eliminar_nodo(nodo_E)
    # grafo.eliminar_arista(nodo_A, nodo_E)

    return grafo


if __name__ == "__main__":
    main()
