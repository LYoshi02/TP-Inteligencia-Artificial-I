import os, sys
from dataclasses import dataclass

def obtener_ruta_archivo(rel_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

@dataclass
class Estilos:
    style_qss: str

@dataclass
class Imagenes:
    flecha_doble_derecha: str
    flecha_doble_izquierda: str
    flecha_paso_inicial: str
    flecha_ultimo_paso: str
    escoba: str
    informacion: str
    pausa: str
    play: str

@dataclass
class RutasRecursos:
    ESTILOS: Estilos
    IMAGENES: Imagenes

RUTAS_RECURSOS = RutasRecursos(
    ESTILOS=Estilos(
        style_qss=obtener_ruta_archivo("vista/styles/style.qss")
    ),
    IMAGENES=Imagenes(
        flecha_doble_derecha=obtener_ruta_archivo("vista/images/icons8-doble-derecha-52.png"),
        flecha_doble_izquierda=obtener_ruta_archivo("vista/images/icons8-doble-izquierda-52.png"),
        flecha_paso_inicial=obtener_ruta_archivo("vista/images/icons8-primero-1-52.png"),
        flecha_ultimo_paso=obtener_ruta_archivo("vista/images/icons8-skip-forward-52.png"),
        escoba=obtener_ruta_archivo("vista/images/icons8-escoba-48.png"),
        informacion=obtener_ruta_archivo("vista/images/icons8-información-50.png"),
        pausa=obtener_ruta_archivo("vista/images/icons8-pausa-50.png"),
        play=obtener_ruta_archivo("vista/images/icons8-play-30.png")
    )
)
