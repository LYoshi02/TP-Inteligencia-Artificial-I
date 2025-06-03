import sys
from PyQt6.QtWidgets import QApplication

from constantes.recursos import RUTAS_RECURSOS
from vista.vista import Vista

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open(RUTAS_RECURSOS.ESTILOS.style_qss, "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    window = Vista()

    # Mostramos la ventana
    window.show()

    # Ejecutamos la aplicación
    sys.exit(app.exec())

