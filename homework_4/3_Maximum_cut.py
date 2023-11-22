# Взвешенный неориентированный граф без петель задан матрицей смежности.
# Распределите вершины по двум долям так, чтобы сумма весов рёбер,
# соединяющих вершины из разных долей, была максимальна.
#
# Формат ввода
# Вводится число N (2 ≤ N ≤ 20) — количество вершин в графе.
#
# В следующих N строках, содержащих по N целых чисел от 0 до 1000, задаётся матрица смежности.
# 0 означает отсутствие ребра.
#
# Формат вывода
# В первой строке выведите суммарный вес рёбер, соединяющих вершины из разных долей.
#
# Во второй строке выведите N чисел 1 или 2 — номера долей для каждой из вершин графа.

def count_flow(matrix, used, flow, added):
    if added == 0:
        return 0
    for i in range(len(used) - 1):
        if used[i + 1]:
            flow -= matrix[i][added - 1]
        else:
            flow += matrix[i][added - 1]
    return flow


def permutations(matrix, n, used, flow, curr_flow, path, index=0):
    curr_flow = count_flow(matrix, used, curr_flow, index)
    if flow[0] < curr_flow:
        flow[0] = curr_flow
        path[0] = used.copy()

    for i in range(index + 1, n + 1):
        used[i] = True
        permutations(matrix, n, used, flow, curr_flow, path, i)
        used[i] = False


def find_max_flow(matrix, n):
    used = [False] * (n + 1)
    path_res = [0]
    flow = [0]
    permutations(matrix, n, used, flow, 0, path_res)
    print(flow[0])
    for i in path_res[0][1:]:
        if i:
            print(2, end=" ")
        else:
            print(1, end=" ")


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
find_max_flow(matrix, n)


