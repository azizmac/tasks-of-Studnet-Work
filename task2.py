from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A','C', 'D', 'E', 'F'],
    'C': ['A','B', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'B']
}

G = nx.Graph()

for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

start_vertex = 'D'
goal_vertex = 'C'
path = bfs_shortest_path(graph, start_vertex, goal_vertex)
print(f"Кратчайший путь между {start_vertex} и {goal_vertex}: {path}")

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightgrey')
nx.draw_networkx_edges(G, pos, edge_color='black')
nx.draw_networkx_labels(G, pos)

path_nodes = [start_vertex] + path + [goal_vertex]
path_edges = list(zip(path_nodes[:-1], path_nodes[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='blue')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', arrowstyle='-|>', arrows=True)
plt.show()
