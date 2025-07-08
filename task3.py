import networkx as nx
import matplotlib.pyplot as plt

# === Центральний граф метро ===
G = nx.Graph()

# M1
m1 = ["Університет", "Театральна", "Хрещатик", "Арсенальна"]
G.add_edges_from(zip(m1, m1[1:]), weight=2)  # час проїзду = 2 хв

# M2
m2 = ["Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Українських Героїв", "Олімпійська"]
G.add_edges_from(zip(m2, m2[1:]), weight=3)  # час проїзду = 3 хв

# M3
m3 = ["Лук’янівська", "Золоті ворота", "Палац спорту", "Кловська"]
G.add_edges_from(zip(m3, m3[1:]), weight=4)  # час проїзду = 4 хв

# Пересадочні вузли (пари станцій)
transfers = [
    ("Театральна", "Золоті ворота"),          # M1 <-> M3
    ("Хрещатик", "Майдан Незалежності"),      # M1 <-> M2
    ("Площа Українських Героїв", "Палац спорту")         # M2 <-> M3
]
# Для пересадок вага = 5 хв (час переходу між лініями)
G.add_edges_from(transfers, weight=5)

# === Географічне розташування (приблизне) ===
pos = {
    # Червона лінія
    "Університет": (0, 2), "Театральна": (0, 1), "Хрещатик": (0, 0), "Арсенальна": (1, -0.5),
    # Синя лінія
    "Контрактова площа": (-2, 3), "Поштова площа": (-1, 2), "Майдан Незалежності": (-1, -0.5),
    "Площа Українських Героїв": (-1, -1.5), "Олімпійська": (-1, -2.5),
    # Зелена лінія
    "Лук’янівська": (3, 3), "Золоті ворота": (2, 1), "Палац спорту": (2, -1), "Кловська": (3, -2),
    "Печерська": (4, -3), "Дружби народів": (5, -4), "Видубичі": (6, -5)
}

# === Алгоритм Дейкстри: знаходимо шляхи
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight="weight"))
all_shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight="weight"))

# Вивід таблиці найкоротших шляхів
print("Найкоротші відстані між станціями (час у хвилинах):")
for source, lengths in all_shortest_lengths.items():
    for target, time in lengths.items():
        if source != target:
            print(f"{source:20} ➡ {target:20} = {time} хв")

# === Візуалізація графа
plt.figure(figsize=(12, 8))

# Малюємо всі вершини та ребра з підписами ваг
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1200, font_size=10)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("DFS: Центральний граф метро з вагами (час проїзду в хвилинах)", fontsize=14)
plt.show()

# === Виділимо приклад найкоротшого шляху
source_station = "Контрактова площа"
target_station = "Кловська"
shortest_path = all_shortest_paths[source_station][target_station]

print(f"\nНайкоротший шлях від '{source_station}' до '{target_station}':")
print(" ➡ ".join(shortest_path))

# Підсвічуємо цей шлях
path_edges = list(zip(shortest_path, shortest_path[1:]))
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=1200)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3, label="Найкоротший шлях")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title(f"Найкоротший шлях: {source_station} ➡ {target_station}", fontsize=14)
plt.legend()
plt.show()
