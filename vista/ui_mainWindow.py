from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QSizePolicy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Columna izquierda: Datos y controles
        self.layoutDatos = QtWidgets.QVBoxLayout()
        self.layoutDatos.setContentsMargins(10, 10, 10, 10)
        self.layoutDatos.setSpacing(20)

        self.separator1 = QtWidgets.QFrame()
        self.separator1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator1.setObjectName("separator1")
        self.layoutDatos.addWidget(self.separator1)

        self.Titulo = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Titulo.setWordWrap(True)
        self.Titulo.setObjectName("Titulo")
        self.layoutDatos.addWidget(self.Titulo)

        self.separator2 = QtWidgets.QFrame()
        self.separator2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator2.setObjectName("separator2")
        self.layoutDatos.addWidget(self.separator2)

        self.widgetControles = QtWidgets.QWidget()
        self.layoutControles = QtWidgets.QVBoxLayout(self.widgetControles)
        self.layoutControles.setContentsMargins(10, 10, 10, 10)
        self.layoutControles.setSpacing(20)
        self.layoutControles.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Botón info + label Modo
        self.layoutLabelModo = QtWidgets.QHBoxLayout()
        self.infoButtonModo = QtWidgets.QPushButton()
        self.infoButtonModo.setObjectName("infoButtonModo")
        self.infoButtonModo.setFixedSize(20, 20)
        self.infoButtonModo.setIcon(QtGui.QIcon("./resources/images/icons8-información-50.png"))
        self.infoButtonModo.setIconSize(QtCore.QSize(16, 16))
        self.layoutLabelModo.addWidget(self.infoButtonModo)
        self.labelModo = QtWidgets.QLabel("Modo de generación:")
        self.layoutLabelModo.addWidget(self.labelModo)
        self.layoutLabelModo.addStretch()
        self.layoutControles.addLayout(self.layoutLabelModo)

        self.layoutRadios = QtWidgets.QHBoxLayout()
        self.radioButtonManual = QtWidgets.QRadioButton("Manual")
        self.radioButtonAleatorio = QtWidgets.QRadioButton("Aleatorio")
        self.layoutRadios.addWidget(self.radioButtonManual)
        self.layoutRadios.addWidget(self.radioButtonAleatorio)
        self.layoutControles.addLayout(self.layoutRadios)

        # Instrucciones para construir el grafo
        self.groupBoxInstrucciones = QtWidgets.QGroupBox("")
        self.groupBoxInstrucciones.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        )
        self.layoutInstrucciones = QtWidgets.QVBoxLayout(self.groupBoxInstrucciones)
        self.layoutInstrucciones.setSpacing(8)
        self.layoutControles.addWidget(self.groupBoxInstrucciones)

        # SpinBox
        self.layoutLabelSpinBox = QtWidgets.QHBoxLayout()
        self.infoButtonSpinBox = QtWidgets.QPushButton()
        self.infoButtonSpinBox.setObjectName("infoButtonSpinBox")
        self.infoButtonSpinBox.setFixedSize(20, 20)
        self.infoButtonSpinBox.setIcon(QtGui.QIcon("./resources/images/icons8-información-50.png"))
        self.infoButtonSpinBox.setIconSize(QtCore.QSize(16, 16))
        self.layoutLabelSpinBox.addWidget(self.infoButtonSpinBox)
        self.labelSpinBox = QtWidgets.QLabel("Cantidad de nodos:")
        self.layoutLabelSpinBox.addWidget(self.labelSpinBox)
        self.layoutLabelSpinBox.addStretch()
        self.layoutControles.addLayout(self.layoutLabelSpinBox)

        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.setMinimumHeight(30)
        self.layoutControles.addWidget(self.spinBox)

        # ComboBox
        self.layoutLabelComboBox = QtWidgets.QHBoxLayout()
        self.infoButtonComboBox = QtWidgets.QPushButton()
        self.infoButtonComboBox.setObjectName("infoButtonComboBox")
        self.infoButtonComboBox.setFixedSize(20, 20)
        self.infoButtonComboBox.setIcon(QtGui.QIcon("./resources/images/icons8-información-50.png"))
        self.infoButtonComboBox.setIconSize(QtCore.QSize(16, 16))
        self.layoutLabelComboBox.addWidget(self.infoButtonComboBox)
        self.labelComboBox = QtWidgets.QLabel("Heurística:")
        self.layoutLabelComboBox.addWidget(self.labelComboBox)
        self.layoutLabelComboBox.addStretch()
        self.layoutControles.addLayout(self.layoutLabelComboBox)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setMinimumHeight(30)
        self.comboBox.addItems(["Selecciona una heurística", "Ambos", "Línea Recta", "Manhattan"])
        self.layoutControles.addWidget(self.comboBox)

        self.layoutDatos.addWidget(self.widgetControles)
        self.layoutDatos.addStretch()

        # Columna central: Contenedor principal
        self.layoutContenedorP = QtWidgets.QVBoxLayout()
        self.layoutContenedorP.setSpacing(20)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.widget_base = QtWidgets.QWidget()
        self.widget_manhattan = QtWidgets.QWidget()
        self.widget_lRecta = QtWidgets.QWidget()
        self.widget_base.setObjectName("widget_base")
        self.widget_manhattan.setObjectName("widget_manhattan")
        self.widget_lRecta.setObjectName("widget_lRecta")
        self.horizontalLayout_3.addWidget(self.widget_base)
        self.horizontalLayout_3.addWidget(self.widget_manhattan)
        self.horizontalLayout_3.addWidget(self.widget_lRecta)
        self.layoutContenedorP.addLayout(self.horizontalLayout_3)

        self.layout_widget_base = QtWidgets.QVBoxLayout(self.widget_base)
        self.graphicsView_base = QtWidgets.QGraphicsView()
        self.graphicsView_base.setObjectName("graphicsView_base")
        self.layout_widget_base.addWidget(self.graphicsView_base)

        self.layout_widget_manhattan = QtWidgets.QVBoxLayout(self.widget_manhattan)
        self.graphicsView_manhattan = QtWidgets.QGraphicsView()
        self.graphicsView_manhattan.setObjectName("graphicsView_manhattan")
        self.layout_widget_manhattan.addWidget(self.graphicsView_manhattan)

        self.layout_widget_lRecta = QtWidgets.QVBoxLayout(self.widget_lRecta)
        self.graphicsView_lRecta = QtWidgets.QGraphicsView()
        self.graphicsView_lRecta.setObjectName("graphicsView_lRecta")
        self.layout_widget_lRecta.addWidget(self.graphicsView_lRecta)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.widget_manhattanResults = QtWidgets.QWidget()
        self.widget_manhattanResults.setObjectName("widget_manhattanResults")
        self.widget_lRectaResults = QtWidgets.QWidget()
        self.widget_lRectaResults.setObjectName("widget_lRectaResults")
        self.horizontalLayout_2.addWidget(self.widget_manhattanResults)
        self.horizontalLayout_2.addWidget(self.widget_lRectaResults)
        self.layoutContenedorP.addLayout(self.horizontalLayout_2)

        self.layoutWidget2 = QtWidgets.QVBoxLayout(self.widget_lRectaResults)
        self.labelWidget2 = QtWidgets.QLabel("Resultados - Línea Recta:")
        self.labelWidget2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget2.setObjectName("labelWidget2")
        self.layoutWidget2.addWidget(self.labelWidget2)

        self.layoutWidget5 = QtWidgets.QVBoxLayout(self.widget_manhattanResults)
        self.labelWidget5 = QtWidgets.QLabel("Resultados - Manhattan:")
        self.labelWidget5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget5.setObjectName("labelWidget5")
        self.layoutWidget5.addWidget(self.labelWidget5)

        # Columna derecha: Menú de botones
        self.layoutMenu = QtWidgets.QVBoxLayout()
        self.layoutMenu.addStretch()

        self.widget_menu = QtWidgets.QWidget()
        self.layoutBotones = QtWidgets.QVBoxLayout(self.widget_menu)
        self.widget_menu.setObjectName("widget_menu")
        self.layoutBotones.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButtonPlay = QtWidgets.QPushButton()
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.pushButtonPlay.setIcon(QtGui.QIcon("./resources/images/icons8-play-30.png"))
        self.pushButtonPlay.setIconSize(QtCore.QSize(53, 50))
        self.pushButtonPlay.setFixedSize(60, 60)
        self.layoutBotones.addWidget(self.pushButtonPlay)

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutBotones.addWidget(self.line)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        icon_nombres = ["siguiente_paso", "paso_atras", "limpiar"]
        for i, icon_path in enumerate(
                ["icons8-doble-derecha-52.png", "icons8-doble-izquierda-52.png", "icons8-escoba-48.png"]):
            btn = QtWidgets.QPushButton()
            btn.setObjectName(f"pushButton_{icon_nombres[i]}")
            btn.setMinimumSize(50, 45)
            btn.setMaximumSize(50, 45)
            btn.setIcon(QtGui.QIcon(f"./resources/images/{icon_path}"))
            btn.setIconSize(QtCore.QSize(30, 40))
            self.verticalLayout_5.addWidget(btn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.layoutBotones.addLayout(self.verticalLayout_5)
        self.layoutMenu.addWidget(self.widget_menu)
        self.layoutMenu.addStretch()

        self.horizontalLayout.addLayout(self.layoutDatos, 2)
        self.horizontalLayout.addLayout(self.layoutContenedorP, 10)
        self.horizontalLayout.addLayout(self.layoutMenu, 1)

        widgets_con_sombra = [
            self.widget_base, self.widget_manhattan, self.widget_manhattanResults, self.widget_lRecta,
            self.widget_lRectaResults, self.comboBox, self.spinBox, self.widget_menu
        ]
        for widget in widgets_con_sombra:
            sombra = QGraphicsDropShadowEffect()
            sombra.setBlurRadius(10)
            sombra.setOffset(0, 2)
            sombra.setColor(QtGui.QColor(0, 0, 0, 45))
            widget.setGraphicsEffect(sombra)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))
        self.Titulo.setText(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))
