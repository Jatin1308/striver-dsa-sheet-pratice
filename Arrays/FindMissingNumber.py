from typing import List


def missingNumber(nums: List[int]) -> int:
    """approach 1"""
    # for i in range(len(nums)):
    #     if i not in nums:
    #         return i

    """approach 2"""
    # Now, let’s XOR all the numbers between 1 to N.
    # xor1 = 1^2^.......^N

    # Let’s XOR all the numbers in the given array.
    # xor2 = 1^2^......^N (contains all the numbers except the missing one).

    # Now, if we again perform XOR between xor1 and xor2, we will get:
    # xor1 ^ xor2 = (1^1)^(2^2)^........^(missing Number)^.....^(N^N)

    n = len(nums)
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for num in nums:
        ans ^= num
    return ans


print(missingNumber([3, 0, 1]))
