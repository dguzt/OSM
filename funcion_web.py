from parseOsm import *
from grafos import *
from kruskal import kruskal
from dijkstra import dijkstra
from depuracion import depurar
# from grafico import mapeoarbol

def funcion_web(lat1, lon1, lat2, lon2):
    grafo = Grafo()
    archivo = "map.osm"
    depurar(archivo)
    archivo2 = "modificado.xml"
    grafo = Grafo()
    grafo = grafoOSM(archivo2)
    arbol = kruskal(grafo)
    """ruta es una lista de coordenadas(tuplas)"""
    return ruta(lat1, lon1, lat2, lon2, grafo, arbol)

def ruta(lat1, lon1, lat2, lon2, grafo, arbol):
    id1 = encuentra_punto(lat1, lon1)
    id2 = encuentra_punto(lat2, lon2)
    camino = dijkstra(grafo, arbol, id1, id2)
    return transformar_ruta(camino)

def encuentra_punto(lat, lon):
    #ccc

def transformar_ruta(camino):
    #ccc
