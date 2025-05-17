def combinationSumWithRepeatedNumbers(nums,target):
    n = len(nums)
    res = []

    def solve(currSeq, target, ind):
        if target <= 0 or ind == n:
            if target == 0:
                res.append(list(currSeq))
            return

        currSeq.append(nums[ind])
        solve(currSeq,target-nums[ind],ind)
        currSeq.pop()
        solve(currSeq, target, ind+1)
    solve([],target,0)
    return res

print(combinationSumWithRepeatedNumbers([2,3,6,7],7))