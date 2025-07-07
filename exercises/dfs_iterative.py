import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# === Граф у вигляді списку суміжності ===
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# === Запис порядку відвіданих вершин ===
visited_order = []

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            visited_order.append(vertex)  # Зберігаємо порядок відвідання
            stack.extend(reversed(graph[vertex]))

# Виклик DFS
dfs_iterative(graph, 'A')

# === Візуалізація ===
def visualize_dfs_iterative(graph, visited_order):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=42)  # Розташування вершин
    fig, ax = plt.subplots()

    # Початковий колір для всіх вершин
    node_colors = ['lightgray' for _ in G.nodes()]

    def update(frame):
        ax.clear()
        ax.set_title(f"DFS (Ітеративно): відвідано {visited_order[:frame+1]}")
        # Змінюємо колір відвіданих вершин
        for i in range(frame + 1):
            node = visited_order[i]
            node_idx = list(G.nodes()).index(node)
            node_colors[node_idx] = 'lightgreen'
        nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax, node_size=800, font_weight='bold')

    ani = animation.FuncAnimation(fig, update, frames=len(visited_order), interval=1000, repeat=False)
    plt.show()

visualize_dfs_iterative(graph, visited_order)
