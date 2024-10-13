from collections import Counter

def xSum(nums,k,x):

    n = len(nums)
    result = []

    def helper(subarray,x):
        count = Counter(subarray)
        print(count)

        d = {}
        for ele in subarray:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele]+=1
        sortedKeys = sorted(count.items(),key = lambda item: (-item[1],-item[0]))
        
        totSum = 0

        for element, freq in sortedKeys[:x]:
            print(sortedKeys,element,freq)
            totSum+=element*freq
    
        return totSum

    for i in range(n-k+1):
        subarray = nums[i:i+k]
        result.append(helper(subarray,x))


    return result



# [1,1,2,2,3,4,2,3], k = 6, x = 2

# [3,8,7,8,7,5], k = 2, x = 2


# print(xSum([1,1,2,2,3,4,2,3],6,2))

print(xSum([3,8,7,8,7,5],2,2))