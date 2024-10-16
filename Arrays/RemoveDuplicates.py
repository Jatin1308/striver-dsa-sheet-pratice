def removeDuplicates(arr, n):
    i = 0

    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i+1

    # by creating a set -> O(nlogn) +O(n)

arr = [1, 2, 2, 3, 3, 4]
res = (removeDuplicates(arr, 6))

print(arr[:res],arr)

