from PyQt6.QtCore import QUrl
from PyQt6.QtQml import QQmlApplicationEngine
import os


def cargar_interfaz(engine, backend):

    ruta_absoluta = os.path.abspath("resources/AiApp/AiAppContent/App.qml")
    print(f"Ruta del archivo QML: {ruta_absoluta}")

    try:
        engine.load(QUrl.fromLocalFile(ruta_absoluta))
    except Exception as e:
        print(f"Error al cargar el archivo QML: {e}")
        return

    # vincular con el backend
    # engine.rootContext().setContextProperty("backend", backend)
