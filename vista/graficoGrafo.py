from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGraphicsTextItem, QInputDialog
from PyQt6.QtGui import QBrush, QPen, QFont, QColor
from PyQt6.QtCore import Qt
import math


class Nodo(QGraphicsEllipseItem):
    def __init__(self, x, y, nombre, radio=20):
        super().__init__(-radio, -radio, 2 * radio, 2 * radio)
        self.setBrush(QBrush(QColor("#6C7A4E")))
        self.setPen(QPen(Qt.GlobalColor.white))
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.setPos(x, y)
        self.nombre = nombre
        self.radio = radio

        texto = QGraphicsTextItem(nombre, self)
        texto.setPos(-radio / 2, -radio / 2)

    def contains_point(self, point):
        center = self.pos() + self.boundingRect().center()
        return math.sqrt((point.x() - center.x()) ** 2 + (point.y() - center.y()) ** 2) <= self.radio


class GrafoScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.nodos = []
        self.nodo_para_conectar = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, Nodo)), None)

            if item is None:
                if not any(nodo.contains_point(pos) for nodo in self.nodos):
                    nombre, ok = QInputDialog.getText(None, "Nuevo Nodo", "Nombre del nodo:")
                    if ok and nombre:
                        nodo = Nodo(pos.x(), pos.y(), nombre)
                        self.addItem(nodo)
                        self.nodos.append(nodo)
                        print(f"Nodo ({nombre}) creado en: ({pos.x():.2f}, {pos.y():.2f})")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, Nodo)), None)

            if item:
                if self.nodo_para_conectar is None:
                    self.nodo_para_conectar = item
                    item.setBrush(QBrush(QColor("#333333")))
                else:
                    if item != self.nodo_para_conectar:
                        peso, ok = QInputDialog.getInt(None, "Peso de la arista", "Ingrese el peso:")
                        if ok:
                            line = self.addLine(self.nodo_para_conectar.scenePos().x(),
                                                self.nodo_para_conectar.scenePos().y(),
                                                item.scenePos().x(), item.scenePos().y(),
                                                QPen(
                                                    Qt.GlobalColor.black))
                            line.setZValue(-1)

                            texto_peso = QGraphicsTextItem(str(peso), line)
                            texto_peso.setPos((self.nodo_para_conectar.scenePos().x() + item.scenePos().x()) / 2,
                                              (self.nodo_para_conectar.scenePos().y() + item.scenePos().y()) / 2)
                            texto_peso.setDefaultTextColor(Qt.GlobalColor.black)
                            texto_peso.setFont(QFont("Arial", 10))

                            print(f"Conectando ({self.nodo_para_conectar.nombre}) con ({item.nombre}) con peso {peso}")
                        self.nodo_para_conectar.setBrush(QBrush(QColor("#6C7A4E")))
                        self.nodo_para_conectar = None
