# Неориентированный взвешенный граф задан матрицей смежности.
# Найдите кратчайший цикл, который начинается и заканчивается в вершине номер 1
# и проходит через все вершины по одному разу.
#
# Формат ввода
# В первой строке вводится число N (N ≤ 10) — количество вершин графа.
# Следующие N строк содержат по N целых неотрицательных чисел и задают матрицу смежности.
# Число 0 означает, что ребро отстутствует. Любое другое число задаёт вес ребра.
#
# Формат вывода
# Выведите минимальную суммарную длину цикла или число -1, если цикл построить невозможно.

def permutations(matrix, arr, used, dist, curr_dist, index=0):
    if index == len(arr) - 2:
        flag = True
        for i in range(1, len(arr)):
            if matrix[arr[i - 1] - 1][arr[i] - 1] == 0:
                flag = False
                break
        curr_dist[0] += matrix[arr[-2] - 1][0]
        if curr_dist[0] < dist[0] and flag:
            dist[0] = curr_dist[0]
        curr_dist[0] -= matrix[arr[-2] - 1][0]

    for i in range(2, len(arr)):
        if not used[i]:
            used[i] = True
            curr_dist[0] += matrix[arr[index] - 1][i - 1]
            if curr_dist[0] >= dist[0]:
                curr_dist[0] -= matrix[arr[index] - 1][i - 1]
                used[i] = False
                continue
            arr[index + 1] = i
            permutations(matrix, arr, used, dist, curr_dist, index + 1)
            arr[index + 1] = 0
            curr_dist[0] -= matrix[arr[index] - 1][i - 1]
            used[i] = False


def find_shortest_cycle(matrix, n):
    if n == 1:
        print(0)
        return
    used = [False] * (n + 1)
    used[1] = True
    arr = [1] * (n + 1)

    dist = [float("inf")]
    curr_dist = [0]
    permutations(matrix, arr, used, dist, curr_dist)
    print(-1 if dist[0] == float("inf") else dist[0])


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
find_shortest_cycle(matrix, n)
