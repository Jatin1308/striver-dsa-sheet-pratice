# def greatestProperDivisor(x):

#     if x <=1:
#         return 0  # no proper divisor
    
#     for i in range(x//2,0,-1):
#         if x%i == 0:
#             return i
        
#     return 1  # if x is prime, the greatest proper divisor is 1


# def minOperationsToNonDecreasing(nums):
#     n = len(nums)

#     totalOperations = 0

#     for i in range(n-2,-1,-1):
#         while nums[i] > nums[i+1]:

#             gpd = greatestProperDivisor(nums[i])

#             if gpd == 0 or gpd == 1:
#                 return -1
            
#             nums[i]//=gpd
#             totalOperations+=1

#             if nums[i] <=0:
#                 return -1
            
#     return totalOperations





from typing import List
class Solution:
    def greatestProperDivisor(self,x):

        if x <=1:
            return 0  # no proper divisor
        
        for i in range(x//2,0,-1):
            if x%i == 0:
                return i
            
        return 1  # if x is prime, the greatest proper divisor is 1

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        totalOperations = 0

        for i in range(n-2,-1,-1):
            while nums[i] > nums[i+1]:
                gpd = self.greatestProperDivisor(nums[i])
                if gpd <= 1:
                    return -1
                
                divCount = 0
                while nums[i] > nums[i+1]:
                    nums[i] //= gpd
                    divCount+=1
                totalOperations+=divCount

            if nums[i]<=0:
                return -1
            
        return totalOperations

# print(minOperationsToNonDecreasing([25,7]))
s = Solution()
print(s.minOperations([7,7,6]))
print(s.minOperations([1,1,1,1]))