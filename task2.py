import networkx as nx
import matplotlib.pyplot as plt

# === Центральний граф метро (як у Task 1) ===
G = nx.Graph()

# M1
m1 = ["Університет", "Театральна", "Хрещатик", "Арсенальна"]
G.add_edges_from(zip(m1, m1[1:]))

# M2
m2 = ["Контрактова площа", "Поштова площа", "Майдан Незалежності", "Льва Толстого", "Олімпійська"]
G.add_edges_from(zip(m2, m2[1:]))

# M3
m3 = ["Лук’янівська", "Золоті ворота", "Палац спорту", "Кловська"]
G.add_edges_from(zip(m3, m3[1:]))

# Пересадочні вузли
transfers = [
    ("Театральна", "Золоті ворота"),          # M1 <-> M3
    ("Хрещатик", "Майдан Незалежності"),      # M1 <-> M2
    ("Льва Толстого", "Палац спорту")         # M2 <-> M3
]
G.add_edges_from(transfers)

# === DFS: пошук шляху ===
def dfs_path(graph, start, goal, path=None, visited=None):
    """Рекурсивний DFS для пошуку шляху."""
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    if start == goal:
        return path
    visited.add(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

# === BFS: пошук шляху ===
def bfs_path(graph, start, goal):
    """Ітеративний BFS для пошуку шляху."""
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph.neighbors(current):
            if neighbor not in visited and neighbor not in [p[0] for p in queue]:
                queue.append((neighbor, path + [neighbor]))
    return None

# === Задаємо початок і кінець
start_station = "Університет"
goal_station = "Кловська"

dfs_result = dfs_path(G, start_station, goal_station)
bfs_result = bfs_path(G, start_station, goal_station)

# === Результати
print(f"DFS шлях від '{start_station}' до '{goal_station}':")
print(" ➡ ".join(dfs_result))
print(f"\nBFS шлях від '{start_station}' до '{goal_station}':")
print(" ➡ ".join(bfs_result))

# === Візуалізація з виділеними шляхами
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))

# Малюємо всі вершини та ребра
nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=1200)

# Виділяємо шлях DFS червоним
dfs_edges = list(zip(dfs_result, dfs_result[1:]))
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="red", width=3, label="DFS шлях")

# Виділяємо шлях BFS синім
bfs_edges = list(zip(bfs_result, bfs_result[1:]))
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="blue", width=3, style="dashed", label="BFS шлях")

plt.title("DFS vs BFS: шляхи на графі Київського метро", fontsize=14)
plt.legend()
plt.show()
