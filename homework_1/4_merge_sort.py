# Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.
#
# На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с помощью уже реализованной функции.
#
# Формат ввода
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 10**6).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами (-10**9 ≤ ai ≤ 10**9).
#
# Формат вывода
# Выведите результат сортировки, то есть N целых чисел, разделенных пробелами, в порядке неубывания.

def merge(merged_arr, arr_1, arr_2):
    p_1 = 0
    p_2 = 0
    while p_1 != len(arr_1) and p_2 != len(arr_2):
        if arr_1[p_1] <= arr_2[p_2]:
            merged_arr.append(arr_1[p_1])
            p_1 += 1
        else:
            merged_arr.append(arr_2[p_2])
            p_2 += 1
    if p_1 == len(arr_1):
        merged_arr += arr_2[p_2:]
    else:
        merged_arr += arr_1[p_1:]


def merge_sort(arr, left, right) -> list:
    if right - left <= 1:
        return arr[left:right]
    result = []
    arr_1 = merge_sort(arr, left, (left + right) // 2)
    arr_2 = merge_sort(arr, (left + right) // 2, right)
    merge(result, arr_1, arr_2)
    return result


n = int(input())
array = list(map(int, input().split()))
print(*merge_sort(array, 0, n))

# def merge(merged_arr, arr_1, arr_2, left):
#     p_1 = 0
#     p_2 = 0
#     while p_1 != len(arr_1) and p_2 != len(arr_2):
#         if arr_1[p_1] <= arr_2[p_2]:
#             merged_arr[left+ p_1 + p_2] = arr_1[p_1]
#             p_1 += 1
#         else:
#             merged_arr[left + p_1 + p_2] = arr_2[p_2]
#             p_2 += 1
#     if p_1 == len(arr_1):
#         for i in range(p_2, len(arr_2)):
#             merged_arr[left + p_1 + i] = arr_2[i]
#     else:
#         for i in range(p_1, len(arr_1)):
#             merged_arr[left + i + p_2] = arr_1[i]
#
#
# def merge_sort(arr, left, right):
#     if right - left <= 1:
#         return arr[left:right]
#     arr_1 = merge_sort(arr, left, (left + right) // 2)
#     arr_2 = merge_sort(arr, (left + right) // 2, right)
#     merge(arr, arr_1, arr_2, left)
#     return arr[left:right]
#
#
# n = int(input())
# array = list(map(int, input().split()))
# merge_sort(array, 0, n)
# print(*array)
