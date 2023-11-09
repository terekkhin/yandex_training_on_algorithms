# Строка S была записана много раз подряд, после чего от получившейся строки взяли префикс и дали вам.
# Ваша задача определить минимально возможную длину исходной строки S.
#
# Формат ввода
# В первой и единственной строке входного файла записана строка, которая содержит только
# латинские буквы, длина строки не превышает 50000 символов.
#
# Формат вывода
# Выведите ответ на задачу.

def substring_equality(h, x, a, b, length, p):
    return (h[a + length] + h[b] * x[length]) % p == (h[b + length] + h[a] * x[length]) % p


def find_base_line(s):
    n = len(s)
    if n == 0:
        return 0
    p = 10 ** 9 + 7
    x_ = 257
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    for i in range(n):
        h[i + 1] = (h[i] * x_ + ord(s[i])) % p
        x[i + 1] = (x[i] * x_) % p
    length = n - 1
    while not substring_equality(h, x, 0, n - length, length, p):
        length -= 1
    return n - length


s = input()
print(find_base_line(s))
