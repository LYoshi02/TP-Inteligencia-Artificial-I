# TP Inteligencia Artificial I - Comparativa de Heurísticas con Algoritmo A*

## Sobre el Proyecto
El **algoritmo A*** es un algoritmo de búsqueda ampliamente utilizado para encontrar un camino entre un nodo inicial y un nodo objetivo en un grafo. Utiliza una función heurística para determinar en cada instante por cuál nodo se debe continuar explorando.

En este proyecto realizamos una implementación del algoritmo A* aplicando las heurísticas de distancia Euclidiana y Manhattan. El programa permite construir gráficamente el grafo a procesar, generar grafos aleatorios, elegir la/s heurística/s a aplicar, visualizar el paso a paso del funcionamiento del algoritmo y los resultados obtenidos de la búsqueda.

## Instalación Local
1. Clonar el repositorio.
```bash
git clone https://github.com/LYoshi02/TP-Inteligencia-Artificial-I.git
cd TP-Inteligencia-Artificial-I
```
2. Instalar las dependencias.
```bash
pip install -r requirements.txt
```
3. Ejecutar el programa.
```bash
python main.py
```


## Instrucciones de Uso
El programa cuenta con 2 modos de generación de grafos que se pueden seleccionar desde la barra lateral izquierda:
-   Modo manual: permite construir un grafo creando los nodos y aristas manualmente.
-   Modo aleatorio: permite generar un grafo con nodos y aristas aleatorias de manera automática a partir de la cantidad de nodos ingresada.

Para cada uno de los modos es posible seleccionar entre las heurísticas de distancia Euclidiana y Manhattan desde la barra lateral izquierda. También es posible seleccionar ambas a la vez.

### Modo Manual
Para generar el grafo en el modo manual se deben seguir los siguientes pasos:
1. Hacer click en el área central para agregar nodos. Se solicitará el ingreso de un nombre que identifique al nodo.
2.  Hacer doble clic en un nodo y luego en otro para conectarlos mediante una arista e ingresar el costo entre ambos.
3.  Seleccionar la heurística que desees ver.
4.  Hacer click en el botón de “Play” de la barra lateral derecha.
5.  Ingresar el nodo inicial y el nodo objetivo para comenzar la ejecución del algoritmo

### Modo Aletorio
Para generar el grafo en el modo aleatorio se deben seguir los siguientes pasos:
1. Ingresar la cantidad de nodos deseados y presionar el botón “Generar grafo”.
2. Seleccionar la heurística que desees ver.
3. Hacer click en el botón de “Play” de la barra lateral derecha.
4. Ingresar el nodo inicial y el nodo objetivo para comenzar la ejecución del algoritmo

### Acciones
Grafo:
-   Se puede hacer zoom al grafo manteniendo presionada la tecla CTRL y scrolleando la rueda del mouse hacia arriba o hacia abajo.

Nodos:
-   Se puede mover un nodo haciendo doble click en el mismo y arrastrándolo hacia la ubicación deseada.
-   Se puede eliminar un nodo haciendo click derecho sobre el mismo y seleccionando la opción “Eliminar nodo”.

Aristas:
-   Se puede actualizar la distancia de una arista haciendo click derecho sobre la misma y seleccionando la opción “Actualizar costo”.
-   Se puede eliminar una arista haciendo click derecho sobre la misma y seleccionando la opción “Eliminar arista”.

### Ejecución del Algoritmo
Una vez se comienza la ejecución del algoritmo, se puede visualizar el paso a paso del algoritmo A* utilizando los botones de la barra lateral derecha:
-   Pausar algoritmo: detiene el proceso de búsqueda y regresa a la pantalla anterior para modificar el grafo generado.
-   Retroceder atrás: va al paso anterior del algoritmo.
-   Avanzar paso: va al paso siguiente del algoritmo.
-   Ir al paso inicial: retrocede al primer paso del algoritmo.
-   Ir al último paso: avanza hasta el último paso del algoritmo.
-   Borrar grafo: borra el grafo actual y regresa a la pantalla anterior para construir un nuevo grafo.

## Tecnologías Utilizadas
**Lenguaje de Programación:**
 - Python v3.13

**Librerías:**
 - PyQt6: utilizada para la creación de Interfaces Gráficas de Usuario (GUI) usando las funcionalidades de la librería Qt en Python.
 - NetworkX:  permite la creación, manipulación y estudio de grafos y análisis de redes. Usada dentro del proyecto para la generación de grafos aleatorios.
- PyInstaller: utilizada para convertir el programa en un ejecutable de Windows (.exe).

## Autores
 - Debat, Yoshi
 - Nürnberg, Sofía
 - Terleski, Isaac
