import math
from typing import Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QMenu

from modelo.grafo.nodo import Nodo

TemaNodo = Literal["default", "seleccionado", "inicio", "actual", "cerrado", "abierto", "abierto_mejor", "camino"]

class NodoGrafico(QGraphicsEllipseItem):
    def __init__(self, nodo: Nodo, radio=20):
        super().__init__(-radio, -radio, 2 * radio, 2 * radio)
        self.aplicar_tema("default")
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.setPos(nodo.x, nodo.y)
        self.nombre = nodo.nombre
        self.radio = radio
        self.setZValue(10)
        self.setToolTip(f"Posición: ({nodo.x:.2f}, {nodo.y:.2f})\n"
                        f"g: {nodo.costo_desde_inicio:.2f}\n"
                        f"h': {nodo.heuristica:.2f}\n"
                        f"f': {nodo.costo_total:.2f}")

        texto = QGraphicsTextItem(nodo.nombre, self)
        texto.setPos(-radio / 2, -radio / 2)

    def aplicar_tema(self, tema: TemaNodo):
        match tema:
            case "default":
                self.setBrush(QBrush(QColor("#487575")))
                self.setPen(QPen(Qt.GlobalColor.black))
            case "seleccionado":
                self.setBrush(QBrush(QColor("#333333")))
                self.setPen(QPen(QColor("#555555")))
            case "inicio":
                self.setBrush(QBrush(QColor("#ef233c")))
            case "actual":
                self.setBrush(QBrush(QColor("#EE9B00")))
            case "cerrado":
                self.setBrush(QBrush(QColor("#ced4da")))
            case "abierto":
                self.setBrush(QBrush(QColor("#48cae4")))
            case "abierto_mejor":
                self.setBrush(QBrush(QColor("#0077b6")))
            case "camino":
                self.setBrush(QBrush(QColor("#ff5a5f")))

    def set_color(self, color: QColor):
        self.setBrush(QBrush(color))

    def contains_point(self, point): # Determina si clic fue dentro del círculo del nodo
        center = self.pos() + self.boundingRect().center()
        return math.sqrt((point.x() - center.x()) ** 2 + (point.y() - center.y()) ** 2) <= self.radio

    def contextMenuEvent(self, event):
        menu = QMenu()
        eliminar = menu.addAction("Eliminar nodo")
        accion = menu.exec(event.screenPos())
        if accion == eliminar:
            self.scene().eliminar_nodo(self)
