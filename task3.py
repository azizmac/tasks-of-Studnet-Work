import networkx as nx
import matplotlib.pyplot as plt

# Функция для нахождения минимального остовного дерева
def find_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph)

def calculate_F_cycles(graph, spanning_tree):
    num_edges = graph.number_of_edges()
    num_branches = spanning_tree.number_of_edges()
    return num_edges - num_branches

def visualize_graph_and_spanning_tree(graph, spanning_tree):
    pos = nx.spring_layout(graph)

    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')

    nx.draw_networkx_edges(spanning_tree, pos, edge_color='green', width=2)

    plt.title("Граф и его минимальное остовное дерево")
    plt.show()

graph = nx.Graph()
edges = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4)
]
graph.add_edges_from(edges)

spanning_tree = find_spanning_tree(graph)

F_cycles = calculate_F_cycles(graph, spanning_tree)

print(f"Число всех рёбер в графе: {graph.number_of_edges()}")
print(f"Число ветвей в каркасе: {spanning_tree.number_of_edges()}")
print(f"Количество Ф-циклов: {F_cycles}")

visualize_graph_and_spanning_tree(graph, spanning_tree)