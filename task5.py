import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    path = {start: None}

    for _ in range(len(graph) - 1):
        for current_node, neighbours in graph.items():
            for neighbour, distance in neighbours.items():
                if distances[current_node] + distance < distances[neighbour]:
                    distances[neighbour] = distances[current_node] + distance
                    path[neighbour] = current_node

    for current_node, neighbours in graph.items():
        for neighbour, distance in neighbours.items():
            if distances[current_node] + distance < distances[neighbour]:
                return "Graph contains a negative weight cycle"

    return distances, path

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2},
    'C': {},
    'D': {'E': 4},
    'E': {}
}
distances, path = bellman_ford(graph, 'A')
print('Distances from A: ', distances)

G = nx.DiGraph(directed=True)
for node, neighbours in graph.items():
    for neighbour, distance in neighbours.items():
        G.add_edge(node, neighbour, weight=distance)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels = True)

labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
