# Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.
#
# На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.
# Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.
#
# Формат ввода
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 10**6).
# Во второй строке содержатся N целых чисел a_i, разделенных пробелами (-10**9 ≤ ai ≤ 10**9).
#
# Формат вывода
# Выведите результат сортировки, то есть N целых чисел, разделенных пробелами.

from random import choice


def partition(array, x, left, right):
    e, g, n = left, left, left
    for i in range(left, right):
        if array[i] < x:
            array[e], array[n] = array[n], array[e]
            if e != g:
                array[g], array[n] = array[n], array[g]
            e += 1
            g += 1
            n += 1
        elif array[i] == x:
            array[g], array[n] = array[n], array[g]
            g += 1
            n += 1
        else:
            n += 1
    if g == right - 1 and e == left:
        return "stop", "stop"
    return e, g


def select_x(array, left, right):
    return choice(array[left:right])


def quick_sort(array, left, right):
    if right - left <= 1:
        return
    x = select_x(array, left, right)
    e, g = partition(array, x, left, right)
    if e == "stop":
        return
    quick_sort(array, left, e)
    quick_sort(array, g, right)


def main():
    n = int(input())
    if n == 0:
        return
    array = list(map(int, input().split()))
    quick_sort(array, 0, n)
    if array:
        print(*array)


if __name__ == "__main__":
    main()


