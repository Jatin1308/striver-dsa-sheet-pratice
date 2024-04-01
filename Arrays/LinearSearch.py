def linearSearch(n: int, num: int, arr: [int]) -> int:
    for i in range(n):
        if arr[i] == num:
            return i
    else:
        return -1


print(linearSearch(5, 1, [1, 2, 3, 4, 1, 5]))
