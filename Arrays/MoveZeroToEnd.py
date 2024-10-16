# -> for 2*n complexity solution

"""def moveZeros(n: int, a: [int]) -> [int]:
    d = {}
    l = []
    for x in a:
        if x == 0:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        else:
            l.append(x)
    if d.get(0):
        for i in range(d.get(0)):
            l.append(0)

    return l"""

# better approach is using the 2 pointers





def moveZeros2Pointers(n, arr):
    
    # to check if there is any zero in the array and assign the first zero's index to j
    j = -1
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    # it means there is no zero
    if j == -1:
        return arr


    # i will be initialized with j+1 and once i crosses boundary we will have our answer
    for i in range(j + 1, n+1):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    print(arr)


moveZeros2Pointers(4, [1, 0, 2, 0, 4])

moveZeros2Pointers(3, [8,6,9])
