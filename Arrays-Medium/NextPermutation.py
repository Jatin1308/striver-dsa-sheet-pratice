from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:

    ind = -1
    n = len(A)

    for i in range(n-2,-1,-1):
        if A[i] < A[i+1]:
            ind = i
            break
    if ind == -1:
        A = A[::-1]
        return A

    """justGreater = A[ind+1]
    justGreaterInd = 0

    for i in range(ind+1,n):
        if A[i] > A[ind]:
            if A[i] < justGreater:
                justGreater = A[i]
                justGreaterInd = i


    A[ind],A[justGreaterInd] = A[justGreaterInd],A[ind]
"""
    for i in range(n - 1, ind, -1):
        if A[i] > A[ind]:
            A[i], A[ind] = A[ind], A[i]
            break
    A[ind + 1:] = reversed(A[ind + 1:])

    return A




# print(nextGreaterPermutation([3,1,2]))

print(nextGreaterPermutation([2,1,5,4,3,0,0]))
