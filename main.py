import sys
from PyQt6.QtWidgets import QMainWindow, QApplication

from vista import vista
from algoritmo import a_estrella
from modelo.grafo.grafo import Grafo
from modelo.grafo.nodo import Nodo

from vista.vista import Vista


class main(QMainWindow, vista.Ui_MainWindow):

    def ejecutar_algoritmo(self):
        grafo = generar_grafo()
        nodo_inicio: Nodo = grafo.obtener_nodo("S")
        nodo_objetivo: Nodo = grafo.obtener_nodo("E")
        resultado = a_estrella(grafo, nodo_inicio, nodo_objetivo)
        print("Resultado del algoritmo A*:", resultado)


def generar_grafo() -> Grafo:
    nodo_S: Nodo = Nodo("S", heuristica=10)
    nodo_A: Nodo = Nodo("A", heuristica=9)
    nodo_B: Nodo = Nodo("B", heuristica=7)
    nodo_D: Nodo = Nodo("D", heuristica=8)
    nodo_H: Nodo = Nodo("H", heuristica=6)
    nodo_F: Nodo = Nodo("F", heuristica=6)
    nodo_G: Nodo = Nodo("G", heuristica=3)
    nodo_E: Nodo = Nodo("E", heuristica=0)

    grafo = Grafo()
    for nodo in [nodo_S, nodo_A, nodo_B, nodo_D, nodo_H, nodo_F, nodo_G, nodo_E]:
        grafo.agregar_nodo(nodo)

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
    app = QApplication(sys.argv)
    with open("vista/styles/style.qss", "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window = Vista()

    # Mostramos la ventana
    window.show()

    # Ejecutamos la aplicación
    sys.exit(app.exec())

