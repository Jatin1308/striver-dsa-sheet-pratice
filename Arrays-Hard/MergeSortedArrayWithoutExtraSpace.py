def merge(a : list,b: list):

    a = removeZero(a)
    b = removeZero(b)
    
    # without extra space
    n = len(a)
    m = len(b)

    left = n-1
    right = 0

    while left >=0  and right < m:
        if a[left] > b[right]:
            a[left],b[right] = b[right],a[left]
            left -= 1
            right+=1
        else:
            # so it means all the elements are in the correct place and we no need to go further
            break
    
    a = sorted(a)
    b = sorted(b)

    a.extend(b)

    return a

def removeZero(a):
    res = [i for i in a if i != 0] 
    print(res)
    return res 

    
    # # with extra space

    # left, right = 0, 0
    # index = 0
    # ans = [0]*(len(a)+len(b))

    # while left < len(a) and right < len(b):
    #     if a[left]<= b[right]:
    #         ans[index] = a[left]
    #         left+=1
    #         index+=1
    #     else:
    #         ans[index] = b[right]
    #         right+=1
    #         index+=1
    
    # while left < len(a):
    #     ans[index] = a[left]
    #     left+=1
    #     index+=1

    # while right < len(b):
    #     ans[index] = b[right]
    #     right+=1
    #     index+=1
    
    


    

    


# l = [1,3,4,7]
# m = [4,9,11,13,15,19,33]
l = [1,2,3,0,0,0]
m = [2,5,6]
print(merge(l,m))