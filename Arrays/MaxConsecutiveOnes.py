def traffic(n, m, arr):
    i = 0 # lazy window pointer
    j = 0 # continuous iterator
    zeroCount = 0
    ans = 0

    while j < n:
        if arr[j] == 0:
            zeroCount += 1
        while zeroCount > m:
            if arr[i] == 0:
                zeroCount -= 1
            i += 1
        ans = max(ans,j-i+1)
        j += 1
    return ans







# print(traffic(3,1,[0,1,1]))

print(traffic(6, 3, [0, 1, 0, 0, 1, 0]))
