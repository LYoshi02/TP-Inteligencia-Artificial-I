from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtGui import QWindow, QIcon
import os

def cargar_interfaz(engine, backend):
    ruta = os.path.abspath("resources/AiApp/AiAppContent/App.qml")

    print(f"Ruta del archivo QML: {ruta}")

    try:
        engine.load(QUrl.fromLocalFile(ruta))
    except Exception as e:
        print(f"Error al cargar el archivo QML: {e}")
        return

    if not engine.rootObjects():
        print("No se encontró la ventana.")
        return

    ventana = engine.rootObjects()[0]
    icono = QIcon(os.path.abspath("resources/AiApp/AiAppContent/images/estrellaIcon.png"))
    ventana.setIcon(icono)

    ancho_fijo = 1200
    alto_fijo = 700
    ventana.setMinimumWidth(ancho_fijo)
    ventana.setMaximumWidth(ancho_fijo)
    ventana.setMinimumHeight(alto_fijo)
    ventana.setMaximumHeight(alto_fijo)

    ventana.setFlags(
        Qt.WindowType.Window |
        Qt.WindowType.WindowMinimizeButtonHint |
        Qt.WindowType.WindowCloseButtonHint |
        Qt.WindowType.WindowTitleHint
    )

    # engine.rootContext().setContextProperty("backend", backend)
