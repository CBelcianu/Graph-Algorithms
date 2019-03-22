'''
Created on 28 feb. 2018

@author: Catalin
'''
class Digraph:
    def __init__(self):
        '''
        default constructor for Digraph class
        '''
        self.nodes = set()
        self.outbound = dict()
        self.inbound = dict()
        self.edges = 0
        
    def getNodes(self):
        return self.nodes
    
    def getEdges(self):
        edges=[]
        for i in self.nodes:
            for j in self.get_outbound_of(i):
                edges.append((i,j))
        return edges
    def costs(self):
        costs=dict()
        for i in self.nodes:
            for j in self.get_outbound_of(i):
                costs[(i,j)]=self.get_arc_weight(i, j);
        return costs
    
    def negCosts(self):
        costs=dict()
        for i in self.nodes:
            for j in self.get_outbound_of(i):
                costs[(i,j)]=(self.get_arc_weight(i, j))*(-1);
        return costs
    def add_node(self, node):
        '''
        function that adds a node to the graph
        input: node
        '''
        if node in self.nodes:
            return

        self.nodes.add(node)
        self.outbound[node] = dict()
        self.inbound[node] = dict()

    def add_arc(self, tail, head, weight):
        '''
        function that adds an arc to the graph
        input: tail node, head node and the weight of the arc
        '''
        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.outbound[tail][head] = weight
        self.inbound[head][tail] = weight
        self.edges += 1
        
    def modify_weight(self, tail, head, weight):
        '''
        function that modifies the weight of a given edge
        input: tail node, head node and the new weight
        '''
        if tail in self.nodes and head in self.nodes:
            self.outbound[tail][head] = weight
            self.inbound[head][tail] = weight

    def has_arc(self, tail, head):
        '''
        function that verifies if there exists an arc from the tail node to the head node
        input: tail node, head node
        output: True, False
        '''
        if tail not in self.nodes:
            return False

        if head not in self.nodes:
            return False

        return head in self.outbound[tail].keys()

    def get_arc_weight(self, tail, head):
        '''
        function that returns the weight of an arc
        input: tail node, head node
        output: weight
        '''
        if tail not in self.nodes:
            raise Exception("The tail vertex is not present in this directed graph.")

        if head not in self.nodes:
            raise Exception("The head vertex is not present in this directed graph.")

        if head not in self.outbound[tail].keys():
            raise Exception("The edge is not in this directed graph.")

        return self.outbound[tail][head]

    def remove_arc(self, tail, head):
        '''
        function that removes an arc
        input: tail node, head node
        '''
        if tail not in self.nodes:
            return

        if head not in self.nodes:
            return

        del self.outbound[tail][head]
        del self.inbound[head][tail]
        self.edges -= 1

    def remove_node(self, node):
        if node not in self.nodes:
            return

        self.edges -= len(self.outbound[node]) + len(self.inbound[node])

        for child in self.outbound[node]:
            del self.inbound[child][node]

        for parent in self.inbound[node]:
            del self.outbound[parent][node]

        del self.outbound[node]
        del self.inbound[node]
        self.nodes.remove(node)
    
    def number_of_nodes(self):
        '''
        function that returns the number of nodes in the graph
        output: the number of nodes
        '''
        return len(self.nodes)
    
    def number_of_arcs(self):
        '''
        function that returns the number of arcs in the graph
        output: the number of arcs
        '''
        return self.edges

    def get_inbound_of(self, node):
        '''
        function that returns the list of inbound edges of a given node
        input: node
        output: the list of inbound edges
        '''
        if node not in self.nodes:
            return []

        return list(self.inbound[node].keys())
    
    def get_in_degree(self, node):
        '''
        function that returns the in-degree of a given node (the number of inbound edges)
        input: node
        output: the number of inbound edges
        '''
        if node not in self.nodes:
            raise Exception("this vertex is not present in this directed graph")

        return len(self.inbound[node].keys())

    def get_outbound_of(self, node):
        '''
        function that returns the list of outbound edges of a given node
        input: node
        output: the list of outbound edges
        '''
        if node not in self.nodes:
            return []

        return list(self.outbound[node].keys())
    
    def get_out_degree(self, node):
        '''
        function that returns the out-degree of a given node (the number of outbound edges)
        input: node
        output: the number of outbound edges
        '''
        if node not in self.nodes:
            raise Exception("this vertex is not present in this directed graph")

        return len(self.outbound[node].keys())

    def clear(self):
        del self.nodes[:]
        self.outbound.clear()
        self.inbound.clear()
        self.edges = 0