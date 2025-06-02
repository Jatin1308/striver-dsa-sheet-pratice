def trappingRainWater(arr):

    lmax = 0
    rmax = 0
    total = 0
    l = 0
    r = len(arr)-1

    while l<r:
        if arr[l] < arr[r]:
            if lmax >arr[l]:
                total+=lmax-arr[l]
            else:
                lmax = arr[l]
            l+=1
        else:
            if rmax > arr[r]:
                total+=rmax-arr[r]
            else:
                rmax=arr[r]
            r-=1
    return total

print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))