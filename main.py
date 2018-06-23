from parseOsm import *
from grafos import *
from kruskal import kruskal
from dijkstra import dijkstra
from grafico import mapeoarbol
from depuracion import depurar
grafo = Grafo()

archivo = "map.osm"

depurar(archivo)
print("fin de depuracion")

archivo2 = "modificado.xml"
grafo = Grafo()
grafo = grafoOSM(archivo2)
print("fin de procesamiento de datos OSM")
# PRUEBA
arbol = kruskal(grafo)
print("fin de kruskal")

camino = dijkstra(grafo, arbol)
print("fin de dijkstra")

mapeoarbol(grafo, arbol, camino)
print("fin de grafico de mapa")

print("FIN")
