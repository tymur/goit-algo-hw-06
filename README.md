# goit-algo-hw-06

# Графи Київського метрополітену: Task 1 – Task 3

Цей проєкт демонструє роботу основних алгоритмів теорії графів на прикладі центральної частини Київського метрополітену. Використано бібліотеку **NetworkX** для моделювання графа та алгоритмів.

---

## Task 1: Створення графа та аналіз характеристик
- **Що зроблено:**  
  Створено граф для моделювання центральних станцій трьох гілок Київського метро (червона, синя, зелена).  
  Додано **пересадочні вузли** між гілками.  
  Виконано візуалізацію графа та аналіз:  
  - кількість вершин (станцій)  
  - кількість ребер (шляхів)  
  - ступінь вершин (кількість з’єднань кожної станції).  

---

## Task 2: Алгоритми DFS та BFS для пошуку шляхів
- **Що зроблено:**  
  Реалізовано два алгоритми пошуку шляху:  
  - **DFS (пошук в глибину):** знаходить шлях, занурюючись якомога далі, перш ніж повертатися.  
  - **BFS (пошук в ширину):** знаходить шлях з **мінімальною кількістю вершин** (найкоротший за кількістю кроків).  
  Порівняно шляхи, знайдені цими алгоритмами, та пояснено різницю між ними.  
  Виконано візуалізацію:  
  - шлях DFS (червоний, суцільний)  
  - шлях BFS (синій, пунктирний).

---

## Task 3: Алгоритм Дейкстри для найкоротших шляхів
- **Що зроблено:**  
  До графа додано **ваги на ребрах** (час проїзду та пересадки).  
  Реалізовано **алгоритм Дейкстри** для знаходження найкоротших шляхів між усіма парами станцій.  
  Виведено таблицю відстаней (часів проїзду) та виконано візуалізацію прикладу найкоротшого шляху.

---

## Використані бібліотеки
- `networkx` – робота з графами  
- `matplotlib` – візуалізація графа  

---

## Як запустити
1. Встановити залежності:
   pip install networkx matplotlib
