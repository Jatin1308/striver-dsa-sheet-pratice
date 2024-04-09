from typing import *

def superiorElements(arr : List[int]) -> List[int]:
    # Write your code here.

    max = float("-inf")

    ans = []

    for i in range(len(arr)-1,-1,-1):
        if arr[i] > max:
            max = arr[i]
            ans.append(arr[i])

    return ans


print(superiorElements([10,22,12,3,0,6]))