# По данному числу N (0 < N < 10) выведите все перестановки чисел от 1 до N в лексикографическом порядке.

def permutations(arr, used, index=0):
    if index == len(arr):
        print("".join(map(str, arr)))

    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            arr[index] = i
            permutations(arr, used, index + 1)
            used[i] = False


N = int(input())
arr = [i for i in range(1, N + 1)]
used = [False]*(N + 1)
permutations(arr, used)


