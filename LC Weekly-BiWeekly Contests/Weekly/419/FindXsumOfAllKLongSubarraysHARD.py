from collections import Counter
import heapq
def xSum(nums,k,x):

    result = []
    freq = Counter()
    for i in range(k):
        freq[nums[i]] += 1
    def calcXSum(freq,x):
        sortedEle = sorted(freq.items(), key=lambda item: (-item[1],-item[0]))
        xSum = 0
        for i in range(min(x,len(sortedEle))):
            count,num = sortedEle[i]
            xSum+=count*num

        return xSum
                       


    #     freqList = [(-count,num) for num,count in freq.items()]
    #     heapq.heapify(freqList)

    #     # extract top x elements from heap
    #     xSum = 0
    #     for _ in range(x):
    #         if freqList:
    #             count,num = heapq.heappop(freqList)
    #             xSum+= -count*num    # add freq times number
    #     return xSum


    result.append(calcXSum(freq,x))
    for i in range(k,len(nums)):
        outEle = nums[i-k]
        freq[outEle] -= 1
        if freq[outEle] == 0:
            del freq[outEle]
        incomingEle = nums[i]
        freq[incomingEle]+=1
        result.append(calcXSum(freq,x))
    return result

# [1,1,2,2,3,4,2,3], k = 6, x = 2

# [3,8,7,8,7,5], k = 2, x = 2


print(xSum([1,1,2,2,3,4,2,3],6,2))

print(xSum([3,8,7,8,7,5],2,2))