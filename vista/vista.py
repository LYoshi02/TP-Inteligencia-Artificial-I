import re

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QMainWindow, QFileDialog

from constantes.heuristicas import HEURISTICAS
from constantes.recursos import RUTAS_RECURSOS
from controlador.controlador import Controlador
from modelo.algoritmo.resultados_algoritmo import ResultadosAlgoritmo
from vista.escenas.escena_heuristica import EscenaHeuristica
from vista.ui_main_window import Ui_MainWindow
from vista.grafo.arista_grafico import AristaGrafico
from vista.grafo.nodo_grafico import NodoGrafico
from vista.grafo.grafo_scene import GrafoScene


class Vista(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(RUTAS_RECURSOS.IMAGENES.icono_ventana))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controlador = Controlador()
        self.escenas_heuristicas: dict[str, EscenaHeuristica] = {}

        self._configurar_interfaz()
        self._conectar_botones()
        self.centrar_ventana()

    def _configurar_interfaz(self):
        self.scene_B = GrafoScene(self.controlador)
        self.ui.graphicsView_base.setScene(self.scene_B)

        self.ui.widget_manhattan.setVisible(False)
        self.ui.widget_euclidiana.setVisible(False)
        self.ui.widget_base.setDisabled(True)

        self.ui.graphicsView_base.installEventFilter(self)
        self.ui.graphicsView_manhattan.installEventFilter(self)
        self.ui.graphicsView_euclidiana.installEventFilter(self)

        self.ui.graphicsView_manhattan.setDisabled(True)
        self.ui.graphicsView_euclidiana.setDisabled(True)
        self.ui.graphicsView_base.setDisabled(True)

        self.ui.widgetDatos.show()
        self.mostrar_widget_resultados_y_referencias(False)

        # Desactivar campos de datos
        self.ui.labelComboBox.setVisible(False)
        self.ui.comboBox.setVisible(False)
        item = self.ui.comboBox.model().item(0)
        item.setEnabled(False)

        self.ui.labelSpinBox.setVisible(False)
        self.ui.spinBox.setVisible(False)
        self.ui.pushButton_generar.setVisible(False)

        self.ui.infoButtonComboBox.setVisible(False)
        self.ui.infoButtonSpinBox.setVisible(False)

        self.ui.groupBoxInstrucciones.setVisible(False)
        self.activar_botones_pasos(False)
        self.mostrar_botones_archivo(False, False)

    def _configurar_graphicsView(self, activo: bool):
        for view in [self.ui.graphicsView_manhattan, self.ui.graphicsView_euclidiana, self.ui.graphicsView_base]:
            if activo:
                view.setEnabled(True)
                view.setInteractive(True)
                view.setDragMode(QtWidgets.QGraphicsView.DragMode.RubberBandDrag)
                view.viewport().setCursor(Qt.CursorShape.ArrowCursor)
            else:
                view.setEnabled(True)
                view.setInteractive(False)
                view.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)
                view.viewport().setCursor(Qt.CursorShape.OpenHandCursor)

    # Centrar la ventana
    def centrar_ventana(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Botones
    def _conectar_botones(self):
        self.ui.pushButtonPlay.clicked.connect(self.iniciar_algoritmo)
        self.ui.pushButtonPause.clicked.connect(self.pausar_algoritmo)
        self.findChild(QtWidgets.QPushButton, "pushButton_siguiente_paso").clicked.connect(self.avanzar_paso)
        self.findChild(QtWidgets.QPushButton, "pushButton_paso_atras").clicked.connect(self.retroceder_paso)
        self.findChild(QtWidgets.QPushButton, "pushButton_paso_inicial").clicked.connect(self.ir_al_paso_inicial)
        self.findChild(QtWidgets.QPushButton, "pushButton_ultimo_paso").clicked.connect(self.ir_a_ultimo_paso)
        self.findChild(QtWidgets.QPushButton, "pushButton_limpiar").clicked.connect(self.limpiar_escena)
        self.findChild(QtWidgets.QPushButton, "pushButton_cargar_archivo_grafo").clicked.connect(self.cargar_archivo_grafo)
        self.findChild(QtWidgets.QPushButton, "pushButton_guardar_archivo_grafo").clicked.connect(self.guardar_archivo_grafo)
        self.ui.pushButton_generar.clicked.connect(self.generar_grafo_aleatorio)

        self.ui.infoButtonComboBox.clicked.connect(self.mostrar_info_heuristica)
        self.ui.infoButtonModo.clicked.connect(self.mostrar_info_modo_generacion)
        self.ui.radioButtonManual.toggled.connect(self.activar_campos)
        self.ui.radioButtonAleatorio.toggled.connect(self.activar_campos)
        self.ui.infoButtonSpinBox.clicked.connect(self.mostrar_info_cantidad_nodos)

    def activar_botones_pasos(self, mostrar: bool):
        self.findChild(QtWidgets.QPushButton, "pushButton_siguiente_paso").setEnabled(mostrar)
        self.findChild(QtWidgets.QPushButton, "pushButton_paso_atras").setEnabled(mostrar)
        self.findChild(QtWidgets.QPushButton, "pushButton_paso_inicial").setEnabled(mostrar)
        self.findChild(QtWidgets.QPushButton, "pushButton_ultimo_paso").setEnabled(mostrar)

    # ---- Funcionalidades de los botones: Conexión con el controlador ----
    def iniciar_algoritmo(self):

        try:
            seleccion = self.ui.comboBox.currentText()
            nodos = self.controlador.obtener_nodos()

            if not self._validar_entrada(seleccion, nodos):
                return

            self.obtener_estados(nodos)
            self.ui.widgetDatos.hide()
            self.ui.pushButtonPlay.hide()
            self.ui.pushButtonPause.show()
            self.activar_botones_pasos(True)

            if seleccion == "Ambos":
                self.ejecutar_ambas_heuristicas()
            else:
                self.ejecutar_heuristica()

            self._configurar_graphicsView(False)

            self.agregar_referencias()
            self.mostrar_widget_resultados_y_referencias(True)
            self.inicializar_busquedas()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

    def _validar_entrada(self, seleccion, nodos):
        if not nodos:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No hay nodos disponibles.")
            return False
        if seleccion == "Selecciona una heurística":
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una heurística.")
            return False
        return True

    def inicializar_busquedas(self):
        for escena_heuristica in self.escenas_heuristicas.values():
            recorrido = self.controlador.comenzar_algoritmo(escena_heuristica.heuristica)
            escena_heuristica.graficar_grafo(recorrido)
        self.cargar_resultados()

    def avanzar_paso(self):
        for escena_heuristica in self.escenas_heuristicas.values():
            escena_heuristica.avanzar_paso()
        self.cargar_resultados()

    def retroceder_paso(self):
        for escena_heuristica in self.escenas_heuristicas.values():
            escena_heuristica.retroceder_paso()
        self.cargar_resultados()

    def ir_al_paso_inicial(self):
        for escena_heuristica in self.escenas_heuristicas.values():
            escena_heuristica.ir_al_paso_inicial()
        self.cargar_resultados()

    def ir_a_ultimo_paso(self):
        for escena_heuristica in self.escenas_heuristicas.values():
            escena_heuristica.ir_a_ultimo_paso()
        self.cargar_resultados()

    def pausar_algoritmo(self):
        self.controlador.pausar_algoritmo()
        self._configurar_graphicsView(True)
        seleccion = self.ui.comboBox.currentText()
        if seleccion == HEURISTICAS.distancia_euclidiana.texto:
            self.ui.widget_euclidiana.setVisible(False)
            self.ui.graphicsView_euclidiana.setScene(None)
        elif seleccion == HEURISTICAS.distancia_manhattan.texto:
            self.ui.widget_manhattan.setVisible(False)
            self.ui.graphicsView_manhattan.setScene(None)
        elif seleccion == "Ambos":
            self.ui.widget_euclidiana.setVisible(False)
            self.ui.widget_manhattan.setVisible(False)
            self.ui.graphicsView_euclidiana.setScene(None)
            self.ui.graphicsView_manhattan.setScene(None)

        self.ui.widget_base.setVisible(True)
        self.ui.widget_base.setDisabled(False)
        self.ui.graphicsView_base.setVisible(True)
        self.ui.graphicsView_base.setDisabled(False)
        self.ui.graphicsView_base.setScene(self.scene_B)
        self.scene_B.graficar_grafo(self.controlador.obtener_grafo())

        self.escenas_heuristicas.clear()

        self.ui.widgetDatos.show()
        self.ui.pushButtonPlay.show()
        self.ui.pushButtonPause.hide()
        self.activar_botones_pasos(False)
        self.ui.comboBox.setEnabled(True)
        self.mostrar_widget_resultados_y_referencias(False)
        self.mostrar_botones_archivo(self.ui.radioButtonManual.isChecked(), True)


    def obtener_estados(self, nodos):
        def orden_nodos(clave):
            return [int(texto) if texto.isdigit() else texto.lower() for texto in re.split(r'(\d+)', str(clave))]

        dialogo = QtWidgets.QDialog(self)
        dialogo.setWindowTitle("Seleccionar Estados")
        layout = QtWidgets.QVBoxLayout(dialogo)

        combo_inicial = QtWidgets.QComboBox()
        combo_objetivo = QtWidgets.QComboBox()
        nombres_nodos = [nodo.nombre for nodo in nodos]
        nombres_nodos.sort(key=orden_nodos)
        combo_inicial.addItems(nombres_nodos)
        combo_objetivo.addItems(nombres_nodos)

        layout.addWidget(QtWidgets.QLabel("Estado inicial:"))
        layout.addWidget(combo_inicial)
        layout.addWidget(QtWidgets.QLabel("Estado objetivo:"))
        layout.addWidget(combo_objetivo)

        btn_aceptar = QtWidgets.QPushButton("Aceptar")
        layout.addWidget(btn_aceptar)

        def aceptar():
            estado_inicial = combo_inicial.currentText()
            estado_objetivo = combo_objetivo.currentText()
            if estado_inicial == estado_objetivo:
                QtWidgets.QMessageBox.warning(dialogo, "Error", "El estado inicial y el objetivo deben ser distintos.")
            else:
                self.establecer_estados(estado_objetivo, estado_inicial)
                dialogo.accept()

        btn_aceptar.clicked.connect(aceptar)
        dialogo.exec()

    def establecer_estados(self, estado_objetivo, estado_inicial):
        nodo_inicial = self.controlador.obtener_nodo(estado_inicial)
        nodo_objetivo = self.controlador.obtener_nodo(estado_objetivo)

        self.controlador.establecer_nodo_inicio(nodo_inicial)
        self.controlador.establecer_nodo_objetivo(nodo_objetivo)

    def limpiar_escena(self):
        escena_base = self.ui.graphicsView_base.scene()
        for item in list(escena_base.items()):
            if isinstance(item, (NodoGrafico, AristaGrafico)):
                escena_base.removeItem(item)

        self.controlador.restablecer_grafo()

        self.scene_B.deseleccionar_nodo_para_conectar()

        self.ui.widgetDatos.show()
        self.ui.pushButtonPlay.show()
        self.ui.pushButtonPause.hide()
        self.mostrar_widget_resultados_y_referencias(False)
        self.mostrar_botones_archivo(self.ui.radioButtonManual.isChecked(), True)
        self.activar_botones_pasos(False)

        self.ui.widget_base.setDisabled(False)
        self.ui.widget_base.setVisible(True)
        self.ui.graphicsView_base.setDisabled(False)
        self.ui.graphicsView_base.setVisible(True)

        self.ui.comboBox.setCurrentIndex(0)

        self.ui.widget_manhattan.setVisible(False)
        self.ui.graphicsView_manhattan.setDisabled(True)

        self.ui.widget_euclidiana.setVisible(False)
        self.ui.graphicsView_euclidiana.setDisabled(True)
        self._configurar_graphicsView(True)

    def generar_grafo_aleatorio(self):
        grafo = self.controlador.generar_grafo_aleatorio(self.ui.spinBox.value(), self.ui.graphicsView_base.width(), self.ui.graphicsView_base.height())
        self.scene_B.deseleccionar_nodo_para_conectar()
        self.scene_B.graficar_grafo(grafo)

    # ---- Interacciones con la UI ----
    def activar_campos(self):
        self.ui.groupBoxInstrucciones.setVisible(True)

        modo_aleatorio = self.ui.radioButtonAleatorio.isChecked()
        modo_manual = self.ui.radioButtonManual.isChecked()

        self.ui.infoButtonSpinBox.setVisible(modo_aleatorio)
        self.ui.labelSpinBox.setVisible(modo_aleatorio)
        self.ui.spinBox.setVisible(modo_aleatorio)
        self.ui.pushButton_generar.setVisible(modo_aleatorio)

        self.ui.widget_base.setDisabled(False)
        self.ui.graphicsView_base.setDisabled(False)

        self.mostrar_botones_archivo(modo_manual, True)

        self.ui.infoButtonComboBox.setVisible(True)
        self.ui.labelComboBox.setVisible(True)
        self.ui.comboBox.setVisible(True)

        if modo_manual:
            titulo = "Pasos para dibujar el grafo:"
            instrucciones =  [
                "<b>1.</b> Haz clic en el área para agregar nodos.",
                "<b>2.</b> Haz doble clic en un nodo y luego en otro para conectarlos mediante una arista e ingresar su costo.",
                "<b>3.</b> Selecciona la heurística que desees utilizar.",
                "<b>4.</b> Haz clic en 'Play' para ejecutar el algoritmo."
            ]
        else:
            titulo = "Pasos para generar el grafo:"
            instrucciones = [
                "<b>1.</b> Ingrese la cantidad de nodos y presione el botón 'Generar grafo'",
                "<b>2.</b> Selecciona la heurística.",
                "<b>3.</b> Haz clic en 'Play' para ejecutar el algoritmo."
            ]
        self.ui.groupBoxInstrucciones.setTitle(titulo)
        self.actualizar_instrucciones(instrucciones)

    def actualizar_instrucciones(self, instrucciones):
        while self.ui.layoutInstrucciones.count():
            item = self.ui.layoutInstrucciones.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for texto in instrucciones:
            label = QtWidgets.QLabel()
            label.setTextFormat(QtCore.Qt.TextFormat.RichText)  # Permitir HTML
            label.setWordWrap(True)
            label.setText(texto)
            self.ui.layoutInstrucciones.addWidget(label)

    def mostrar_widget_resultados_y_referencias(self, mostrar: bool):
        self.ui.horizontalLayout_2.setEnabled(mostrar)
        self.ui.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        for i in range(self.ui.horizontalLayout_2.count()):
            item = self.ui.horizontalLayout_2.itemAt(i).widget()
            if item:
                item.setVisible(False)

        self.ui.widget_euclidianaResults.setVisible(False)
        self.ui.widget_manhattanResults.setVisible(False)
        self.ui.widget_referencia.setVisible(False)

        if mostrar:
            self.ui.widget_referencia.setVisible(True)
            self.ui.layoutContenedorP.setStretch(0, 1)
            self.ui.layoutContenedorP.setStretch(1, 10)
            self.ui.layoutContenedorP.setStretch(2, 2)

            seleccion = self.ui.comboBox.currentText()
            if seleccion == HEURISTICAS.distancia_euclidiana.texto:
                self.ui.widget_euclidianaResults.setVisible(True)
                self.inicializar_tabla_resultados(self.ui.table_euclidiana)
            elif seleccion == HEURISTICAS.distancia_manhattan.texto:
                self.ui.widget_manhattanResults.setVisible(True)
                self.inicializar_tabla_resultados(self.ui.table_manhattan)
            elif seleccion == "Ambos":
                self.ui.widget_manhattanResults.setVisible(True)
                self.ui.widget_euclidianaResults.setVisible(True)
                self.inicializar_tabla_resultados(self.ui.table_euclidiana)
                self.inicializar_tabla_resultados(self.ui.table_manhattan)
        else:
            self.ui.layoutContenedorP.setStretch(0, 0)
            self.ui.layoutContenedorP.setStretch(1, 1)
            self.ui.layoutContenedorP.setStretch(2, 0)

    def agregar_referencias(self):
        colores = [
            ("#ef233c", "Inicio"),
            ("#EE9B00", "Actual"),
            ("#ced4da", "Cerrado"),
            ("#48cae4", "Abierto"),
            ("#0077b6", "Abierto Mejor"),
            ("#ff5a5f", "Camino"),
            ("#487575", "Default")
        ]

        count = self.ui.layout_widget_referencia.count()
        for i in reversed(range(1, count)):
            item = self.ui.layout_widget_referencia.takeAt(i)
            if item.widget():
                item.widget().deleteLater()

        for color, texto in colores:
            widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(5)

            label_color = QtWidgets.QLabel()
            label_color.setFixedSize(18, 18)
            label_color.setStyleSheet(f"""
                background-color: {color};
                border-radius: 9px;
                border: 1px solid black;
            """)

            label_texto = QtWidgets.QLabel(texto)
            label_texto.setStyleSheet("font-size: 14px; font-weight: normal;")

            layout.addWidget(label_color)
            layout.addWidget(label_texto)

            self.ui.layout_widget_referencia.addWidget(widget)

    def inicializar_tabla_resultados(self, tabla):
        tabla.setRowCount(1)
        tabla.setColumnCount(6)

        valores_iniciales = ["0", "0", "0.00", "-", "-", "-"]

        for col, valor in enumerate(valores_iniciales):
            item = QtWidgets.QTableWidgetItem(valor)
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            tabla.setItem(0, col, item)

        tabla.resizeColumnsToContents()

    def actualizar_tabla_resultados(self, tabla, resultados: ResultadosAlgoritmo):
        try:
            datos = [
                str(resultados.nro_paso),
                str(resultados.cantidad_nodos_explorados),
                f"{float(resultados.costo_total):.2f}" if resultados.costo_total is not None else "-",
                f"{float(resultados.tiempo_total):.4f} seg" if resultados.tiempo_total is not None else "-",
                " → ".join(resultados.ruta) if isinstance(resultados.ruta, list) else "No encontrado",
                "✓" if resultados.objetivo_alcanzado else "✗"
            ]

            tabla.clearContents()
            tabla.setRowCount(1)

            for col, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(valor)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if col == 5:
                    item.setForeground(QColor("green") if valor == "✓" else QColor("red"))
                tabla.setItem(0, col, item)

            tabla.resizeColumnsToContents()
        except Exception as e:
            print(f"Error al actualizar tabla: {str(e)}")
            self.inicializar_tabla_resultados(tabla)

    def cargar_resultados(self):
        try:
            seleccion = self.ui.comboBox.currentText()
            if not seleccion:
                return

            if seleccion in [HEURISTICAS.distancia_euclidiana.texto, "Ambos"]:
                resultados = self.controlador.obtener_resultados_algoritmo(HEURISTICAS.distancia_euclidiana.nombre)
                if resultados:
                    self.actualizar_tabla_resultados(self.ui.table_euclidiana, resultados)

            if seleccion in [HEURISTICAS.distancia_manhattan.texto, "Ambos"]:
                resultados = self.controlador.obtener_resultados_algoritmo(HEURISTICAS.distancia_manhattan.nombre)
                if resultados:
                    self.actualizar_tabla_resultados(self.ui.table_manhattan, resultados)

        except Exception as e:
            print(f"Error al cargar resultados: {str(e)}")
            QtWidgets.QMessageBox.warning(self, "Error", f"No se pudieron cargar los resultados: {str(e)}")

    def ejecutar_heuristica(self):
        seleccion = self.ui.comboBox.currentText()
        scene_heuristica = GrafoScene(self.controlador)

        self.ui.widget_euclidiana.setVisible(False)
        self.ui.widget_manhattan.setVisible(False)
        self.ui.graphicsView_euclidiana.setDisabled(True)
        self.ui.graphicsView_manhattan.setDisabled(True)
        self.ui.widget_base.setVisible(False)
        self.ui.graphicsView_base.setVisible(False)

        if seleccion == HEURISTICAS.distancia_euclidiana.texto:
            self.ui.widget_euclidiana.setVisible(True)
            self.ui.graphicsView_euclidiana.setDisabled(True)
            self.ui.graphicsView_euclidiana.setScene(scene_heuristica)
            self.escenas_heuristicas[HEURISTICAS.distancia_euclidiana.nombre] = (
                EscenaHeuristica(self.controlador, scene_heuristica, HEURISTICAS.distancia_euclidiana.nombre))
        elif seleccion == HEURISTICAS.distancia_manhattan.texto:
            self.ui.widget_manhattan.setVisible(True)
            self.ui.graphicsView_manhattan.setDisabled(True)
            self.ui.graphicsView_manhattan.setScene(scene_heuristica)
            self.escenas_heuristicas[HEURISTICAS.distancia_manhattan.nombre] = (
                EscenaHeuristica(self.controlador, scene_heuristica, HEURISTICAS.distancia_manhattan.nombre))

    def ejecutar_ambas_heuristicas(self):
        scene_linea_recta = GrafoScene(self.controlador)
        scene_manhattan = GrafoScene(self.controlador)

        self.ui.graphicsView_euclidiana.setScene(scene_linea_recta)
        self.ui.graphicsView_manhattan.setScene(scene_manhattan)

        self.ui.graphicsView_euclidiana.setDisabled(True)
        self.ui.widget_base.setDisabled(False)
        self.ui.widget_euclidiana.setVisible(True)
        self.ui.widget_manhattan.setVisible(True)
        self.ui.graphicsView_manhattan.setDisabled(True)
        self.ui.widget_base.setVisible(False)

        self.escenas_heuristicas[HEURISTICAS.distancia_euclidiana.nombre] = (
            EscenaHeuristica(self.controlador, scene_linea_recta, HEURISTICAS.distancia_euclidiana.nombre))
        self.escenas_heuristicas[HEURISTICAS.distancia_manhattan.nombre] = (
            EscenaHeuristica(self.controlador, scene_manhattan, HEURISTICAS.distancia_manhattan.nombre))

    # Guia de usuario
    def mostrar_info_cantidad_nodos(self):
        QtWidgets.QMessageBox.information(
            None, "Información - Cantidad de Nodos",
            "Define cuántos nodos tendrá el grafo a generar"
        )

    def mostrar_info_modo_generacion(self):
        QtWidgets.QMessageBox.information(
            None, "Información - Modo de Generación",
            "Manual: creas los nodos y conexiones con click.\n"
            "Aleatorio: generar un grafo aleatorio automáticamente a partir de una cantidad de nodos dada."
        )

    def mostrar_info_heuristica(self):
        QtWidgets.QMessageBox.information(
            None, "Información - Heurística",
            "Selecciona el tipo de heurística que se utilizará para calcular el camino."
        )

    def mostrar_botones_archivo(self, modo_manual: bool, modo_ambos:bool):
        self.ui.pushButtonCargarArchivo.setVisible(modo_manual)
        self.ui.pushButtonGuardarArchivo.setVisible(modo_ambos)

    def cargar_archivo_grafo(self):
        path, _ = QFileDialog.getOpenFileName(None, "Cargar Grafo", "", "Archivos JSON (*.json)")
        grafo_cargado = self.controlador.cargar_archivo_grafo(path)
        if grafo_cargado:
            self.scene_B.deseleccionar_nodo_para_conectar()
            self.scene_B.graficar_grafo(self.controlador.obtener_grafo())
        else:
            dialogo = QtWidgets.QDialog(self)
            dialogo.setWindowTitle("Cargar Grafo")
            QtWidgets.QMessageBox.warning(dialogo, "Error", "No se pudo cargar el grafo del archivo seleccionado.")

    def guardar_archivo_grafo(self):
        path, _ = QFileDialog.getSaveFileName(None, "Guardar Grafo", "", "Archivos JSON (*.json)")
        grafo_guardado = self.controlador.guardar_archivo_grafo(path)
        if not grafo_guardado:
            dialogo = QtWidgets.QDialog(self)
            dialogo.setWindowTitle("Guardar Grafo")
            QtWidgets.QMessageBox.warning(dialogo, "Error", "No se pudo guardar el grafo.")

    def eventFilter(self, source, event): # zoom para los graphicsView
        if isinstance(source, QtWidgets.QGraphicsView):
            # zoom con Ctrl + rueda del mouse
            if event.type() == QtCore.QEvent.Type.Wheel and QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.KeyboardModifier.ControlModifier:
                zoom_factor = 1.15
                if event.angleDelta().y() > 0:
                    source.scale(zoom_factor, zoom_factor)
                else:
                    source.scale(1 / zoom_factor, 1 / zoom_factor)
                return True

            # doble clic para resetear zoom
            elif event.type() == QtCore.QEvent.Type.MouseButtonDblClick:
                source.resetTransform()
                return True

        return super().eventFilter(source, event)

