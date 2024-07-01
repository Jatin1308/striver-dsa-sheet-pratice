def findElements(arr,n):
    
    '''without extra space '''

    ''' using simple math formulae '''
    SN = n*(n+1)//2
    S2N = (n*(n+1)*(2*n+1))//6

    S = 0
    S2 = 0
    for i in range(n):
        S+=arr[i]
        S2+=arr[i]*arr[i]

    val1 = S-SN   # x-y
    val2 = S2-S2N

    val2 = val2/val1  # x+y


    x = (val1+val2)//2

    y = x-val1

    return [x,y] 












    

    ''' with extra space
    smallestMissing = float("inf")
    ans = []
    d = {}
    for ele in arr:
        d[ele] = d.get(ele,0)+1

    # print("Prepared Dict: ",d)
    for key in d.keys():
        if d[key] == 2:
            ans.append(key)
    # print("Repeating: ",ans)


    for i in range(1,n+1):
        if i not in d:
            # print(smallestMissing,i)
            smallestMissing = min(smallestMissing,i)
    ans.append(smallestMissing)
    # print("Missing: ",ans)

    
    return ans

'''

# print(findElements([1,3,3]))

# print(findElements([21,12,20,17,15,36,22,6,29,3,4,34,5,1,23,32,14,31,25,18,19,39,19,13,8,9,7,37,11,27,33,24,2,26,35,38,10,16,28]))

print(findElements([12 ,7 ,5 ,1, 13 ,1 ,10 ,8 ,11 ,9 ,2 ,4 ,3 ,6],14))

# print(findElements([2,2],2))