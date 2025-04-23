def longestSubArraySumZero(arr):


    ''' use prefixSum algo '''

    prefSum, maxLen = 0, 0
    d = {}  # for storing the prefSum and its iden where we got it
    for i in range(len(arr)):
        prefSum += arr[i]
        if prefSum == 0:
            maxLen = i+1
        if prefSum in d:
            maxLen = max(maxLen,i-d[prefSum])
        if prefSum not in d:
            d[prefSum] = i
            print(d)
    return maxLen




    '''
    sol:  generate all the sub arrays

    Need to optimize it
    if sum(arr) == 0:
        return len(arr)
    
    fix = 0
    length = 0
    
    while fix < len(arr):
        moving = fix+1
        while moving < len(arr):
            s = sum(arr[fix:moving+1])
            if s == 0:
                length = max(length,len(arr[fix:moving+1]))
            moving+=1
        fix+=1
    return length
'''


# print(longestSubArraySumZero([9, -3, 3, -1, 6, -5]))

print(longestSubArraySumZero([-1, 1, -1, 1]))

# print(longestSubArraySumZero([6, -2, 2, -8, 1, 7, 4, -10]))

# print(longestSubArraySumZero([1, 3, -5, 6, -2]))