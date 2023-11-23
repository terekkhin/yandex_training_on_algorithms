# По данному числу n выведите все правильные скобочные последовательности из
# круглых и квадратных скобок длины n в лексикографическом порядке.
#
# Формат ввода
# Одно целое число n (0 ≤ n ≤ 16).
#
# Формат вывода
# Выведите все правильные скобочные последовательности из круглых и
# квадратных скобок длины n в лексикографическом порядке. Каждая последовательность должна выводиться в новой строке.


from collections import deque


open_close_brackets = {
        ")": "(",
        "]": "["
    }


def permutations(arr, brackets, brackets_deque, open_b_count=0, index=0):
    if index == len(arr):
        if not brackets_deque:
            print("".join(map(str, arr)))
        return

    for i in range(0, 4):
        if brackets[i] in open_close_brackets.values():
            brackets_deque.append(brackets[i])
            open_b_count += 1
        else:
            if not brackets_deque or brackets_deque[-1] != open_close_brackets[brackets[i]]:
                continue
            elif brackets_deque[-1] == open_close_brackets[brackets[i]]:
                brackets_deque.pop()
        if open_b_count > len(arr)//2:
            brackets_deque.pop()
            open_b_count -= 1
            continue
        arr[index] = brackets[i]
        permutations(arr, brackets, brackets_deque, open_b_count, index + 1)
        if brackets[i] in open_close_brackets.keys():
            brackets_deque.append(open_close_brackets[brackets[i]])
        else:
            brackets_deque.pop()
            open_b_count -= 1
        arr[index] = 0


N = int(input())
brackets = ['(', '[', ')', ']']
brackets_deque = deque()
arr = [0] * N
permutations(arr, brackets, brackets_deque)
