'''
Created on 19 apr. 2018

@author: Catalin
'''

def shortestPath(graph, s, t):
    """
    function that searches for the shortest path between two vertices in a directed graph
    input: a graph, s - starting vertex, t - destination vertex
    output: the path as a list of vertices or None if no path exists
    """
    dist=bfs(graph,s)
    return retrivePath(graph, dist, s, t)
    
def bfs(graph, s):
    """
    breadth first search algorithm
    input: a graph, s - starting vertex
    output: a dictionary where the keys are accessible vertices and the value is the distance from the staring vertex 
    """
    dist={s:0}
    queue=[]
    queue.append(s)
    while (len(queue)!=0):
        vertex=queue.pop(0)
        for x in graph.get_outbound_of(vertex):
            if x not in dist.keys():
                dist[x]=1+dist[vertex]
                queue.append(x)
    return dist

def retrivePath(graph, dist, s, t):
    """
    function that returns the shortest path between a starting vertex and a ending vertex
    input: a graph, dist - dictionary where the keys are accessible vertices and the value is the distance from the staring vertex , s - starting vertex, t - ending vertex
    output: the path as a list of vertices or None if no path exists
    """
    path=[t]
    while t!=s:
        if len(graph.get_inbound_of(t))==0:
            raise ValueError("no path")
        for vertex in graph.get_inbound_of(t):
            try:
                if dist[vertex]==dist[t]-1:
                    path.append(vertex)
                    t=vertex
                    break
            except KeyError:
                raise ValueError("no path")
    path.reverse()
    return path
    