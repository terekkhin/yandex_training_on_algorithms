# Поразрядная сортировка является одним из видов сортировки, которые работают практически за линейное от
# размера сортируемого массива время. Такая скорость достигается за счет того, что эта сортировка использует
# внутреннюю структуру сортируемых объектов. Изначально этот алгоритм использовался для сортировки перфокарт.
# Первая его компьютерная реализация была создана в университете MIT Гарольдом Сьюардом (Harold Н. Seward).
# Опишем алгоритм подробнее. Пусть задан массив строк s1 , ..., si причём все строки имеют одинаковую длину m.
# Работа алгоритма состоит из m фаз. На i -ой фазе строки сортируются па i -ой с конца букве.
# Происходит это следующим образом. Будем, для простоты, в этой задаче рассматривать строки из цифр от 0 до 9.
# Для каждой цифры создается «корзина» («bucket»), после чего строки si распределяются по «корзинам» в
# соответствии с i-ой цифрой с конца. Строки, у которых i-ая с конца цифра равна j попадают в j-ую корзину
# (например, строка 123 на первой фазе попадет в третью корзину, на второй — во вторую, на третьей — в первую).
# После этого элементы извлекаются из корзин в порядке увеличения номера корзины. Таким образом, после первой
# фазы строки отсортированы по последней цифре, после двух фаз — по двум последним, ..., после m фаз — по всем.
# При важно, чтобы элементы в корзинах сохраняли тот же порядок, что и в исходном массиве (до начала этой фазы).
# Например, если массив до первой фазы имеет вид: 111, 112, 211, 311, то элементы по корзинам распределятся
# следующим образом: в первой корзине будет. 111, 211, 311, а второй: 112. Напишите программу, детально
# показывающую работу этого алгоритма на заданном массиве.
#
# Формат ввода
# Первая строка входного файла содержит целое число n (1 ≤ n ≤ 1000) .
# Последующие n строк содержат каждая по одной строке si . Длины всех si , одинаковы и не превосходят 20.
# Все si состоят только из цифр от 0 до 9.
#
# Формат вывода
# В выходной файл выведите исходный массив строк в, состояние «корзин» после распределения элементов по
# ним для каждой фазы и отсортированный массив. Следуйте формату, приведенному в примере.

n = int(input())
if n != 0:
    numbers = []
    for i in range(n):
        numbers.append(input())
    print("Initial array:")
    print(*numbers, sep=", ")
    buckets = [[] for _ in range(10)]
    for i in range(len(numbers[0])):
        print("**********")
        print(f"Phase {i + 1}")
        if i != 0:
            for k in buckets:
                numbers += k
        for j in range(len(numbers)):
            if i == 0:
                buckets[int(numbers[j][-i - 1])].append(numbers[j])
            else:
                buckets[int(numbers[j][-i])].remove(numbers[j])
                buckets[int(numbers[j][-i - 1])].append(numbers[j])
        numbers = []
        for j in range(len(buckets)):
            if len(buckets[j]) != 0:
                print(f"Bucket {j}: ", end="")
                print(*buckets[j], sep=", ")
            else:
                print(f"Bucket {j}: empty")
    print("**********")
    for k in buckets:
        numbers += k
    print("Sorted array:")
    print(*numbers, sep=", ")





