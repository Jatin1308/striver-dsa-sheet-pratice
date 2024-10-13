from typing import List

def minBitwiseArray(nums: List[int]) -> List[int]:
    # n = len(nums)
    # ans = [-1]*n
    '''
    for i in range(n):
        num = nums[i]
        for x in range(num):
            if x | (x+1) == num:
                ans[i] = x
                break
    
    return ans'''


    # optimized approach

    ans = []
    for num in nums:

        if num & 1 == 0:
            ans.append(-1)
        else:
            x = (num-1)//2
            if x | (x+1) == num:
                ans.append(x)
            else:
                ans.append(-1)
    return ans




print(minBitwiseArray([2,3,5,7]))
# print(minBitwiseArray([11,13,31]))

print(minBitwiseArray([884532611,741533369,868936609,816315823,150570781,346594697,334726181,921762641,89355881,403165729,931242733]))