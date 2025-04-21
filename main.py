from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QUrl
from PyQt6.QtQml import QQmlApplicationEngine

from algoritmo import a_estrella
from grafo.grafo import Grafo
from grafo.nodo import Nodo
from vista import vista
import sys


def main():
    #Vista - En proceso
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    vista.cargar_interfaz(engine, None)

    if not engine.rootObjects():
        print("Error al cargar la interfaz")
        sys.exit(-1)



    grafo = generar_grafo()
    nodo_inicio: Nodo = grafo.obtener_nodo("S")
    nodo_objetivo: Nodo = grafo.obtener_nodo("E")
    resultado = a_estrella(grafo, nodo_inicio, nodo_objetivo)
    print("Resultado del algoritmo A*:", resultado)

    sys.exit(app.exec())  # Cambié 'app.exec_()' por 'app.exec()' en PyQt6


def generar_grafo() -> Grafo:
    # Creación de nodos
    nodo_S: Nodo = Nodo("S", heuristica=10)
    nodo_A: Nodo = Nodo("A", heuristica=9)
    nodo_B: Nodo = Nodo("B", heuristica=7)
    nodo_D: Nodo = Nodo("D", heuristica=8)
    nodo_H: Nodo = Nodo("H", heuristica=6)
    nodo_F: Nodo = Nodo("F", heuristica=6)
    nodo_G: Nodo = Nodo("G", heuristica=3)
    nodo_E: Nodo = Nodo("E", heuristica=0)

    # Crear grafo y agregar nodos
    grafo = Grafo()
    for nodo in [nodo_S, nodo_A, nodo_B, nodo_D, nodo_H, nodo_F, nodo_G, nodo_E]:
        grafo.agregar_nodo(nodo)

    # Agregar aristas
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

    return grafo


if __name__ == "__main__":
    main()
