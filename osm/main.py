from parseOsm import *
from grafos import *
from kruskal import kruskal
from dijkstra import dijkstra
from grafico import mapeoarbol
from depuracion import depurar

def main():
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
    idA = encuentra_punto(grafo, -12.066159, -77.073635) # -12.071697, -77.076262)
    assert idA in grafo.dic_vertices.keys(), "idA no se encuentra dentro del grafo"
    idB = encuentra_punto(grafo, -12.072115, -77.072334 ) # -12.070534, -77.066984) # -12.086531, -77.063292)
    assert idB in grafo.dic_vertices.keys(), "idB no se encuentra dentro del grafo"
    camino = dijkstra(grafo, arbol,idA, idB)
    print("fin de dijkstra")
    mapeoarbol(grafo, arbol, camino)
    print("fin de grafico de mapa")
    print("FIN")


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
    return closer.id


def transformar_ruta(camino):
    return [(nodo.y, nodo.x) for nodo in camino]


if __name__ == "__main__":
    main()
