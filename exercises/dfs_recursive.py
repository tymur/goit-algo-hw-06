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

# === Зберігаємо порядок відвідування вершин ===
visited_order = []

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    visited_order.append(vertex)  # Записуємо відвідану вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Виклик DFS
dfs_recursive(graph, 'A')

# === Візуалізація ===
def visualize_dfs(graph, visited_order):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=42)  # Розташування вершин
    fig, ax = plt.subplots()

    # Всі вершини спочатку сірі
    node_colors = ['lightgray' for _ in G.nodes()]

    def update(frame):
        ax.clear()
        ax.set_title(f"DFS: відвідано {visited_order[:frame+1]}")
        # Змінюємо колір відвіданих вершин
        for i in range(frame + 1):
            node = visited_order[i]
            node_idx = list(G.nodes()).index(node)
            node_colors[node_idx] = 'skyblue'
        nx.draw(G, pos, with_labels=True, node_color=node_colors, ax=ax, node_size=800, font_weight='bold')

    ani = animation.FuncAnimation(fig, update, frames=len(visited_order), interval=1000, repeat=False)
    plt.show()

visualize_dfs(graph, visited_order)
