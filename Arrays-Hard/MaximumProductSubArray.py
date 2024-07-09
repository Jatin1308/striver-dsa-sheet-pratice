from typing import List


def maxProduct(arr: List[int]) -> int:
    # first naive sol: generate all sub arrays and then check

    # optimal - two aproaches: 1. observational   2. kadane's algo
    '''
    Observations: 
        1. what if all the elements are +ve wit no zero: whole array is the answer
        2. what if even negatives no zeroes: whole array is the answer
        3. odd negatives and others are positives: in this case we can remove 1 negative and and how is the array shaped after this 
    '''
    pref =1
    suff = 1
    ans = float('-inf')
    n = len(arr)

    for i in range(len(arr)):
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1
        pref = pref * arr[i]
        suff = suff * arr[n-i-1]

        ans = max(ans,max(pref,suff))

    return ans

maxProduct([2,3,-2,4])

