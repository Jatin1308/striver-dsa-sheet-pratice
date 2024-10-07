import math
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        gcdPairs = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):

                gcd_value = math.gcd(nums[i],nums[j])
                gcdPairs.append(gcd_value)
        
        gcdPairs.sort()

        ans = []

        for query in queries:
            ans.append(gcdPairs[query])

        return ans