from grafos import *
from kruskal import kruskal
from dijkstra import dijkstra
from grafico import mapeoarbol

grafo = Grafo()

grafo.ymin = 0
grafo.ymax = 14
grafo.xmin = 0
grafo.xmax = 14

# ALMACENAMIENTO DE NODOS EN GRAFO
nd1 = Vertice(1)
nd1.x = 3
nd1.y = 4
grafo.agregarVertice(nd1)
nd2 = Vertice(2)
nd2.x = 4
nd2.y = 4
grafo.agregarVertice(nd2)
nd3 = Vertice(3)
nd3.x = 7
nd3.y = 8
grafo.agregarVertice(nd3)
nd4 = Vertice(4)
nd4.x = 7
nd4.y = 4
grafo.agregarVertice(nd4)
nd5 = Vertice(5)
nd5.x = 7
nd5.y = 2
grafo.agregarVertice(nd5)
nd6 = Vertice(6)
nd6.x = 4
nd6.y = 4
grafo.agregarVertice(nd6)
nd7 = Vertice(7)
nd7.x = 12
nd7.y = 4
grafo.agregarVertice(nd7)

# ALMACENAMIENTO DE CALLES EN GRAFO
grafo.conj_aristas.add((1,1,2))
grafo.conj_aristas.add((5,2,3))
grafo.conj_aristas.add((3,2,4))
grafo.conj_aristas.add((4,3,4))
grafo.conj_aristas.add((2,4,5))
grafo.conj_aristas.add((2,4,6))
grafo.conj_aristas.add((3,6,7))

# PRUEBA
arbol = kruskal(grafo)
print("fin de kruskal")

camino = dijkstra(grafo, arbol)
print("fin de dijkstra")
print(camino)

mapeoarbol(grafo, arbol, camino)
print("fin de grafico de mapa")

print("FIN")
