from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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

        self.separator1 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.separator1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator1.setGeometry(QtCore.QRect(5, 10, 10, 1))
        self.separator1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator1.setObjectName("separator1")
        self.layoutDatos.addWidget(self.separator1)

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

        self.separator2 = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.separator2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.separator2.setGeometry(QtCore.QRect(5, 10, 10, 1))
        self.separator2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.separator2.setObjectName("separator2")
        self.layoutDatos.addWidget(self.separator2)

        # Controles
        self.widgetControles = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.layoutControles = QtWidgets.QVBoxLayout(self.widgetControles)
        self.layoutControles.setContentsMargins(10, 10, 10, 10)
        self.layoutControles.setSpacing(20)
        self.layoutControles.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.infoButtonModo = QtWidgets.QPushButton(parent=self.widgetControles)
        self.infoButtonModo.setFixedSize(20, 20)
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

        self.spinBox = QtWidgets.QSpinBox(parent=self.widgetControles)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(100)
        self.spinBox.setMinimumHeight(30)
        self.layoutControles.addWidget(self.spinBox)

        self.infoButtonComboBox = QtWidgets.QPushButton(parent=self.widgetControles)
        self.infoButtonComboBox.setFixedSize(20, 20)
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
        self.layoutControles.addLayout(self.layoutLabelComboBox)

        self.comboBox = QtWidgets.QComboBox(parent=self.widgetControles)
        self.comboBox.setMinimumHeight(30)
        self.comboBox.addItems(["Ambos","Línea Recta", "Manhattan"])
        self.layoutControles.addWidget(self.comboBox)

        self.layoutDatos.addWidget(self.widgetControles)
        self.layoutDatos.addStretch()


        self.layoutContenedorP = QtWidgets.QVBoxLayout()
        self.layoutContenedorP.setSpacing(20)
        self.layoutContenedorP.setObjectName("layoutContenedorP")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_H = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_H.setObjectName("widget_H")
        self.horizontalLayout_3.addWidget(self.widget_H)

        self.widget_LR = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_LR.setObjectName("widget_LR")
        self.horizontalLayout_3.addWidget(self.widget_LR)
        self.layoutContenedorP.addLayout(self.horizontalLayout_3)

        self.layout_widget_H = QtWidgets.QVBoxLayout(self.widget_H)
        self.graphicsView_H = QtWidgets.QGraphicsView(self.widget_H)
        self.scene_H = QtWidgets.QGraphicsScene()
        self.graphicsView_H.setScene(self.scene_H)
        self.graphicsView_H.setObjectName("graphicsView_H")
        self.layout_widget_H.addWidget(self.graphicsView_H)

        # Para widget_LR
        self.layout_widget_LR = QtWidgets.QVBoxLayout(self.widget_LR)
        self.graphicsView_LR = QtWidgets.QGraphicsView(self.widget_LR)
        self.scene_LR = QtWidgets.QGraphicsScene()
        self.graphicsView_LR.setScene(self.scene_LR)
        self.graphicsView_LR.setObjectName("graphicsView_LR")
        self.layout_widget_LR.addWidget(self.graphicsView_LR)


        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_HR = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_HR.setObjectName("widget_HR")
        self.horizontalLayout_2.addWidget(self.widget_HR)

        self.widget_RLR = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget_RLR.setObjectName("widget_RLR")
        self.horizontalLayout_2.addWidget(self.widget_RLR)
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
        self.widget_4.setObjectName("widget_4")

        self.pushButtonPlay = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButtonPlay.setGeometry(QtCore.QRect(10, 10, 60, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/images/icons8-play-30.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonPlay.setIcon(icon)
        self.pushButtonPlay.setIconSize(QtCore.QSize(53, 50))
        self.pushButtonPlay.setObjectName("pushButtonPlay")

        self.line = QtWidgets.QFrame(parent=self.widget_4)
        self.line.setGeometry(QtCore.QRect(7, 80, 65, 2))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./resources/images/icons8-doble-derecha-52.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 45))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./resources/images/icons8-doble-izquierda-52.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 45))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./resources/images/icons8-escoba-48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.layoutMenu.addWidget(self.widget_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.layoutMenu.addItem(spacerItem3)

        self.horizontalLayout.addLayout(self.layoutDatos)
        self.horizontalLayout.addLayout(self.layoutContenedorP)
        self.horizontalLayout.addLayout(self.layoutMenu)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 10)

        #Estilos
        self.layoutWidget2 = QtWidgets.QVBoxLayout(self.widget_RLR)
        self.layoutWidget2.setContentsMargins(10, 10, 10, 10)
        self.labelWidget2 = QtWidgets.QLabel("Resultados:", parent=self.widget_RLR)
        self.labelWidget2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget2.setObjectName("labelWidget2")
        self.layoutWidget2.addWidget(self.labelWidget2)


        self.layoutWidget5 = QtWidgets.QVBoxLayout(self.widget_HR)
        self.layoutWidget5.setContentsMargins(10, 10, 10, 10)
        self.labelWidget5 = QtWidgets.QLabel("Resultados:", parent=self.widget_HR)
        self.labelWidget5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget5.setObjectName("labelWidget5")
        self.layoutWidget5.addWidget(self.labelWidget5)

        widgets_con_sombra = [

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))
        self.Titulo.setText(_translate("MainWindow", "Algoritmo A*: Comparación de Heurísticas"))