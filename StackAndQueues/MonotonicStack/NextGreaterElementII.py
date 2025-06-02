from typing import List
def nge2(nums):
    n = len(nums)
    nge = [-1]*n
    stack : List = []

    for i in range(2*n-1,-1,-1):
        while stack and stack[-1]<=nums[i%n]:
            stack.pop()

        if i<n:
            nge[i] = -1 if len(stack) == 0 else stack[-1]

        stack.append(nums[i%n])

    return nge


print(nge2([1,2,1]))

print(nge2([1,2,3,4,3]))