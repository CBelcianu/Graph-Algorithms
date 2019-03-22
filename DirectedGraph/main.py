'''
Created on 15 mar. 2018

@author: Catalin
'''
from graph import Digraph
from BreadthFirstSearch import shortestPath
from Dijkstra import dijkstraPath, bellman, highestcostwalk
from DAG import TopoAlg

def ReadGraph(diGraph, fileName="graph3.txt"):
    f = open(fileName, "r")
    line = f.readline().strip()
    attrs = line.split(" ")
    attrs[0] = int(attrs[0])
    attrs[1] = int(attrs[1])
    for i in range(attrs[0]):
        diGraph.add_node(i)
    line = f.readline().strip()
    while line != "":
            attrs = line.split(" ")
            attrs[0] = int(attrs[0])
            attrs[1] = int(attrs[1])
            attrs[2] = int(attrs[2])
            diGraph.add_arc(attrs[0], attrs[1], attrs[2])
            line = f.readline().strip()
    f.close()
    
def printMenu():
    print("\t1.Get the number of vertices")
    print("\t2.Given two vertices, find out whether there is an edge from the first one to the second one")
    print("\t3.Get the in degree and the out degree of a specified vertex")
    print("\t4.Iterate through the set of outbound edges of a specified vertex")
    print("\t5.Iterate through the set of inbound edges of a specified vertex")
    print("\t6.Given an edge, retrieve its weight")
    print("\t7.Given an edge, modify its weight")
    print("\t8.Given two vertices, find the shortest path between them")
    print("\t9.Given two vertices, find the minimum cost path between the 2nd and the 1st one (backwords Dijkastra)")
    print("\t10.Verify if a graph is DAG and compute the longest path between 2 vertices")
    
def main():
    gp=Digraph()
    ReadGraph(gp)
    while(True):
        printMenu()
        command = input("Enter command: ").strip()
        if command=='1':
            print(gp.number_of_arcs())
        elif command=='2':
            tail=int(input("Tail vertex: "))
            head=int(input("Head vertex: "))
            print(gp.has_arc(tail, head))
        elif command=='3':
            vertex=int(input("Vertex: "))
            try:
                print("in degree:",gp.get_in_degree(vertex),"\nout degree:",gp.get_out_degree(vertex))
            except Exception as e:
                print(e)
        elif command=='4':
            vertex=int(input("Vertex: "))
            out=gp.get_outbound_of(vertex)
            for i in range(len(out)):
                print(i+1,"-> ["+str(vertex)+", "+str(out[i])+"]")
        elif command=='5':
            vertex=int(input("Vertex: "))
            out=gp.get_inbound_of(vertex)
            for i in range(len(out)):
                print(i+1,"-> ["+str(out[i])+", "+str(vertex)+"]")
        elif command=='6':
            tail=int(input("Tail vertex: "))
            head=int(input("Head vertex: "))
            try:
                print(gp.get_arc_weight(tail, head))
            except Exception as e:
                print(e)
        elif command=='7':
            tail=int(input("Tail vertex: "))
            head=int(input("Head vertex: "))
            weight=int(input("New weight: "))
            if gp.has_arc(tail, head)==True:
                gp.modify_weight(tail, head, weight)
            else:
                print("this edge is not present in this graph")
        elif command=='8':
            tail=int(input("Tail vertex: "))
            head=int(input("Head vertex: "))
            try:
                dist=shortestPath(gp,tail,head)
                if len(dist)>0:
                    print(dist)
            except ValueError as ve:
                print(ve)
        elif command=='9':
            tail=int(input("Head vertex: "))
            head=int(input("Tail vertex: "))
            c=gp.costs()
            try:
                pth,cst=dijkstraPath(gp, tail, head, c)
                print(pth,cst)
            except ValueError as ve:
                print(ve)
        elif command=='10':
            g=Digraph()
            g.add_arc(5, 11, 1)
            g.add_arc(11, 2, 1)
            g.add_arc(7, 11, 1)
            g.add_arc(11, 9, 1)
            g.add_arc(7, 8, 1)
            g.add_arc(8, 9, 3)
            g.add_arc(11, 10, 1)
            g.add_arc(3, 8, 1)
            g.add_arc(3, 10, 1)
            if TopoAlg(g)==0:
                print("the graph is not a dag")
            else:
                print(TopoAlg(g))
                sortl=TopoAlg(g)
                e=g.getEdges()
                costs=g.negCosts()
                s=int(input("start: "))
                t=int(input("end: "))
                #pth,cst=bellman(g,costs,e,s,t)
                #pth.reverse()
                #cst=cst*(-1)
                pth,cst=highestcostwalk(g, sortl, costs, s, t)
                print(pth,cst)
                
             
main()    