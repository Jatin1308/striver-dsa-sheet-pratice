def sumSubArrMin(arr):
    sub = []

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sub.append(min(arr[i:j+1]))
    return sum(sub)%(10**9+7)

# print(sumSubArrMin([3,1,2,4]))
# print(sumSubArrMin([11,81,94,43,3]))

def findNse(arr,n):
    nse = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        nse[i] = n if len(stack) == 0 else stack[-1]
        stack.append(i)
    return nse

def findPse(arr,n):
    pse = [-1]*n
    stack = []
    for i in range(0,n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        pse[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(i)
    return pse



def optimal(arr):
    n = len(arr)
    nse = findNse(arr,n)
    pse = findPse(arr,n)
    total = 0
    for i in range(n):
        left = i-pse[i]
        right = nse[i]-i
        total+=(right*left*arr[i])
    return total

print(optimal([3,1,2,4]))
# print(optimal([11,81,94,43,3]))