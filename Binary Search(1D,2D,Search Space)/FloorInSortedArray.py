def binarySearch(arr,low,mid,high,target):
    if low <= mid:
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            # print("target greater: ",arr[low],arr[mid],arr[high])
            low = mid+1
            return binarySearch(arr,low,(low+high)//2,high,target)
        elif target < arr[mid]:
            high = mid-1
            # print("target lesser: ",arr[low],arr[mid],arr[high])
            return binarySearch(arr,low,(low+high)//2,high,target)
    else:
        # print("ELSE: ",arr[low],arr[mid],arr[high],arr)
        return mid
    
def search(arr, target: int) -> int:
    low = 0

    high = len(arr)-1
    mid = (low+high) //2
    return binarySearch(arr,low,mid,high,target)

def findFloor(arr,n,target):
    res = search(arr,target)
    return res


print("The floor for 5 is: ",findFloor([1,2,8,10,11,12,19],7,5))

print("The floor for 0 is: ",findFloor([1,2,8,10,11,12,19],7,0))