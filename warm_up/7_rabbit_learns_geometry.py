# Кролики очень любопытны. Они любят изучать геометрию, бегая по грядкам.
# Наш кролик как раз такой. Сегодня он решил изучить новую фигуру — квадрат.
#
# Кролик бегает по грядке — клеточному полю N × M клеток.
# В некоторых из них посеяны морковки, в некоторых нет.
#
# Помогите кролику найти сторону квадрата наибольшей площади, заполненного морковками полностью.
#
# Формат ввода
# В первой строке даны два натуральных числа N и M (1 <= N, M <= 1000).
# Далее в N строках расположено по M чисел, разделенных пробелами
# (число равно 0, если в клетке нет морковки или 1, если есть).
#
# Формат вывода
# Выведите одно число — сторону наибольшего квадрата, заполненного морковками.

#
# n, m = map(int, input().split())
#
# field = []
# for i in range(n):
#     field.append(list(map(int, input().split())))
# size = min(n, m)
# start_i = 0
# start_j = 0
# stop_flag = False
# while size:
#     for i in range(start_i, start_i + size):
#         for j in range(start_j, start_j + size):
#             if field[i][j] == 0:
#                 stop_flag = True
#                 break
#         if stop_flag:
#             break
#     if not stop_flag:
#         break
#     else:
#         start_j += 1
#         if start_j + size > m:
#             start_j = 0
#             start_i += 1
#             if start_i + size > n:
#                 start_i = 0
#                 size -= 1
#         stop_flag = False
# print(size)


def find_largest_square(field, n, m):
    if not field or not len(field):
        return 0
    dp = [[0 for _ in range(m)] for _ in range(n)]
    max_size = 0
    for i in range(n):
        for j in range(m):
            dp[i][j] = field[i][j]
            if i > 0 and j > 0 and field[i][j] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            if max_size < dp[i][j]:
                max_size = dp[i][j]
    return max_size


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []
    for i in range(n):
        field.append(list(map(int, input().split())))
    print(find_largest_square(field, n, m))
