def fourSum(arr,target):
    ans = []
    arr = sorted(arr)
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1,len(arr)):
            if j != i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = len(arr)-1

            while k < l:
                s = arr[i]
                s += arr[j]
                s += arr[k]
                s += arr[l]

                
                if s == target:
                    ans.append([arr[i],arr[j],arr[k],arr[l]])
                    k+=1
                    l-=1
                    while k < l and arr[k] == arr[k-1]:
                        k+=1
                    while k < l and arr[l] == arr[l+1]:
                        l-=1

                elif s < target:
                    k+=1
                else:
                    l-=1
    return ans


print(fourSum([2,2,2,2,2],8))