'''
Created on 3 mai 2018

@author: Catalin
'''
import heapq

def retrievePath(prev, start):
    '''
    function that computes the path between the starting vertex and the ending vertex
    input: prev - dictionary of child vertices, start - starting vertex
    output: path - the path as a list of nodes
    '''
    path = []
    if start not in prev:
        return None
    while start != None:
        path.append(start)
        start = prev[start]
    return path
    
def dijkstraPath(graph, start, final, costs):
    '''
    function that computes the minimum cost path between 2 vertices, starting the computation from the ending vertex
    input: graph - directed graph, start - starting vertex, final - ending vertex, costs - dictionary with keys tuples of vertices and values the cost of the edge
                                                                                           from vertex1 to vertex2
    output: a tuple containing the list of vertices of the path and the cost of the path
    '''
    dist ={}
    prev ={}
    prev[final]=None
    q=[]
    dist[final]=0
    heapq.heappush(q, (dist[final], final))
    while len(q)>0:
        dummy, x=heapq.heappop(q)
        if(dummy == dist[x]):
            for y in graph.get_inbound_of(x):
                if y not in prev or dist[y]>dist[x]+costs[(y,x)]:
                    prev[y]=x
                    dist[y]=dist[x]+costs[(y,x)]
                    heapq.heappush(q, (dist[y], y))
    try:                
        return retrievePath(prev, start), dist[start]
    except KeyError:
        raise ValueError("no such path")
    
def bellman(graph,costs,edges,s,t):
    dist=dict()
    prev=dict()
    for x in graph.getNodes():
        dist[x]=9999;
    dist[s]=0;
    prev[s]=None;
    changed=True;
    while changed:
        changed=False
        for (x,y) in edges:
            if dist[y]>dist[x]+costs[(x,y)]:
                dist[y]=dist[x]+costs[(x,y)]
                prev[y]=x
                changed=True
    return retrievePath(prev, t), dist[t]

def highestcostwalk(graph, sortl, s, t):
    costs=[0]*len(graph.getNodes())
    
    