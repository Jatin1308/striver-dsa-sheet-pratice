def subsetSum1(arr):

    n = len(arr)
    res = []
    def solve(ind,subset):
        if ind == n:
            print("CurrentSubset: ",subset)
            res.append(sum(list(subset)))
            return

        subset.append(arr[ind])
        solve(ind+1,subset)
        subset.pop()
        solve(ind+1,subset)
    # arr = sorted(arr)
    solve(0,[])
    return sorted(res)

# print(subsetSum1([5,2,1]))
print(subsetSum1([1,2,2]))