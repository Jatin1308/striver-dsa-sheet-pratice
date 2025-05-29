# do with bit manipulation
"""
    2**n = 1<<n, always
"""
def powerSet(nums):
    n = len(nums)
    numbOfSubs = 1<<n  #2**len(nums)
    ans = []
    for i in range(numbOfSubs):
        l = []
        for j in range(n):
            if (i >> j) & 1:
                l.append(nums[j])
        ans.append(l)
    return ans



print(powerSet([1,2,3]))