def canPerformOperations(source, pattern, targetIndicies, k):
    n = len(source)
    m = len(pattern)

    removed = set(targetIndicies[:k])


    j = 0

    for i in range(n):
        if i in removed:
            continue
        if j <m and source[i] == pattern[j]:
            j+=1
        if j==m:
            return True
        
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