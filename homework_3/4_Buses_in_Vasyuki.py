# Между некоторыми деревнями края Васюки ходят автобусы.
# Поскольку пассажиропотоки здесь не очень большие, то автобусы ходят всего несколько раз в день.
#
# Марии Ивановне требуется добраться из деревни d в деревню v как можно быстрее
# (считается, что в момент времени 0 она находится в деревне d).
#
# Формат ввода
# Сначала вводится число N – общее число деревень (1 <= N <= 100),
# затем номера деревень d и v, за ними следует количество автобусных рейсов R (0 <= R <= 10000).
# Далее идут описания автобусных рейсов. Каждый рейс задается номером деревни отправления,
# временем отправления, деревней назначения и временем прибытия (все времена – целые от 0 до 10000).
# Если в момент t пассажир приезжает в какую-то деревню, то уехать из нее он может в любой момент времени, начиная с t.
#
# Формат вывода
# Выведите минимальное время, когда Мария Ивановна может оказаться в деревне v.
# Если она не сможет с помощью указанных автобусных рейсов добраться из d в v, выведите -1.


import heapq


def dijkstra(adj_list, start, finish):
    inf = float("inf")
    heap = []
    N = len(adj_list) - 1
    visited = [False] * (N + 1)
    visited[0] = True
    dist = [inf] * (N + 1)
    dist[start] = 0
    heapq.heappush(heap, (0,  0, start))
    heapq.heappush(heap, (inf, inf, -1))
    for _ in range(N):
        # Выбор непосещенной вершины с минимальным расстоянием
        curr_v = heapq.heappop(heap)
        if curr_v[2] == -1:
            break
        while visited[curr_v[2]]:
            curr_v = heapq.heappop(heap)

        # Отметка посещения
        visited[curr_v[2]] = True

        if visited[finish]:
            break

        # Изменение весов
        for arrival_time, departure_time, vertex in adjacency_list[curr_v[2]]:
            if arrival_time < dist[vertex] and departure_time >= dist[curr_v[2]]:
                dist[vertex] = arrival_time
                heapq.heappush(heap, (arrival_time, departure_time, vertex))
    return dist[finish] if dist[finish] != inf else -1


N = int(input())
S, F = map(int, input().split())
K = int(input())

# Преобразование матрицы смежности в список смежности
adjacency_list = [list() for _ in range(N + 1)] # list(tuple(weight, t, vertex))
for _ in range(K):
    v_1, departure_time, v_2, arrival_time = map(int, input().split())
    adjacency_list[v_1].append((arrival_time, departure_time, v_2))

print(dijkstra(adjacency_list, S, F))
