from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: #FAFAF9;")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1001, 751))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 15, 0, 15)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.layoutDatos = QtWidgets.QVBoxLayout()
        self.layoutDatos.setContentsMargins(10, 10, 10, 10)
        self.layoutDatos.setSpacing(20)
        self.layoutDatos.setObjectName("layoutDatos")

        self.separator = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator.setGeometry(QtCore.QRect(5, 80, 65, 2))
        self.separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator.setStyleSheet("""
                   background-color: #A9B388 ;  
               """)
        self.layoutDatos.addWidget(self.separator)
        # Título
        self.Titulo = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.Titulo.setMinimumSize(QtCore.QSize(145, 100))
        self.Titulo.setMaximumSize(QtCore.QSize(200, 150))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.Titulo.setFont(font)
        self.Titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Titulo.setObjectName("Titulo")
        self.Titulo.setWordWrap(True)
        self.layoutDatos.addWidget(self.Titulo)

        self.separator = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator.setGeometry(QtCore.QRect(5, 80, 65, 2))
        self.separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator.setStyleSheet("""
            background-color: #A9B388 ;  
        """)
        self.layoutDatos.addWidget(self.separator)

        # Controles
        self.widgetControles = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.layoutControles = QtWidgets.QVBoxLayout(self.widgetControles)
        self.layoutControles.setContentsMargins(10, 10, 10, 10)
        self.layoutControles.setSpacing(20)
        self.layoutControles.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.infoButtonComboBox = QtWidgets.QPushButton(parent=self.widgetControles)
        self.infoButtonComboBox.setFixedSize(20, 20)
        self.infoButtonComboBox.setStyleSheet("background-color: transparent; border: none;")
        info_icon = QtGui.QIcon("./resources/images/icons8-información-50.png")
        self.infoButtonComboBox.setIcon(info_icon)
        self.infoButtonComboBox.setIconSize(QtCore.QSize(16, 16))

        self.layoutLabelComboBox = QtWidgets.QHBoxLayout()
        self.layoutLabelComboBox.setContentsMargins(0, 0, 0, 0)
        self.layoutLabelComboBox.setSpacing(3)

        self.layoutLabelComboBox.addWidget(self.infoButtonComboBox)
        self.labelComboBox = QtWidgets.QLabel(parent=self.widgetControles)
        self.labelComboBox.setText("Heurística:")
        self.layoutLabelComboBox.addWidget(self.labelComboBox)
        self.layoutLabelComboBox.addStretch()

        self.infoButtonComboBox.clicked.connect(self.mostrar_info_heuristica)

        self.layoutControles.addLayout(self.layoutLabelComboBox)

        self.comboBox = QtWidgets.QComboBox(parent=self.widgetControles)
        self.comboBox.setMinimumHeight(30)
        self.comboBox.setStyleSheet("background-color: white;")
        self.comboBox.addItems(["Ambos","Línea Recta", "Manhattan"])
        self.layoutControles.addWidget(self.comboBox)
        self.comboBox.currentIndexChanged.connect(self.actualizar_widgets_heuristica)

        self.infoButtonModo = QtWidgets.QPushButton(parent=self.widgetControles)
        self.infoButtonModo.setFixedSize(20, 20)
        self.infoButtonModo.setStyleSheet("background-color: transparent; border: none;")
        info_icon_modo = QtGui.QIcon("./resources/images/icons8-información-50.png")
        self.infoButtonModo.setIcon(info_icon_modo)
        self.infoButtonModo.setIconSize(QtCore.QSize(16, 16))

        self.layoutLabelModo = QtWidgets.QHBoxLayout()
        self.layoutLabelModo.setContentsMargins(0, 0, 0, 0)
        self.layoutLabelModo.setSpacing(3)

        self.layoutLabelModo.addWidget(self.infoButtonModo)

        self.labelModo = QtWidgets.QLabel(parent=self.widgetControles)
        self.labelModo.setText("Modo de generación:")
        self.layoutLabelModo.addWidget(self.labelModo)

        self.layoutLabelModo.addStretch()

        self.infoButtonModo.clicked.connect(self.mostrar_info_modo_generacion)

        self.layoutControles.addLayout(self.layoutLabelModo)

        self.layoutRadios = QtWidgets.QHBoxLayout()
        self.radioButtonManual = QtWidgets.QRadioButton(parent=self.widgetControles)
        self.radioButtonManual.setText("Manual")
        self.layoutRadios.addWidget(self.radioButtonManual)

        self.radioButtonAleatorio = QtWidgets.QRadioButton(parent=self.widgetControles)
        self.radioButtonAleatorio.setText("Aleatorio")
        self.layoutRadios.addWidget(self.radioButtonAleatorio)
        self.layoutControles.addLayout(self.layoutRadios)

        self.infoButtonSpinBox = QtWidgets.QPushButton(parent=self.widgetControles)
        self.infoButtonSpinBox.setFixedSize(20, 20)
        self.infoButtonSpinBox.setStyleSheet("background-color: transparent;")
        info_icon_spinbox = QtGui.QIcon("./resources/images/icons8-información-50.png")
        self.infoButtonSpinBox.setIcon(info_icon_spinbox)
        self.infoButtonSpinBox.setIconSize(QtCore.QSize(16, 16))

        self.layoutLabelSpinBox = QtWidgets.QHBoxLayout()
        self.layoutLabelSpinBox.setSpacing(5)
        self.layoutLabelSpinBox.setContentsMargins(0, 0, 0, 0)

        self.layoutLabelSpinBox.addWidget(self.infoButtonSpinBox)
        self.labelSpinBox = QtWidgets.QLabel(parent=self.widgetControles)
        self.labelSpinBox.setText("Cantidad de nodos:")
        self.layoutLabelSpinBox.addWidget(self.labelSpinBox)
        self.layoutLabelSpinBox.addStretch()

        self.layoutControles.addLayout(self.layoutLabelSpinBox)

        self.infoButtonSpinBox.clicked.connect(self.mostrar_info_cantidad_nodos)

        self.spinBox = QtWidgets.QSpinBox(parent=self.widgetControles)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.setMinimumHeight(30)
        self.spinBox.setStyleSheet("background-color: white;")
        self.layoutControles.addWidget(self.spinBox)

        self.layoutDatos.addWidget(self.widgetControles)
        self.layoutDatos.addStretch()

        self.layoutContenedorP = QtWidgets.QVBoxLayout()
        self.layoutContenedorP.setSpacing(20)
        self.layoutContenedorP.setObjectName("layoutContenedorP")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_3.setStyleSheet("background-color: white; border-radius: 15px;")
        self.horizontalLayout_3.addWidget(self.widget_3)

        self.widget_8 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_8.setStyleSheet("background-color: white; border-radius: 15px;")
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.layoutContenedorP.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_2.setStyleSheet("background-color: white; border-radius: 15px;")
        self.horizontalLayout_2.addWidget(self.widget_2)

        self.widget_5 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_5.setStyleSheet("background-color: white; border-radius: 15px;")
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.layoutContenedorP.addLayout(self.horizontalLayout_2)

        self.layoutContenedorP.setStretch(0, 10)
        self.layoutContenedorP.setStretch(1, 3)

        self.layoutMenu = QtWidgets.QVBoxLayout()
        self.layoutMenu.setObjectName("layoutMenu")

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.layoutMenu.addItem(spacerItem2)

        self.widget_4 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_4.setMinimumSize(QtCore.QSize(80, 300))
        self.widget_4.setMaximumSize(QtCore.QSize(100, 350))
        self.widget_4.setStyleSheet("background-color: white; border-radius: 25px; padding: 10px;")
        self.widget_4.setObjectName("widget_4")

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 60, 60))
        self.pushButton_2.setStyleSheet("background-color: #111111; border-radius: 15px; color: white; font-size: 24px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/images/icons8-play-30.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(53, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.line = QtWidgets.QFrame(parent=self.widget_4)
        self.line.setGeometry(QtCore.QRect(7, 80, 65, 2))
        self.line.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.widget_6 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_6.setGeometry(QtCore.QRect(5, 90, 80, 200))
        self.widget_6.setObjectName("widget_6")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.widget_6)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-10, 0, 91, 201))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 45))
        self.pushButton_3.setStyleSheet("background-color: #A9B388 ; border-radius: 15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resources/images/icons8-doble-derecha-52.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 40))
        self.verticalLayout_5.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 45))
        self.pushButton_4.setStyleSheet("background-color: #A9B388 ; border-radius: 15px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resources/images/icons8-doble-izquierda-52.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 40))
        self.verticalLayout_5.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 45))
        self.pushButton.setStyleSheet("background-color: #A9B388 ; border-radius: 15px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resources/images/icons8-escoba-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(30, 40))
        self.verticalLayout_5.addWidget(self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.layoutMenu.addWidget(self.widget_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.layoutMenu.addItem(spacerItem3)

        self.horizontalLayout.addLayout(self.layoutDatos)
        self.horizontalLayout.addLayout(self.layoutContenedorP)
        self.horizontalLayout.addLayout(self.layoutMenu)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)

        #Estilos
        self.labelComboBox.setStyleSheet("color: black; font-weight: bold;")
        self.labelModo.setStyleSheet("color: black; font-weight: bold;")
        self.radioButtonManual.setStyleSheet("color: black; font-weight: bold;")
        self.radioButtonAleatorio.setStyleSheet("color: black; font-weight: bold;")
        self.labelSpinBox.setStyleSheet("color: black; font-weight: bold;")
        self.Titulo.setStyleSheet("color: black; font-weight: bold; font-size: 22px;")

        self.comboBox.setStyleSheet("""
            background-color: white;
            color: black;
        """)

        radio_button_style = """
        QRadioButton {
            color: black;
            spacing: 8px;
        }

        QRadioButton::indicator {
            width: 16px;
            height: 16px;
            border-radius: 8px;
            border: 1px solid #999999;
            background: white;
        }

        QRadioButton::indicator:checked {
            background-color: #556B2F;
            border: 1px solid #FFFFFF  ;
        }
        """

        self.radioButtonManual.setStyleSheet(radio_button_style)
        self.radioButtonAleatorio.setStyleSheet(radio_button_style)
        self.spinBox.setStyleSheet("""
            background-color: white;
            color: black;
        """)

        self.layoutWidget2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.layoutWidget2.setContentsMargins(10, 10, 10, 10)
        self.labelWidget2 = QtWidgets.QLabel("Resultados:", parent=self.widget_2)
        self.labelWidget2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget2.setStyleSheet("font-size: 14px; font-weight: bold; color: #333333;")
        self.layoutWidget2.addWidget(self.labelWidget2)


        self.layoutWidget5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.layoutWidget5.setContentsMargins(10, 10, 10, 10)
        self.labelWidget5 = QtWidgets.QLabel("Resultados:", parent=self.widget_5)
        self.labelWidget5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget5.setStyleSheet("font-size: 14px; font-weight: bold; color: #333333;")
        self.layoutWidget5.addWidget(self.labelWidget5)

        widgets_con_sombra = [
            self.widget_2,
            self.widget_3,
            self.widget_5,
            self.widget_8,
            self.comboBox,
            self.spinBox,
            self.widget_4,
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


    # Ver si dejar estas funciones acá o mover al controlador
    def actualizar_widgets_heuristica(self):
        seleccion = self.comboBox.currentText()

        self.widget_8.setVisible(False)
        self.widget_3.setVisible(False)
        self.widget_2.setVisible(False)
        self.widget_5.setVisible(False)

        if seleccion == "Línea Recta":
            self.widget_8.setVisible(True)
            self.widget_2.setVisible(True)
        elif seleccion == "Manhattan":
            self.widget_3.setVisible(True)
            self.widget_5.setVisible(True)
        elif seleccion == "Ambos":
            self.widget_8.setVisible(True)
            self.widget_3.setVisible(True)
            self.widget_2.setVisible(True)
            self.widget_5.setVisible(True)

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
        QtWidgets.QMessageBox.information(None, "Información - Heurística",
                                          "Selecciona el tipo de heurística que se utilizará para calcular el camino.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))
        self.Titulo.setText(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))
