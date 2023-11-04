# Задана последовательность целых чисел a1, a2, …, an.
# Задаются запросы: сказать любой элемент последовательности на отрезке от L до R включительно,
# не равный минимуму на этом отрезке.
#
# Формат ввода
# В первой строке содержатся два целых числа N, 1 ≤ N ≤ 100 и M, 1 ≤ M ≤ 1000 — длина
# последовательности и количество запросов соответственно.
# Во второй строке — сама последовательность, 0 ≤ ai ≤ 1000.
# Начиная с третьей строки перечисляются M запросов, состоящих из границ отрезка L и R,
# где L, R - индексы массива, нумеруются с нуля.
#
# Формат вывода
# На каждый запрос выведите в отдельной строке ответ — любой элемент на [L, R], кроме минимального.
# В случае, если такого элемента нет, выведите "NOT FOUND".

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

for i in range(m):
    flag = False
    left, right = map(int, input().split())
    min_num = numbers[left]
    for j in numbers[left:right + 1]:
        if min_num < j:
            print(j)
            flag = True
            break
        elif min_num > j:
            flag = True
            print(min_num)
            break
    if not flag:
        print('NOT FOUND')


