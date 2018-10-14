import matplotlib.pyplot as plt
from .grafos import *

def mapeoarbol(grafo, arbol, camino):
	plt.title("MAPA DE RUTAS")
	plt.xlabel("Longitud")
	plt.ylabel("Latitud")
	plt.axis([grafo.xmin, grafo.xmax, grafo.ymin, grafo.ymax])
	#grafo
	print("impresion de calles")
	imprimirCalles(grafo.conj_aristas, grafo)
	#kruskal
	print("impresion de arbol de kruskal")
	imprimirCalles(arbol, grafo, 'm')
	#impresion de dijkstra
	print("impresion de camino de dijkstra")
	imprimirDijkstra(camino, grafo)
	plt.show()

def imprimirCalles(conjunto, grafo, color = 'y'):
	i = 0
	for tupla in conjunto:
		peso, id1, id2 = tupla
		nd1, nd2 = grafo.dic_vertices[id1], grafo.dic_vertices[id2]
		x1, y1, x2, y2 = nd1.x, nd1.y, nd2.x, nd2.y
		if i % 550 == 0: print("cargando...")
		i += 1
		plt.plot([x1, x2], [y1, y2], color)

def imprimirDijkstra(camino, grafo):
	i = 0
	while(len(camino)):
		node = camino.pop()
		node_origin = grafo.dic_vertices[node.etiqueta[0]]
		x1, y1, x2, y2 = node.x, node.y, node_origin.x, node_origin.y
		if i % 550 == 0: print("cargando...")
		i += 1
		plt.plot([x1, x2], [y1, y2], "g", linewidth=5)
