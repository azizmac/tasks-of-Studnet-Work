import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.incidence_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.incidence_list[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        # Рекурсивно посещаем все смежные вершины
        for u in self.incidence_list[v]:
            if not visited[u]:
                self.dfs_util(u, visited)

    def dfs(self, start_vertex):
        visited = [False] * self.V
        self.dfs_util(start_vertex, visited)

# create the graph object
g = Graph(6)  # Создание графа с 6 вершинами

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Результаты поиска в глубину начиная с вершины 0:")
g.dfs(0)

G = nx.Graph()

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,5)

nx.draw(G, with_labels=True)
plt.show()
