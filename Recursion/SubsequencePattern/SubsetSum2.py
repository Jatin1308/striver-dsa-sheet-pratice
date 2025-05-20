"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsetSum2(arr):

    n = len(arr)
    res = set()
    def solve(ind,subset):
        if ind == n:
            # print("CurrentSubset: ",subset,"len: ",len(subset))
            res.add(tuple(sorted(subset)))
            return

        subset.append(arr[ind])
        solve(ind+1,subset)
        subset.pop()
        solve(ind+1,subset)
    # arr = sorted(arr)
    solve(0,[])
    return list(res)

# print(subsetSum1([5,2,1]))
print(subsetSum2([1,2,2]))