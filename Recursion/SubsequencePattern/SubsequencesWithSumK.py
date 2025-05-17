def subSequencesWithSumK(nums,k):
    res = []
    n = len(nums)
    def solve(currSeq,currSum,ind):
        if ind == n:
            if currSum == k:
                # print(currSeq)
                res.append(list(currSeq))
                return True
            return False
        currSeq.append(nums[ind])
        currSum+=nums[ind]

        if solve(currSeq,currSum,ind+1):
            return True
        currSeq.pop()
        currSum-=nums[ind]
        if solve(currSeq,currSum,ind+1):
            return True

        return False

    solve([],0,0)
    return res

print(subSequencesWithSumK([1,2,1],2))