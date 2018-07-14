from os import path
from .parseOsm import *
from .grafos import *
from .kruskal import kruskal
from .dijkstra import dijkstra
from .depuracion import depurar
# from grafico import mapeoarbol

archivo = path.join(path.dirname(__file__), "map.osm")
depurar(archivo)
archivo2 = "modificado.xml"
grafo = grafoOSM(archivo2)
arbol = kruskal(grafo)

def ruteo(p1, p2):
    [lat1, lon1] = p1
    [lat2, lon2] = p2
    """ruta es una lista de coordenadas(tuplas)"""
    return ruta(lat1, lon1, lat2, lon2, grafo, arbol)

def ruta(lat1, lon1, lat2, lon2, grafo, arbol):
    id1 = encuentra_punto(grafo, lat1, lon1)
    id2 = encuentra_punto(grafo, lat2, lon2)
    camino = dijkstra(grafo, arbol, id1, id2)
    return transformar_ruta(camino)

def encuentra_punto(grafo, lat, lon):
    vertices = grafo.dic_vertices.values()
    distances = [(v,  (v.x - lon)**2 + (v.y - lat)**2) for v in vertices]

    closer, distance = distances[0]
    for v, d in distances:
        if d < distance:
            closer, distance = v, d

    print('Punto: ', closer, 'id: ', closer.id)
    return closer.id

def transformar_ruta(camino):
    return [(nodo.y, nodo.x) for nodo in camino]
