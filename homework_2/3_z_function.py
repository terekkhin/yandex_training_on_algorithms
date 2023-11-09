# Дана непустая строка S, длина которой N не превышает 10**6.
# Будем считать, что элементы строки нумеруются от 0 до N-1.
#
# Вычислите z-функцию z[i] для всех i от 0 до N-1.
# z[i] определяется как максимальная длина подстроки, начинающейся с позиции i и
# совпадающей с префиксом всей строки. z[0] = 0
#
# Формат ввода
# Одна строка длины N, 0 < N ≤ 10**6, состоящая из прописных латинских букв.
#
# Формат вывода
# Выведите N чисел — значения z-функции для каждой позиции, разделённые пробелом.


def substring_equality(h, x, a, b, length, p):
    return (
        (h[a + length] + h[b]*x[length]) % p == (h[b + length] + h[a]*x[length]) % p
    )


def calculate_hash(s, p, x_):
    n = len(s)
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    for i in range(n):
        h[i + 1] = (h[i] * x_ + ord(s[i])) % p
        x[i + 1] = (x[i] * x_) % p
    return h, x


def find_z_function(s):
    p = 10 ** 9 + 7
    x_ = 257
    hsh, x = calculate_hash(s, p, x_)
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        left = 0
        right = n - i
        mid = (left + right) // 2
        while left <= right:
            if substring_equality(hsh, x, 0, i, mid, p):
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        z[i] = mid
    return z


s = input()
print(*find_z_function(s), sep=" ")
