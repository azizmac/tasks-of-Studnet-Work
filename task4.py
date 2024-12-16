import networkx as nx
import matplotlib.pyplot as plt
class Node():
    def __init__(self, name):
        self.name = name
        self.distance = float('inf')
        self.predecessor = None

class Graph():
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def print_graph(self):
        for node in self.nodes:
            print('Node:', node.name)
            if node.predecessor is not None:
                print('Predecessor:', node.predecessor.name)
            else:
                print('No predecessor')
            print("Distance:", node.distance if node.distance!= float('inf') else 'Infinity')
    def add_edge(self,u,v,w):
        self.edges.append((u, v, w))

nodes = [Node(i) for i in range(1, 7)]
edges = []
graph = Graph(nodes, edges)
for i in range(3):
    graph.add_edge(nodes[2], nodes[i], 2)
graph.add_edge(nodes[0], nodes[3], 5)
graph.add_edge(nodes[5], nodes[3], 7)
graph.add_edge(nodes[0], nodes[4], 8)
graph.add_edge(nodes[1], nodes[4], 1)
graph.add_edge(nodes[3], nodes[5], 3)
def FordBellman(G, source):
    source.distance = 0
    for i in range(len(G.nodes)-1):
        for edge in G.edges:
            u, v, w = edge[0], edge[1], edge[2]
            if (v.distance > u.distance + w):
                v.distance = u.distance + w
                v.predecessor = u

    for edge in G.edges:
        u, v, w = edge[0], edge[1], edge[2]
        if (v.distance > u.distance + w):
            return "Graph has a negative weight cycle"
    graph.print_graph()
FordBellman(graph, nodes[2])
G = nx.DiGraph()
node_labels={}
for i in range(1,7):
    G.add_node(i)
    node_labels[i]=str(i)
for i in range(3):
    G.add_edge(3,i+1,weight=2)
G.add_edge(1,4,weight=5)
G.add_edge(6,4,weight=7)
G.add_edge(1,5,weight=8)
G.add_edge(2,5,weight=1)
G.add_edge(4,6,weight=3)
pos = nx.spring_layout(G) 
nx.draw_networkx(G, pos, arrows=False,with_labels = True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
