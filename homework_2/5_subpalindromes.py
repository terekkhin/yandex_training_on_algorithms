# Строка называется палиндромом, если она читается одинаково как слева направо,
# так и справа налево. Например, строки abba, ata являются палиндромами.
#
# Вам дана строка. Ее подстрокой называется некоторая непустая последовательность
# подряд идущих символов. Напишите программу, которая определит, сколько подстрок данной строки является палиндромами.
#
# Формат ввода
# Вводится одна строка, состоящая из прописных латинских букв. Длина строки не превышает 100000 символов.
#
# Формат вывода
# Выведите одно число — количество подстрок данной строки, которые являются палиндромами

def substring_equality(h, h_rev, x, a, b, length, p):
    return (h[a + length] + h_rev[b] * x[length]) % p == (h_rev[b + length] + h[a] * x[length]) % p


def bin_search(n, h, h_rev, x, p, i, shift):
    # shift = 1 for odd shift = 0 for honest
    left = 0
    right = min(i, n - i - shift)
    while left <= right:
        mid = (left + right) // 2
        if substring_equality(h, h_rev, x, i + shift, n - i, mid, p):
            left = mid + 1
        else:
            right = mid - 1
    return right + shift


def find_number_of_subpalindromes(s):
    n = len(s)
    p = 10**9 + 7
    x_ = 257
    h = [0]*(n + 1)
    h_rev = [0] * (n + 1)
    x = [0]*(n + 1)
    x[0] = 1
    for i in range(n):
        h[i + 1] = (h[i]*x_ + ord(s[i])) % p
        h_rev[i + 1] = (h_rev[i] * x_ + ord(s[n - i - 1])) % p
        x[i + 1] = (x[i] * x_) % p
    result = 0
    for i in range(n):
        result += bin_search(n, h, h_rev, x, p, i, 0) + bin_search(n, h, h_rev, x, p, i, 1)
    return result


s = input()
print(find_number_of_subpalindromes(s))

