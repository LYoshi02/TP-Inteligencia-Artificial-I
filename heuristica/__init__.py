from heuristica import heuristica_manhattan, heuristica_linea_recta, heuristica_ambas

nodo_actual = (2, 3)
nodo_objetivo = (5, 7)

print("Manhattan:", heuristica_manhattan(nodo_actual, nodo_objetivo))
print("Línea recta:", heuristica_linea_recta(nodo_actual, nodo_objetivo))
print("Ambas:", heuristica_ambas(nodo_actual, nodo_objetivo))