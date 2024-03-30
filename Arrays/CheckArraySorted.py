def isSorted(n: int, a: [int]) -> int:

    for i in range(len(a)-1):
        if a[i] <= a[i+1]:
            continue
        else:
            return 0
    else:
        return 1