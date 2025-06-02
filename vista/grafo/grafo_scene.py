from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QInputDialog

from modelo.algoritmo.recorrido_algoritmo import RecorridoAlgoritmo
from controlador.controlador import Controlador
from modelo.grafo.arista import Arista
from modelo.grafo.grafo import Grafo
from modelo.grafo.nodo import Nodo
from vista.grafo.arista_grafico import AristaGrafico
from vista.grafo.nodo_grafico import NodoGrafico


class GrafoScene(QGraphicsScene):
    def __init__(self, controlador: Controlador):
        super().__init__()
        self.controlador = controlador
        self.nodo_para_conectar: NodoGrafico | None = None

    def graficar_grafo(self, grafo: Grafo, recorrido_algoritmo: RecorridoAlgoritmo = None):
        self.__limpiar_grafo()

        # Graficar nodos
        nodos_graficados: dict[Nodo, NodoGrafico] = {}
        nodos = grafo.obtener_nodos()
        for nodo in nodos:
            nodo_ui = self.__graficar_nodo(nodo)
            nodos_graficados[nodo] = nodo_ui

        # Graficar aristas
        aristas_graficadas: dict[Arista, AristaGrafico] = {}
        for nodo in nodos:
            aristas_nodo = self.controlador.obtener_aristas_nodo(nodo)
            for arista in aristas_nodo:
                if not arista in aristas_graficadas:
                    arista_ui = self.__graficar_arista(nodos_graficados[nodo], nodos_graficados[arista.obtener_nodo_opuesto(nodo)], arista.costo)
                    aristas_graficadas[arista] = arista_ui
                    nodos_graficados[nodo].agregar_arista_conectada(arista_ui)
                else:
                    nodos_graficados[nodo].agregar_arista_conectada(aristas_graficadas[arista])

        # Graficar recorrido del algoritmo
        if recorrido_algoritmo:
            self.__graficar_recorrido_algoritmo(recorrido_algoritmo, nodos_graficados, aristas_graficadas)

    def __graficar_recorrido_algoritmo(self, recorrido_algoritmo: RecorridoAlgoritmo, nodos_graficados: dict[Nodo, NodoGrafico],
                                     aristas_graficadas: dict[Arista, AristaGrafico]):
        paso_actual = recorrido_algoritmo.obtener_paso_actual()
        if not paso_actual:
            return

        print(str(paso_actual))
        # Pintar nodos cerrados
        for nodo, nodo_ui in nodos_graficados.items():
            if nodo in paso_actual.nodos_cerrados:
                print("Nodo cerrado: " + str(nodo))
                nodo_ui.aplicar_tema("cerrado")
        # Pintar nodos abiertos
        for i, nodo in enumerate(paso_actual.nodos_abiertos):
            print("Nodo abierto: " + str(nodo))
            nodo_abierto_ui = nodos_graficados[nodo]
            if i == 0:
                nodo_abierto_ui.aplicar_tema("abierto_mejor")
            else:
                nodo_abierto_ui.aplicar_tema("abierto")
        # Pintar nodos del camino actual
        for nodo, nodo_ui in nodos_graficados.items():
            if nodo in paso_actual.camino:
                print("Nodo camino: " + str(nodo))
                nodo_ui.aplicar_tema("camino")
        # Pintar nodo inicial
        nodo_inicio_ui = nodos_graficados[recorrido_algoritmo.nodo_inicio]
        print("Nodo inicio: " + str(recorrido_algoritmo.nodo_inicio))
        if nodo_inicio_ui:
            nodo_inicio_ui.aplicar_tema("inicio")
        nodo_objetivo_ui = nodos_graficados[recorrido_algoritmo.nodo_objetivo]
        if nodo_objetivo_ui:
            nodo_objetivo_ui.aplicar_tema("objetivo")

        # Pintar nodo actual
        if paso_actual.nodo_actual:
            nodo_actual_ui = nodos_graficados[paso_actual.nodo_actual]
            print("Nodo actual: " + str(paso_actual.nodo_actual))
            if nodo_actual_ui.nombre == recorrido_algoritmo.nodo_objetivo.nombre:
                nodo_actual_ui.aplicar_tema("objetivo")
            elif nodo_actual_ui:
                nodo_actual_ui.aplicar_tema("actual")

        # Pintar camino recorrido
        i = 1
        while i < len(paso_actual.camino):
            arista = Arista(paso_actual.camino[i], paso_actual.camino[i-1])
            print("Pintar arista: " + str(arista))
            arista_ui = aristas_graficadas[arista]
            arista_ui.aplicar_tema("camino")
            i += 1

        print("----------------")

    def __limpiar_grafo(self):
        for item in self.items():
            self.removeItem(item)
            # Elimina la instancia en memoria
            del item

    def __graficar_nodo(self, nodo: Nodo) -> NodoGrafico:
        nodo_ui = NodoGrafico(nodo)

        if self.nodo_para_conectar and nodo_ui == self.nodo_para_conectar:
            nodo_ui.aplicar_tema("seleccionado")
            nodo_ui.permitir_movimiento(True)

        self.addItem(nodo_ui)
        return nodo_ui

    def __graficar_arista(self, origen: NodoGrafico, destino: NodoGrafico, costo: float) -> AristaGrafico:
        print(f"Graficando arista ({origen.nombre}) con ({destino.nombre}) con costo {costo}")
        arista_ui = AristaGrafico(origen, destino, costo)
        self.addItem(arista_ui)
        return arista_ui

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, NodoGrafico)), None)

            if item is None:
                nombre, ok = QInputDialog.getText(None, "Nuevo Nodo", "Nombre del nodo:")
                if ok and nombre:
                    print(f"Nodo ({nombre}) creado en: ({pos.x():.2f}, {pos.y():.2f})")
                    #Se agrega el nodo al controlador
                    nuevo_grafo = self.controlador.agregar_nodo(nombre, pos.x(), pos.y())
                    self.graficar_grafo(nuevo_grafo)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, NodoGrafico)), None)

            if item:
                if self.nodo_para_conectar is None:
                    self.nodo_para_conectar = item
                    item.permitir_movimiento(True)
                    item.aplicar_tema("seleccionado")
                # Para deseleccionar nodo
                elif self.nodo_para_conectar == item:
                    self.deseleccionar_nodo_para_conectar()
                    item.permitir_movimiento(False)
                    item.aplicar_tema("default")
                elif item != self.nodo_para_conectar:
                    costo, ok = QInputDialog.getInt(None, "Costo de la arista", "Ingrese el costo:")
                    if ok:
                        # Se agrega la arista al controlador
                        nodo_origen = self.controlador.obtener_nodo(self.nodo_para_conectar.nombre)
                        nodo_destino = self.controlador.obtener_nodo(item.nombre)

                        print(f"Conectando ({self.nodo_para_conectar.nombre}) con ({item.nombre}) con costo {costo}")
                        if nodo_origen and nodo_destino:
                            nuevo_grafo = self.controlador.agregar_arista(nodo_origen, nodo_destino, costo)
                            self.graficar_grafo(nuevo_grafo)

    def eliminar_nodo(self, nodo: NodoGrafico):
        nuevo_grafo = self.controlador.eliminar_nodo(nodo.nombre, nodo.pos().x(), nodo.pos().y())
        if self.nodo_para_conectar == nodo:
            self.deseleccionar_nodo_para_conectar()
        self.graficar_grafo(nuevo_grafo)

    def eliminar_arista(self, nodo_origen: NodoGrafico, nodo_destino: NodoGrafico):
        nodo_origen = self.controlador.obtener_nodo(nodo_origen.nombre)
        nodo_destino = self.controlador.obtener_nodo(nodo_destino.nombre)
        grafo_actualizado = self.controlador.eliminar_arista(nodo_origen, nodo_destino)
        self.graficar_grafo(grafo_actualizado)

    def actualizar_costo_arista(self, nodo_origen: NodoGrafico, nodo_destino: NodoGrafico):
        costo, ok = QInputDialog.getInt(None, "Actualizar costo de arista", "Nuevo costo:")

        if ok:
            nodo_origen = self.controlador.obtener_nodo(nodo_origen.nombre)
            nodo_destino = self.controlador.obtener_nodo(nodo_destino.nombre)
            grafo_actualizado = self.controlador.actualizar_costo_arista(nodo_origen, nodo_destino, costo)

            self.graficar_grafo(grafo_actualizado)

    def deseleccionar_nodo_para_conectar(self):
        self.nodo_para_conectar = None

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)

        # Verifica si algún nodo fue movido y actualiza sus coordenadas en el grafo
        for item in self.selectedItems():
            if isinstance(item, NodoGrafico):
                nuevo_x = item.scenePos().x()
                nuevo_y = item.scenePos().y()
                print(f"Nodo {item.nombre} movido a ({nuevo_x:.2f}, {nuevo_y:.2f})")

                grafo = self.controlador.actualizar_nodo(item.nombre, nuevo_x, nuevo_y)
                self.graficar_grafo(grafo)