# Вам дано описание дорожной сети страны. Ваша задача – найти длину кратчайшего пути между городами А и B.
#
# Формат ввода
# Сеть дорог задана во входном файле следующим образом: первая строка содержит числа N и K
# (1 ≤ N ≤ 100000, 0 ≤ K ≤ 300000), где K – количество дорог. Каждая из следующих K
# строк содержит описание дороги с двусторонним движением – три целых числа
# ai, bi и li (1 ≤ ai, bi ≤ N, 1 ≤ li ≤ 106). Это означает, что имеется дорога длины li,
# которая ведет из города ai в город bi. В последней строке находятся два числа А и В – номера городов,
# между которыми надо посчитать кратчайшее расстояние (1 ≤ A, B ≤ N)
#
# Формат вывода
# Выведите одно число – расстояние между нужными городами. Если по дорогам от города А
# до города В доехать невозможно, выведите –1.

import heapq


def dijkstra(adj_list, start, finish):
    inf = float("inf")
    heap = []
    N = len(adj_list) - 1
    visited = [False] * (N + 1)
    visited[0] = True
    dist = [inf] * (N + 1)
    dist[start] = 0
    for i, d in enumerate(dist):
        heapq.heappush(heap, (d, i))
    for _ in range(N):
        # Выбор непосещенной вершины с минимальным расстоянием
        curr_v = heapq.heappop(heap)[1]

        while visited[curr_v]:
            curr_v = heapq.heappop(heap)[1]

        # Отметка посещения
        visited[curr_v] = True

        if visited[finish]:
            break
        # Изменение весов
        for weight, vertex in adjacency_list[curr_v]:
            if dist[curr_v] + weight < dist[vertex]:
                dist[vertex] = dist[curr_v] + weight
                heapq.heappush(heap, (dist[curr_v] + weight, vertex))
    return dist[finish] if dist[finish] != inf else -1


N, K = map(int, input().split())

# Преобразование матрицы смежности в список смежности
adjacency_list = [list() for _ in range(N + 1)] # list(tuple(weight, vertex))
for _ in range(K):
    v_1, v_2, w = map(int, input().split())
    adjacency_list[v_1].append((w, v_2))
    adjacency_list[v_2].append((w, v_1))
S, F = map(int, input().split())
print(dijkstra(adjacency_list, S, F))

