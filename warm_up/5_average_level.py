# В группе учатся n студентов, каждый из которых имеет свой рейтинг a_i.
# Им нужно выбрать старосту; для этого студенты хотят выбрать старосту таким образом чтобы
# суммарный уровень недовольства группы был минимальный. Если выбрать j-го старостой, то уровень недовольства
# i-го студента равен |a_i - a_j|
# Вычислите уровень недовольства группы при выборе каждого из студентов старостой.

n = int(input())
a = list(map(int, input().split()))
result = []
for i in range(n):
    if i == 0:
        result.append(sum(map(lambda x: abs(x - a[0]), a)))
    elif a[i] == a[i - 1]:
        result.append(result[i - 1])
        continue
    else:
        sub = (a[i] - a[i-1])
        result.append(result[i - 1] + sub*i - sub*(n - i))
print(*result)
