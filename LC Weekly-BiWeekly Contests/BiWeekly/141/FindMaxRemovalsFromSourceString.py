def canPerformOperations(source, pattern, targetIndicies, k):
    n = len(source)
    m = len(pattern)

    removed = set(targetIndicies[:k])

    # use 2 pointers if pattern is subsequence of modified source
    j = 0 # pointer for pattern

    for i in range(n):
        if i in removed:
            continue #skip removed indicies
        if j <m and source[i] == pattern[j]:
            j+=1 # match current character with [attern]
        if j==m:
            return True # pattern is still a subsequence
        
    return j == m

def maxOperations(source, pattern, targetIndicies):

    left,right = 0,len(targetIndicies)

    result = 0


    while left <= right:
        mid = (left+right)//2
        if canPerformOperations(source,pattern,targetIndicies,mid):
            result = mid
            left = mid+1
        else:
            right = mid-1

    return result


print(maxOperations("abbaa","aba",[0,1,2]))