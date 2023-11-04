# Задано две строки, нужно проверить, является ли одна анаграммой другой.
# Анаграммой называется строка, полученная из другой перестановкой букв.
#
# Формат ввода
# Строки состоят из строчных латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.
#
# Формат вывода
# Выведите "YES" если одна из строк является анаграммой другой и "NO" в противном случае.

def anagram():
    first = input()
    second = input()

    word_dict = {}
    for char in first:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1

    for char in second:
        if char in word_dict:
            word_dict[char] -= 1
            if word_dict[char] < 0:
                return "No"
        else:
            return "No"

    if any(word_dict.values()):
        return "No"
    print('YES')


print(anagram())

# def anagram():
#     first = input()
#     second = input()
#
#     first = sorted(list(first))
#     second = sorted(list(second))
#
#     if len(first) != len(second):
#         return "NO"
#     for i in range(len(first)):
#         if first[i] != second[i]:
#             return "NO"
#     return "YES"
#
#
# print(anagram())
