def check_edge(adjacency_matrix, node1, node2):
    """
    Перевіряє, чи існує ребро між node1 і node2.
    
    :param adjacency_matrix: 2D список (матриця суміжності)
    :param node1: індекс першого вузла
    :param node2: індекс другого вузла
    :return: 1, якщо ребро існує; -1, якщо ні
    """
    if adjacency_matrix[node1][node2] != 0:
        return 1
    else:
        return -1

# Матриця суміжності для графа:
#   0 --- 1
#    \     \
#     2 --- 3
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

print(check_edge(adjacency_matrix, 0, 1))  # Виведе: 1 (ребро є)
print(check_edge(adjacency_matrix, 0, 3))  # Виведе: -1 (ребра немає)
print(check_edge(adjacency_matrix, 2, 3))  # Виведе: 1 (ребро є)
