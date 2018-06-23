from grafos import *

def barrido_kruskall(grafo, arbol, idA):
    for peso, id1, id2 in arbol:
        grafo.dic_vertices[id1].dic_veci[id2] = peso
        grafo.dic_vertices[id2].dic_veci[id1] = peso

def dijkstra(grafo, arbol, idA, idB):
    # idA = "316802007"  # obtener_nodo() # funcion que pide el nodo a la pagina
    # idB = "660657169"  # obtener_nodo()
    barrido_kruskall(grafo, arbol, idA) #correcto

    """ETIQUETADO DE NODOS DE ACUERDO A DIJKSTRA"""
    cola = []
    nodo = grafo.dic_vertices[idA]
    nodo.etiqueta = (idA, 0)
    id_ant = 0
    cola.append((nodo, id_ant))
    while(len(cola)):
        nodo, id_ant = cola.pop(0)
        for id in nodo.dic_veci:
            if(id_ant == id): continue # no se toma el vecino de donde proviene
            vecino = grafo.dic_vertices[id]
            if (nodo.dic_veci[id] + nodo.etiqueta[1]) <= vecino.etiqueta[1]:
                vecino.etiqueta = (nodo.id, nodo.dic_veci[id] + nodo.etiqueta[1])
            cola.append((vecino, nodo.id))

    """RETORNO DEL CAMINO"""
    camino = []
    id = idB
    while(1):
        if(idA == id): break
        node = grafo.dic_vertices[id]
        camino.append(node)
        id = node.etiqueta[0] # id de donde proviene

    return camino
