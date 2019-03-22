'''
Created on 16 mai 2018

@author: Catalin
'''
def TopoDFS(graph, vertex, sortl, fullyProcessed, inProcess):
    inProcess.add(vertex)
    for y in graph.get_inbound_of(vertex):
        if y in inProcess:
            return False
        elif y not in fullyProcessed:
            ok=TopoDFS(graph,y,sortl,fullyProcessed,inProcess)
            if not ok:
                return False
    inProcess.remove(vertex)
    sortl.append(vertex)
    fullyProcessed.add(vertex)
    return True

def TopoAlg(graph):
    '''
    function that computes topological sorting of a graph
    input: graph
    output: the list of topological sorted vertices
    '''
    sortl=[]
    fullyProcessed=set()
    inProcess=set()
    nds=graph.getNodes()
    for x in nds:
        if x not in fullyProcessed:
            ok=TopoDFS(graph, x, sortl, fullyProcessed, inProcess)
            if not ok:
                return 0
    return sortl
