from typing import List


'''
    brute force : use 3 loops, hashmap and set

    better approach : as we need a+b+c = 0 , we can get c = -(a+b)

    optimal approach  : 2-pointers
'''

def threeSum(arr: List[int]) -> List[List[int]]:
    
    arr = sorted(arr)
    ans = []
    fs = {}
    for i in range(len(arr)):
        if i>0 and arr[i] ==  arr[i-1]:
            continue

        j = i+1
        k = len(arr)-1

        while j<k:
            sum = arr[i] + arr[j] + arr[k]


            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
            else:
                s = [arr[i],arr[j],arr[k]]
                ans.append(s)
                j+=1
                k-=1

                while (j<k and arr[j] == arr[j-1]):
                    j+=1
                while (j < k and arr[k] == arr[k+1]):
                    k-=1
    return ans

print(threeSum([-1,0,1,2,-1,-4]))

