from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow

from controlador.controlador import Controlador
from vista.ui_mainWindow import Ui_MainWindow
from vista.graficoGrafo import GrafoScene

class Vista(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centrar_ventana()
        self.controlador = Controlador()
        self.scene_H = GrafoScene()
        self.scene_LR = GrafoScene()
        self.ui.graphicsView_H.setScene(self.scene_H)
        self.ui.graphicsView_LR.setScene(self.scene_LR)

        #Desactivar widgets
        self.ui.graphicsView_H.setDisabled(True)
        self.ui.graphicsView_LR.setDisabled(True)

        # Conectar botones de la interfaz
        self.ui.pushButtonPlay.clicked.connect(self.iniciar_algoritmo)
        self.ui.pushButton_3.clicked.connect(self.avanzar_paso)
        self.ui.pushButton_4.clicked.connect(self.retroceder_paso)

        # ComboBox Heurística
        self.ui.comboBox.setDisabled(True)
        self.ui.comboBox.currentTextChanged.connect(self.actualizar_widgets_heuristica)
        self.ui.infoButtonComboBox.clicked.connect(self.mostrar_info_heuristica)

        # Modo de Generación
        self.ui.infoButtonModo.clicked.connect(self.mostrar_info_modo_generacion)
        # Selección de modo
        self.ui.radioButtonManual.toggled.connect(self.activar_campos)
        self.ui.spinBox.setDisabled(True)
        self.ui.radioButtonAleatorio.toggled.connect(self.activar_campos)

        # Cantidad de nodos
        self.ui.infoButtonSpinBox.clicked.connect(self.mostrar_info_cantidad_nodos)

    def centrar_ventana(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def iniciar_algoritmo(self):
        self.controlador.comenzar_algoritmo()

    def avanzar_paso(self):
        self.controlador.avanzar_paso()

    def retroceder_paso(self):
        self.controlador.retroceder_paso()

    def actualizar_widgets_heuristica(self):
        seleccion = self.ui.comboBox.currentText()

        # Ocultar todos los widgets primero
        self.ui.widget_LR.setVisible(False)
        self.ui.widget_RLR.setVisible(False)
        self.ui.widget_H.setVisible(False)
        self.ui.widget_HR.setVisible(False)

        # Mostrar los widgets correspondientes según la selección
        if seleccion == "Línea Recta":
            self.ui.widget_LR.setVisible(True)
            self.ui.widget_RLR.setVisible(True)
            self.ui.graphicsView_LR.setDisabled(False)
        elif seleccion == "Manhattan":
            self.ui.widget_H.setVisible(True)
            self.ui.widget_HR.setVisible(True)
            self.ui.graphicsView_H.setDisabled(False)
        elif seleccion == "Ambos":
            self.ui.graphicsView_H.setDisabled(False)
            self.ui.graphicsView_LR.setDisabled(False)
            self.ui.widget_LR.setVisible(True)
            self.ui.widget_RLR.setVisible(True)
            self.ui.widget_H.setVisible(True)
            self.ui.widget_HR.setVisible(True)

    def activar_campos(self):
        self.ui.comboBox.setDisabled(False)
        if self.ui.radioButtonManual.isChecked():
            self.ui.spinBox.setDisabled(True)
        elif self.ui.radioButtonAleatorio.isChecked():
            self.ui.spinBox.setDisabled(False)

    def mostrar_info_cantidad_nodos(self):
        QtWidgets.QMessageBox.information(
            None,
            "Información - Cantidad de Nodos",
            "Define cuántos nodos tendrá el grafo a generar"
        )

    def mostrar_info_modo_generacion(self):
        QtWidgets.QMessageBox.information(
            None,
            "Información - Modo de Generación",
            "Manual: creas los nodos y conexiones con click.\nAleatorio: generar un grafo aleatorio automáticamente a partir de una cantidad de nodos dada."
        )

    def mostrar_info_heuristica(self):
        QtWidgets.QMessageBox.information(
            None, "Información - Heurística",
            "Selecciona el tipo de heurística que se utilizará para calcular el camino."
        )

