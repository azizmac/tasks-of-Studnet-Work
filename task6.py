import matplotlib.pyplot as plt
import networkx as nx


def min_distance(distances, visited):
    min = float('inf')
    for v in range(len(distances)):
        if distances[v] < min and visited[v] == False:
            min = distances[v]
            min_index = v
    return min_index


def dijkstra(graph, src):
    vertices_count = len(graph)
    distances = [float('inf')] * vertices_count
    distances[src] = 0
    visited = [False] * vertices_count

    for count in range(vertices_count):
        u = min_distance(distances, visited)
        visited[u] = True

        for v in range(vertices_count):
            if graph[u][v] > 0 and visited[v] == False and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
    return distances


graph = nx.DiGraph()
graph.add_edge(1, 2, weight=7)
graph.add_edge(1, 3, weight=9)
graph.add_edge(2, 4, weight=10)

nx.draw(graph, with_labels=True)
plt.show()
shortest_paths = dijkstra(graph, 1)
print('Shortest paths from node 1:', shortest_paths)
