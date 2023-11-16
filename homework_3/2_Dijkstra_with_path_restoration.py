# Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.
#
# Формат ввода
# В первой строке содержатся три числа: N, S и F (1 ≤ N ≤ 100, 1 ≤ S, F ≤ N), где N — количество вершин графа,
# S — начальная вершина, а F — конечная. В следующих N строках вводится по N чисел, не превосходящих 100,
# – матрица смежности графа, где -1 означает, что ребра между вершинами нет,
# а любое неотрицательное число — наличие ребра данного веса. На главной диагонали матрицы записаны нули.
#
# Формат вывода
# Последовательно выведите все вершины одного (любого) из кратчайших путей, или -1, если
# пути между указанными вершинами не существует


def dijkstra(adj_list, start, finish):
    N = len(adj_list) - 1
    visited = [False] * (N + 1)
    visited[0] = True
    dist = [inf] * (N + 1)
    prev = [-1] * (N + 1)
    dist[start] = 0
    curr_v = 0
    for _ in range(N):
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
            if dist[vertex] == inf or dist[curr_v] + weight < dist[vertex]:
                prev[vertex] = curr_v
                dist[vertex] = dist[curr_v] + weight

    path = []
    curr_v = finish
    while prev[curr_v] != -1:
        path.append(curr_v)
        curr_v = prev[curr_v]
    if path or not dist[finish]:
        path.append(start)
    return (dist[finish] if dist[finish] != inf else -1), (path[::-1] if path else -1)


N, S, F = map(int, input().split())
inf = float("Inf")

# Преобразование матрицы смежности в список смежности
adjacency_list = [list() for _ in range(N + 1)] # list(tuple(weight, vertex))
for i in range(1, N + 1):
    line_i = list(map(int, input().split()))
    for index, value in enumerate(line_i):
        if value > 0:
            adjacency_list[i].append((value, index + 1))
min_len, min_path = dijkstra(adjacency_list, S, F)
if min_path != -1:
    print(*min_path, sep=" ")
else:
    print(-1)
