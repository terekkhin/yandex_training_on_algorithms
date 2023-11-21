# В начале XVIII века еще не было самолетов, поездов и автомобилей, поэтому все междугородние зимние поездки
# совершались на санях. Как известно, с дорогами в России тогда было даже больше проблем, чем сейчас,
# а именно на N существовавших тогда городов имелась N-1 дорога, каждая из которых соединяла два города.
# Из каждого города можно было добраться в любой другой (возможно, через промежуточные города).
# В каждом городе была почтовая станция («ям»), на которой можно было пересесть в другие сани.
# При этом ямщики могли долго запрягать (для каждого города известно время, которое ямщики в этом городе
# тратят на подготовку саней к поездке) и быстро ехать (также для каждого города известна скорость,
# с которой ездят ямщики из него). Можно считать, что количество ямщиков в каждом городе не ограничено.
#
# Если бы олимпиада проводилась 300 лет назад, то путь участников занимал бы гораздо большее время, чем сейчас.
# Допустим, из каждого города в Москву выезжает участник олимпиады и хочет добраться до Москвы за наименьшее время
# (не обязательно по кратчайшему пути: он может заезжать в любые города, через один и тот же город можно
# проезжать несколько раз). Сначала он едет с ямщиком из своего города. Приехав в любой город, он может либо сразу
# ехать дальше, либо пересесть. В первом случае он едет с той же скоростью, с какой ехал раньше. Если сменить ямщика,
# он сначала ждет, пока ямщик подготовит сани, и только потом едет с ним (с той скоростью, с которой ездит этот ямщик).
# В пути можно делать сколько угодно пересадок.
#
# Определите, какое время необходимо, чтобы все участники олимпиады доехали из своего города в Москву 300 лет назад.
# Все участники выезжают из своих городов одновременно.
#
# Формат ввода
# В первой строке входного файла дано натуральное число N, не превышающее 2000 — количество городов, соединенных
# дорогами. Город с номером 1 является столицей.
#
# Следующие N строк содержат по два целых числа: Ti и Vi — время подготовки саней в городе i, выраженное в часах,
# и скорость, с которой ездят ямщики из города i, в километрах в час (0 ≤ Ti ≤ 100, 1 ≤ Vi ≤ 100).
#
# Следующие N–1 строк содержат описания дорог того времени. Каждое описание состоит из трех чисел Aj, Bj и Sj,
# где Aj и Bj — номера соединенных городов, а Sj — расстояние между ними в километрах (1 ≤ Aj ≤ N, 1 ≤ Bj ≤ N, Aj ≠ Bj,
# 1 ≤ Sj ≤ 10000). Все дороги двусторонние, то есть если из A можно проехать в B, то из B можно проехать в A.
# Гарантируется, что из всех городов можно добраться в столицу.
#
# Формат вывода
# Сначала выведите одно вещественное число — время в часах, в которое в Москву приедет последний участник.
#
# Далее выведите путь участника, который приедет самым последним (если таких участников несколько, выведите путь
# любого из них). Выведите город, из которого этот участник выехал первоначально, и перечислите в порядке посещения
# те города, в которых он делал пересадки. Последовательность должна заканчиваться столицей.
#
# При проверке ответ будет засчитан, если из трех величин «время путешествия по выведенному пути», «выведенное время»
# и «правильный ответ» каждые две отличаются менее чем на 0.0001.

import heapq


