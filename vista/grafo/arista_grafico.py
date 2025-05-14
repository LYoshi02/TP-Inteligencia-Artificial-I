from typing import Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QFont, QColor
from PyQt6.QtWidgets import QGraphicsItemGroup, QGraphicsLineItem, QGraphicsTextItem

from grafo.nodo import Nodo

TemaArista = Literal["default", "camino"]

class AristaGrafico(QGraphicsItemGroup):
    def __init__(self, origen: Nodo, destino: Nodo, peso: float, parent=None):
        super().__init__(parent)

        # Crear la línea
        self.linea = QGraphicsLineItem(
            origen.x, origen.y,
            destino.x, destino.y
        )
        self.linea.setZValue(-1)  # Detrás de los nodos

        # Crear el texto del peso
        self.texto = QGraphicsTextItem(str(peso), self.linea)
        # Posicionar el texto en el medio de la línea
        self.texto.setPos(
            (origen.x + destino.x) / 2,
            (origen.y + destino.y) / 2
        )

        self.aplicar_tema("default")

        # Agregar elementos al grupo
        self.addToGroup(self.linea)
        self.addToGroup(self.texto)

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
