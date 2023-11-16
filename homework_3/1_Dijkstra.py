# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.
#
# Формат ввода
# В первой строке содержатся три числа: N, S и F (1≤ N ≤ 100, 1 ≤ S, F ≤ N), где N — количество вершин графа,
# S — начальная вершина, а F — конечная. В следующих N строках вводится по N чисел, не превосходящих 100,
# – матрица смежности графа, где -1 означает что ребра между вершинами нет,
# а любое неотрицательное число — наличие ребра данного веса. На главной диагонали матрицы записаны нули.
#
# Формат вывода
# Выведите искомое расстояние или -1, если пути между указанными вершинами не существует.


def dijkstra(adj_list, start, finish):
    N = len(adj_list) - 1
    visited = [False] * (N + 1)
    visited[0] = True
    dist = [inf] * (N + 1)
    dist[start] = 0
    curr_v = 0
    while not all(visited):
        # Выбор непосещенной вершины с минимальным расстоянием
        min_dist = inf
        for i, _ in enumerate(dist):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                curr_v = i
        # Отметка посещения
        visited[curr_v] = True
        # Изменение весов
        for weight, vertex in adjacency_list[curr_v]:
            if dist[vertex] == inf:
                dist[vertex] = dist[curr_v] + weight
            else:
                dist[vertex] = min(dist[vertex], dist[curr_v] + weight)

        stop_flag = True
        for i, _ in enumerate(dist):
            if dist[i] != inf and not visited[i]:
                stop_flag = False
                break
        if stop_flag:
            break
    return dist[finish] if dist[finish] != inf else -1


N, S, F = map(int, input().split())
inf = float("Inf")

# Преобразование матрицы смежности в список смежности
adjacency_list = [list() for _ in range(N + 1)] # list(tuple(weight, vertex))
for i in range(1, N + 1):
    line_i = list(map(int, input().split()))
    for index, value in enumerate(line_i):
        if value > 0:
            adjacency_list[i].append((value, index + 1))

print(dijkstra(adjacency_list, S, F))

