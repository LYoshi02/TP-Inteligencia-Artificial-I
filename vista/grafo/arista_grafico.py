import random
from typing import Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QFont, QColor
from PyQt6.QtWidgets import QGraphicsItemGroup, QGraphicsLineItem, QGraphicsTextItem, QMenu, QInputDialog

from vista.grafo.nodo_grafico import NodoGrafico

TemaArista = Literal["default", "camino"]

class AristaGrafico(QGraphicsItemGroup):
    def __init__(self, origen: NodoGrafico, destino: NodoGrafico, costo: float, parent=None):
        super().__init__(parent)

        self.origen: NodoGrafico = origen
        self.destino: NodoGrafico = destino


        # Crear la línea
        self.linea = QGraphicsLineItem()
        self.linea.setZValue(-1)

        # Crear el texto del costo
        self.texto = QGraphicsTextItem(str(costo))
        self.texto.setZValue(1)

        self.aplicar_tema("default")

        # Agregar elementos al grupo
        self.addToGroup(self.linea)
        self.addToGroup(self.texto)

        self.actualizar_posicion()

    def aplicar_tema(self, tema: TemaArista):
        match tema:
            case "default":
                self.linea.setPen(QPen(Qt.GlobalColor.black))
                self.texto.setDefaultTextColor(Qt.GlobalColor.black)
                self.texto.setFont(QFont("Arial", 10))
            case "camino":
                pen = QPen(QColor("#9B2226"))
                pen.setWidth(2)
                self.linea.setPen(pen)
                font = QFont("Arial", 10)
                font.setBold(True)
                self.texto.setFont(font)

    def actualizar_posicion(self):
        origen_pos = self.origen.scenePos()
        destino_pos = self.destino.scenePos()
        self.linea.setLine(origen_pos.x(), origen_pos.y(), destino_pos.x(), destino_pos.y())

        t = random.uniform(0.4, 0.6)
        x = origen_pos.x() + t * (destino_pos.x() - origen_pos.x())
        y = origen_pos.y() + t * (destino_pos.y() - origen_pos.y())

        self.texto.setPos(x, y)

    def contextMenuEvent(self, event):
        menu = QMenu()
        actualizar_costo = menu.addAction("Actualizar costo")
        eliminar = menu.addAction("Eliminar arista")

        accion = menu.exec(event.screenPos())

        if accion == actualizar_costo:
            self.scene().actualizar_costo_arista(self.origen, self.destino)
        elif accion == eliminar:
            self.scene().eliminar_arista(self.origen, self.destino)