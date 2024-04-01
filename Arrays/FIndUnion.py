def sortedArray(a: [int], b: [int]) -> [int]:
    i = 0
    j = 0
    l = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1

    # print(l, "i: ", i, "j:", j)
    if i >= len(a):
        while j < len(b):
            l.append(b[j])
            j += 1
    else:
        while i < len(a):
            # print(i)
            l.append(a[i])
            i += 1
    print(l)


# sortedArray([1, 2, 3, 4], [2, 3, 5])

sortedArray([1, 2, 3, 4], [2, 3, 5])