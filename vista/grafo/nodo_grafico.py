from typing import Literal

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem, QMenu, QGraphicsItem

from modelo.grafo.nodo import Nodo

TemaNodo = Literal["default", "seleccionado", "inicio", "actual", "cerrado", "abierto", "abierto_mejor", "camino", "objetivo"]

class NodoGrafico(QGraphicsEllipseItem):
    def __init__(self, nodo: Nodo, radio=20):
        super().__init__(-radio, -radio, 2 * radio, 2 * radio)
        self.aplicar_tema("default")
        self.permitir_movimiento(False)
        self.setPos(nodo.x, nodo.y)
        self.nombre: str = nodo.nombre
        self.radio = radio
        self.aristas_conectadas = set()
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
            case "inicio":
                self.setBrush(QBrush(QColor("#8B6D5C")))
            case "actual":
                self.setBrush(QBrush(QColor("#C8AE6C")))
            case "cerrado":
                self.setBrush(QBrush(QColor("#ced4da")))
            case "abierto":
                self.setBrush(QBrush(QColor("#9C9CA3")))
            case "abierto_mejor":
                self.setBrush(QBrush(QColor("#6E6E7F")))
            case "camino":
                self.setBrush(QBrush(QColor("#C4B2A3")))
            case "objetivo":
                self.setBrush(QBrush(QColor("#A05240")))

    def contextMenuEvent(self, event):
        menu = QMenu()
        eliminar = menu.addAction("Eliminar nodo")
        accion = menu.exec(event.screenPos())
        if accion == eliminar:
            self.scene().eliminar_nodo(self)

    def permitir_movimiento(self, permitir: bool):
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable, permitir)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable, permitir)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, permitir)

    def agregar_arista_conectada(self, arista):
        self.aristas_conectadas.add(arista)

    def itemChange(self, change, value):
        # Actualiza las posiciones de las aristas conectadas al nodo
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange:
            if hasattr(self, 'aristas_conectadas'):
                for arista in self.aristas_conectadas:
                    arista.actualizar_posicion()

        return super().itemChange(change, value)

    def __eq__(self, nodo):
        if isinstance(nodo, NodoGrafico):
            return self.nombre == nodo.nombre
        return False