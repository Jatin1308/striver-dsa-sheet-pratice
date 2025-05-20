# def combinationSumWithNoRepeatedNumbers(nums,k):
#     n = len(nums)
#     res = set()
#
#     def solve(currSeq, target, ind):
#         if target <= 0 or ind == n:
#             if target == 0:
#                 res.add(tuple(sorted(currSeq)))
#             return
#
#
#         currSeq.append(nums[ind])
#         solve(currSeq,target-nums[ind],ind+1)
#         currSeq.pop()
#         solve(currSeq, target, ind+1)
#     solve([],k,0)
#     return list(res)
#

def moreOptimal(nums, k):
    ans = []
    n = len(nums)
    def solve(ind,target,currSubs):
        if target == 0:
            ans.append(list(currSubs))
            return

        for i in range(ind,n):
            if i > ind and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            currSubs.append(nums[i])
            solve(i+1,target-nums[i],currSubs)
            currSubs.pop()
    nums = sorted(nums)
    print(nums)
    solve(0,k,[])
    return ans


# print(combinationSumWithNoRepeatedNumbers([4,2,3,6,7],7))

# print(moreOptimal([10, 1, 2, 7, 6, 1, 1, 1, 15], 8))

print(moreOptimal([2,5,2,1,2],5))