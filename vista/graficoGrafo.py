import math

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen, QFont, QColor
from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene, QGraphicsTextItem, QInputDialog, QMenu

from controlador.controlador import Controlador


class NodoGrafico(QGraphicsEllipseItem):
    def __init__(self, x, y, nombre, radio=20):
        super().__init__(-radio, -radio, 2 * radio, 2 * radio)
        self.setBrush(QBrush(QColor("#487575")))
        self.setPen(QPen(Qt.GlobalColor.black))
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.setPos(x, y)
        self.nombre = nombre
        self.radio = radio

        texto = QGraphicsTextItem(nombre, self)
        texto.setPos(-radio / 2, -radio / 2)

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

class GrafoScene(QGraphicsScene):
    def __init__(self, controlador: Controlador):
        super().__init__()
        self.controlador = controlador
        self.nodos = []
        self.nodo_para_conectar = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, NodoGrafico)), None)

            if item is None:
                if not any(nodo.contains_point(pos) for nodo in self.nodos):
                    nombre, ok = QInputDialog.getText(None, "Nuevo Nodo", "Nombre del nodo:")
                    if ok and nombre:
                        nodo = NodoGrafico(pos.x(), pos.y(), nombre)
                        self.addItem(nodo)
                        self.nodos.append(nodo)
                        print(f"Nodo ({nombre}) creado en: ({pos.x():.2f}, {pos.y():.2f})")
                        #Se agrega el nodo al controlador
                        self.controlador.agregar_nodo(nombre, pos.x(), pos.y())

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.scenePos()
            items = self.items(pos)
            item = next((i for i in items if isinstance(i, NodoGrafico)), None)

            if item:
                if self.nodo_para_conectar is None:
                    self.nodo_para_conectar = item
                    item.setBrush(QBrush(QColor("#333333")))
                    item.setPen(QPen(QColor("#555555")))

                else:
                    if item != self.nodo_para_conectar:
                        peso, ok = QInputDialog.getInt(None, "Peso de la arista", "Ingrese el peso:")
                        if ok:
                            # Se agrega la arista al controlador
                            nodo_origen = self.controlador.obtener_nodo(self.nodo_para_conectar.nombre)
                            nodo_destino = self.controlador.obtener_nodo(item.nombre)

                            if nodo_origen and nodo_destino:
                                self.controlador.agregar_arista(nodo_origen, nodo_destino, peso)

                            line = self.addLine(self.nodo_para_conectar.scenePos().x(),
                                                self.nodo_para_conectar.scenePos().y(),
                                                item.scenePos().x(), item.scenePos().y(),
                                                QPen(Qt.GlobalColor.black))
                            line.setZValue(-1)

                            texto_peso = QGraphicsTextItem(str(peso), line)
                            texto_peso.setPos((self.nodo_para_conectar.scenePos().x() + item.scenePos().x()) / 2,
                                              (self.nodo_para_conectar.scenePos().y() + item.scenePos().y()) / 2)
                            texto_peso.setDefaultTextColor(Qt.GlobalColor.black)
                            texto_peso.setFont(QFont("Arial", 10))

                            print(f"Conectando ({self.nodo_para_conectar.nombre}) con ({item.nombre}) con peso {peso}")

                        self.nodo_para_conectar.setBrush(QBrush(QColor("#487575")))
                        self.nodo_para_conectar.setPen(QPen(Qt.GlobalColor.black))
                        self.nodo_para_conectar = None

    def eliminar_nodo(self, nodo):
        self.controlador.eliminar_nodo(nodo.nombre, nodo.pos().x(), nodo.pos().y())
        self.removeItem(nodo)
        self.nodos.remove(nodo)

        for item in self.items():
            if isinstance(item, QtWidgets.QGraphicsLineItem):
                if (item.line().p1() == nodo.scenePos()) or (item.line().p2() == nodo.scenePos()):
                    self.removeItem(item)