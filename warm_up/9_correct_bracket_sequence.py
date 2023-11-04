# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок.
# Программа должна определить, является ли данная скобочная последовательность правильной.
# Пустая последовательность является правильной. Если A — правильная,
# то последовательности (A), [A], {A} — правильные.
# Если A и B — правильные последовательности, то последовательность AB — правильная.
#
# Формат ввода
# В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.
#
# Формат вывода
# Если данная последовательность правильная, то программа должна вывести строку "yes", иначе строку "no".

from collections import deque


def correct_brackets(brackets):
    brackets_deque = deque()
    open_close_brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    for bracket in brackets:
        if bracket in open_close_brackets.values():
            brackets_deque.append(bracket)
        else:
            if not brackets_deque or brackets_deque.pop() != open_close_brackets[bracket]:
                return "no"
    if brackets_deque:
        return "no"
    return "yes"


brackets = input()
print(correct_brackets(brackets))
