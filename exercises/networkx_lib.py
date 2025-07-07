import networkx as nx
import matplotlib.pyplot as plt

# Кругова розкладка (circular_layout)
G = nx.complete_graph(8)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Circular Layout")
plt.show()

# Випадкова розкладка (random_layout)
G = nx.complete_graph(8)
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Random Layout")
plt.show()

# Камеральна розкладка (shell_layout)
G = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G, pos)
nx.draw(G, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()