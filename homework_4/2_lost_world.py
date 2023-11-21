# Территория зоопарка Юрского периода «Затерянный мир» представляет собой решётку N × N,
# в каждой клетке которой находится вольер для динозавра. Директор зоопарка Степан Савельев
# планирует расселить в зоопарке N динозавров. Вольеры отделены друг от друга невысоким забором.
# Сотрудникам зоопарка известно, что динозавр не покидает пределов своего вольера, и не ломает забор,
# если он не видит на территории парка других динозавров. Зрительный аппарат у динозавров таков,
# что он видит всех динозавров, которые находятся на одной строке, на одном столбце или на одной диагонали с ним.
# Если же динозавр видит другого ящера, то ломает забор и вступает в борьбу. Директор зоопарка не хочет терпеть
# убытки, поэтому просит вас посчитать количество способов так расселить динозавров в зоопарке,
# чтобы никакой ящер не видел остальных динозавров.
#
# Формат ввода
# Задано единственное число N (N ≤ 10).
#
# Формат вывода
# Необходимо вывести количество способов, которыми можно расселить в зоопарке N динозавров,
# чтобы у зоопарка не было убытков.

def permutations(arr, used_row, used_first_d, used_second_d, res, index=0):
    if index == len(arr):
        res[0] += 1

    for i in range(1, N + 1):
        if not used_row[i] and not used_first_d[index - i + len(arr) - 1] and not used_second_d[i + index]:
            used_row[i] = True
            used_first_d[index - i + len(arr) - 1] = True
            used_second_d[i + index] = True
            arr[index] = i
            permutations(arr, used_row, used_first_d, used_second_d, res, index + 1)
            used_row[i] = False
            used_first_d[index - i + len(arr) - 1] = False
            used_second_d[i + index] = False


N = int(input())

arr = [i for i in range(1, N + 1)]
used_row = [False]*(N + 1)
used_first_d = [False]*(2*N)
used_second_d = [False]*(2*N)
res = [0]
permutations(arr, used_row, used_first_d, used_second_d, res)
print(res[0])
