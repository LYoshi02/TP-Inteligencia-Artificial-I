from typing import Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QFont, QColor
from PyQt6.QtWidgets import QGraphicsItemGroup, QGraphicsLineItem, QGraphicsTextItem

from vista.grafo.nodo_grafico import NodoGrafico

TemaArista = Literal["default", "camino"]

class AristaGrafico(QGraphicsItemGroup):
    def __init__(self, origen: NodoGrafico, destino: NodoGrafico, peso: float, parent=None):
        super().__init__(parent)
        self.origen: NodoGrafico = origen
        self.destino: NodoGrafico = destino

        # Crear la línea
        self.linea = QGraphicsLineItem()
        self.linea.setZValue(-1)  # Detrás de los nodos

        # Crear el texto del peso
        self.texto = QGraphicsTextItem(str(peso), self.linea)

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
        self.texto.setPos(
            (origen_pos.x() + destino_pos.x()) / 2,
            (origen_pos.y() + destino_pos.y()) / 2
        )