# def dijkstra(adj_list, prep, start, finish):
#     inf = float("inf")
#     heap = []
#     N = len(adj_list) - 1
#     visited = [False] * (N + 1)
#     visited[0] = True
#     dist = [inf] * (N + 1)
#     dist[start] = 0
#     prev = [-1] * (N + 1)
#     heapq.heappush(heap, (prep[start][0], prep[start][1], start, -1))
#     heapq.heappush(heap, (inf, 0, -1, -1))
#     while True:
#         # Выбор непосещенной вершины с минимальным расстоянием
#         curr_v = heapq.heappop(heap)
#         if curr_v[2] == -1:
#             break
#
#         if visited[finish]:
#             break
#
#         # Изменение весов
#         for weight, vertex in adjacency_list[curr_v[2]]:
#             curr_speed = curr_v[1]
#             wait = 0
#             prev_v = curr_v[3]
#             if (weight / curr_speed) > (weight / prep[curr_v[2]][1] + prep[curr_v[2]][0]):
#                 curr_speed = prep[curr_v[2]][1]
#                 wait = prep[curr_v[2]][0]
#                 prev_v = curr_v[2]
#             if weight / curr_speed + wait + curr_v[0] < dist[vertex]:
#                 dist[vertex] = weight / curr_speed + curr_v[0] + wait
#                 prev[vertex] = prev_v
#             heapq.heappush(heap, (weight / curr_speed + curr_v[0] + wait, curr_speed, vertex, prev_v))
#             if curr_speed < prep[curr_v[2]][1]:
#                 heapq.heappush(heap, (weight / prep[curr_v[2]][1] + curr_v[0] + prep[curr_v[2]][0], prep[curr_v[2]][1], vertex, curr_v[2]))
#
#
#         # Отметка посещения
#         visited[curr_v[2]] = True
#
#     path = []
#     curr_v = finish
#     while prev[curr_v] != -1:
#         path.append(curr_v)
#         curr_v = prev[curr_v]
#
#     return dist[finish] if dist[finish] != inf else -1, [start] + path[::-1]

def dijkstra(adj_list, prep, start, finish):
    inf = float("inf")
    heap = []
    N = len(adj_list) - 1
    visited = [False] * (N + 1)
    visited[0] = True
    prev = [-1] * (N + 1)
    dist = [(inf, 0) for _ in range(N + 1)]
    dist[start] = (0, 0)
    heapq.heappush(heap, (prep[start][0], prep[start][1], start, start))
    heapq.heappush(heap, (inf, 0, -1, -1))

    curr_v = heapq.heappop(heap)
    while curr_v[2] != -1:
        if dist[finish][0] != inf:
            break
        for weight, vertex in adjacency_list[curr_v[2]]:
            if dist[vertex][0] > weight / curr_v[1] + curr_v[0]:
                dist[vertex] = (weight / curr_v[1] + curr_v[0], curr_v[1])
                prev[vertex] = curr_v[3]
                heapq.heappush(heap, (weight / curr_v[1] + curr_v[0], curr_v[1], vertex, curr_v[3]))
            if dist[vertex][1] < curr_v[1]:
                heapq.heappush(heap, (weight / curr_v[1] + curr_v[0], curr_v[1], vertex, curr_v[3]))
            if curr_v[1] < prep[curr_v[2]][1]:
                if dist[vertex][0] > weight / prep[curr_v[2]][1] + curr_v[0] + prep[curr_v[2]][0]:
                    dist[vertex] = (weight / prep[curr_v[2]][1] + curr_v[0] + prep[curr_v[2]][0], prep[curr_v[2]][1])
                    prev[vertex] = curr_v[2]
                heapq.heappush(heap, (weight / prep[curr_v[2]][1] + curr_v[0] + prep[curr_v[2]][0], prep[curr_v[2]][1], vertex, vertex))
        curr_v = heapq.heappop(heap)

    path = []
    curr_v = finish
    while curr_v != start:
        path.append(curr_v)
        curr_v = prev[curr_v]

    return dist[finish][0] if dist[finish][0] != inf else -1, [start] + path[::-1]


N = int(input())
prep = [0] * (N + 1)
for i in range(1, N + 1):
    prep[i] = tuple(map(int, input().split()))

# Преобразование матрицы смежности в список смежности
adjacency_list = [list() for _ in range(N + 1)] # list(tuple(weight, vertex))
for _ in range(N - 1):
    v_1, v_2, weight = map(int, input().split())
    adjacency_list[v_1].append((weight, v_2))
    adjacency_list[v_2].append((weight, v_1))

time = 0
path = []
for i in range(2, N + 1):
    curr_time, curr_path = dijkstra(adjacency_list, prep, i, 1)
    if curr_time > time:
        time = curr_time
        path = curr_path
print(time)
print(*path, sep=" ")
