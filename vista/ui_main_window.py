from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QSizePolicy, QHeaderView

from constantes.heuristicas import HEURISTICAS
from constantes.recursos import RUTAS_RECURSOS


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

        self.widgetDatos = QtWidgets.QWidget()
        self.widgetDatos.setLayout(self.layoutDatos)

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
        self.infoButtonModo.setIcon(QtGui.QIcon(RUTAS_RECURSOS.IMAGENES.informacion))
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
        self.infoButtonSpinBox.setIcon(QtGui.QIcon(RUTAS_RECURSOS.IMAGENES.informacion))
        self.infoButtonSpinBox.setIconSize(QtCore.QSize(16, 16))
        self.layoutLabelSpinBox.addWidget(self.infoButtonSpinBox)
        self.labelSpinBox = QtWidgets.QLabel("Cantidad de nodos:")
        self.layoutLabelSpinBox.addWidget(self.labelSpinBox)
        self.layoutLabelSpinBox.addStretch()
        self.layoutControles.addLayout(self.layoutLabelSpinBox)

        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(400)
        self.spinBox.setMinimumHeight(30)
        self.layoutControles.addWidget(self.spinBox)

        self.pushButton_generar = QtWidgets.QPushButton()
        self.pushButton_generar.setObjectName("pushButton_generar")
        self.pushButton_generar.setText("Generar Grafo")
        self.pushButton_generar.setFixedSize(130, 35)
        self.layoutControles.addWidget(self.pushButton_generar, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)

        # ComboBox
        self.layoutLabelComboBox = QtWidgets.QHBoxLayout()
        self.infoButtonComboBox = QtWidgets.QPushButton()
        self.infoButtonComboBox.setObjectName("infoButtonComboBox")
        self.infoButtonComboBox.setFixedSize(20, 20)
        self.infoButtonComboBox.setIcon(QtGui.QIcon(RUTAS_RECURSOS.IMAGENES.informacion))
        self.infoButtonComboBox.setIconSize(QtCore.QSize(16, 16))
        self.layoutLabelComboBox.addWidget(self.infoButtonComboBox)
        self.labelComboBox = QtWidgets.QLabel("Heurística:")
        self.layoutLabelComboBox.addWidget(self.labelComboBox)
        self.layoutLabelComboBox.addStretch()
        self.layoutControles.addLayout(self.layoutLabelComboBox)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setMinimumHeight(30)
        self.comboBox.addItems([
            "Selecciona una heurística",
            "Ambos",
            HEURISTICAS.distancia_euclidiana.texto,
            HEURISTICAS.distancia_manhattan.texto
        ])
        self.layoutControles.addWidget(self.comboBox)

        # ----- Botones de Manejo de Archivos -----
        self.layoutBotonesArchivo = QtWidgets.QVBoxLayout(self.widgetControles)
        self.layoutBotonesArchivo.setSpacing(10)

        self.pushButtonCargarArchivo = QtWidgets.QPushButton()
        self.pushButtonCargarArchivo.setObjectName("pushButton_cargar_archivo_grafo")
        self.pushButtonCargarArchivo.setText("Cargar Grafo")
        self.pushButtonCargarArchivo.setFixedSize(130, 35)

        self.pushButtonGuardarArchivo = QtWidgets.QPushButton()
        self.pushButtonGuardarArchivo.setObjectName("pushButton_guardar_archivo_grafo")
        self.pushButtonGuardarArchivo.setText("Guardar Grafo")
        self.pushButtonGuardarArchivo.setFixedSize(130, 35)

        self.layoutBotonesArchivo.addWidget(self.pushButtonCargarArchivo, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.layoutBotonesArchivo.addWidget(self.pushButtonGuardarArchivo, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.layoutControles.addLayout(self.layoutBotonesArchivo)
        # -------------------

        self.layoutDatos.addWidget(self.widgetControles)
        self.layoutDatos.addStretch()

        # Columna central: Contenedor principal
        self.layoutContenedorP = QtWidgets.QVBoxLayout()
        self.layoutContenedorP.setSpacing(10)

        self.horizontalLayout_encabezado = QtWidgets.QHBoxLayout()
        self.widget_referencia = QtWidgets.QWidget()
        self.widget_referencia.setObjectName("widget_referencia")
        self.layout_widget_referencia = QtWidgets.QHBoxLayout(self.widget_referencia)
        self.labelWidgetRef = QtWidgets.QLabel("Referencias:")
        self.labelWidgetRef.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidgetRef.setObjectName("labelWidgetRef")
        self.layout_widget_referencia.addWidget(self.labelWidgetRef)
        self.horizontalLayout_encabezado.addWidget(self.widget_referencia)
        self.layoutContenedorP.addLayout(self.horizontalLayout_encabezado)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.widget_base = QtWidgets.QWidget()
        self.widget_manhattan = QtWidgets.QWidget()
        self.widget_euclidiana = QtWidgets.QWidget()
        self.widget_base.setObjectName("widget_base")
        self.widget_manhattan.setObjectName("widget_manhattan")
        self.widget_euclidiana.setObjectName("widget_euclidiana")
        self.horizontalLayout_3.addWidget(self.widget_base)
        self.horizontalLayout_3.addWidget(self.widget_manhattan)
        self.horizontalLayout_3.addWidget(self.widget_euclidiana)
        self.layoutContenedorP.addLayout(self.horizontalLayout_3)

        self.layout_widget_base = QtWidgets.QVBoxLayout(self.widget_base)
        self.graphicsView_base = QtWidgets.QGraphicsView()
        self.graphicsView_base.setObjectName("graphicsView_base")
        self.layout_widget_base.addWidget(self.graphicsView_base)

        self.layout_widget_manhattan = QtWidgets.QVBoxLayout(self.widget_manhattan)
        self.graphicsView_manhattan = QtWidgets.QGraphicsView()
        self.graphicsView_manhattan.setObjectName("graphicsView_manhattan")
        self.layout_widget_manhattan.addWidget(self.graphicsView_manhattan)

        self.layout_widget_euclidiana= QtWidgets.QVBoxLayout(self.widget_euclidiana)
        self.graphicsView_euclidiana = QtWidgets.QGraphicsView()
        self.graphicsView_euclidiana.setObjectName("graphicsView_euclidiana")
        self.layout_widget_euclidiana.addWidget(self.graphicsView_euclidiana)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.widget_manhattanResults = QtWidgets.QWidget()
        self.widget_manhattanResults.setObjectName("widget_manhattanResults")
        self.widget_euclidianaResults = QtWidgets.QWidget()
        self.widget_euclidianaResults.setObjectName("widget_euclidianaResults")
        self.horizontalLayout_2.addWidget(self.widget_manhattanResults)
        self.horizontalLayout_2.addWidget(self.widget_euclidianaResults)
        self.layoutContenedorP.addLayout(self.horizontalLayout_2)

        self.layoutWidget2 = QtWidgets.QVBoxLayout(self.widget_euclidianaResults)
        self.labelWidget2 = QtWidgets.QLabel("Resultados - Distancia Euclidiana:")
        self.labelWidget2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget2.setObjectName("labelWidget2")
        self.layoutWidget2.addWidget(self.labelWidget2)

        self.layoutWidget5 = QtWidgets.QVBoxLayout(self.widget_manhattanResults)
        self.labelWidget5 = QtWidgets.QLabel("Resultados - Distancia Manhattan:")
        self.labelWidget5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.labelWidget5.setObjectName("labelWidget5")
        self.layoutWidget5.addWidget(self.labelWidget5)

        self.table_manhattan = QtWidgets.QTableWidget()
        self.table_manhattan.setColumnCount(6)
        self.table_manhattan.setHorizontalHeaderLabels(["Nro de paso", "Nodos Explorados", "Costo Total", "Tiempo Total", "Camino Encontrado", "Objetivo encontrado"])
        self.table_manhattan.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table_manhattan.verticalHeader().setVisible(False)
        self.layoutWidget5.addWidget(self.table_manhattan)

        self.table_euclidiana = QtWidgets.QTableWidget()
        self.table_euclidiana.setColumnCount(6)
        self.table_euclidiana.setHorizontalHeaderLabels(["Nro de paso", "Nodos Explorados", "Costo Total", "Tiempo Total", "Camino Encontrado", "Objetivo encontrado"])
        self.table_euclidiana.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table_euclidiana.verticalHeader().setVisible(False)
        self.layoutWidget2.addWidget(self.table_euclidiana)

        # Columna derecha: Menú de botones
        self.layoutMenu = QtWidgets.QVBoxLayout()
        self.layoutMenu.addStretch()

        self.widget_menu = QtWidgets.QWidget()
        self.layoutBotones = QtWidgets.QVBoxLayout(self.widget_menu)
        self.widget_menu.setObjectName("widget_menu")
        self.layoutBotones.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.pushButtonPlay = QtWidgets.QPushButton()
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.pushButtonPlay.setIcon(QtGui.QIcon(RUTAS_RECURSOS.IMAGENES.play))
        self.pushButtonPlay.setIconSize(QtCore.QSize(53, 50))
        self.pushButtonPlay.setFixedSize(60, 60)
        self.pushButtonPlay.setToolTip("Iniciar algoritmo")
        self.layoutBotones.addWidget(self.pushButtonPlay)

        self.pushButtonPause = QtWidgets.QPushButton()
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.pushButtonPause.setIcon(QtGui.QIcon(RUTAS_RECURSOS.IMAGENES.pausa))
        self.pushButtonPause.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonPause.setFixedSize(60, 60)
        self.pushButtonPause.setToolTip("Pausar algoritmo")
        self.pushButtonPause.hide()
        self.layoutBotones.addWidget(self.pushButtonPause)

        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutBotones.addWidget(self.line)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        botones: dict[str, dict[str, str]] = {
            "paso_atras": {
                "tooltip": "Retroceder paso",
                "icono": RUTAS_RECURSOS.IMAGENES.flecha_doble_izquierda
            },
            "siguiente_paso": {
                "tooltip": "Avanzar paso",
                "icono": RUTAS_RECURSOS.IMAGENES.flecha_doble_derecha
            },
            "paso_inicial": {
                "tooltip": "Ir al paso inicial",
                "icono": RUTAS_RECURSOS.IMAGENES.flecha_paso_inicial
            },
            "ultimo_paso": {
                "tooltip": "Ir al último paso",
                "icono": RUTAS_RECURSOS.IMAGENES.flecha_ultimo_paso
            },
            "limpiar": {
                "tooltip": "Borrar grafo",
                "icono": RUTAS_RECURSOS.IMAGENES.escoba
            }
        }

        for nombre_boton, info_boton in botones.items():
            btn = QtWidgets.QPushButton()
            btn.setObjectName(f"pushButton_{nombre_boton}")
            btn.setMinimumSize(50, 45)
            btn.setMaximumSize(50, 45)
            btn.setToolTip(info_boton["tooltip"])
            btn.setIcon(QtGui.QIcon(info_boton["icono"]))
            btn.setIconSize(QtCore.QSize(30, 40))
            self.verticalLayout_5.addWidget(btn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.layoutBotones.addLayout(self.verticalLayout_5)
        self.layoutMenu.addWidget(self.widget_menu)
        self.layoutMenu.addStretch()

        self.horizontalLayout.addWidget(self.widgetDatos, 2)
        self.horizontalLayout.addLayout(self.layoutContenedorP, 10)
        self.horizontalLayout.addLayout(self.layoutMenu, 1)

        widgets_con_sombra = [
            self.widget_base, self.widget_manhattan, self.widget_manhattanResults, self.widget_euclidiana,
            self.widget_euclidianaResults, self.comboBox, self.spinBox, self.widget_menu, self.widget_referencia
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
