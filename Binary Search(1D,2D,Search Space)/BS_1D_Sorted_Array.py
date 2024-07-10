from typing import List

def binarySearch(arr,low,mid,high,target):
    if low <= mid:
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            print("target greater: ",arr[low],arr[mid],arr[high])
            low = mid+1
            return binarySearch(arr,low,(low+high)//2,high,target)
        elif target < arr[mid]:
            high = mid-1
            print("target lesser: ",arr[low],arr[mid],arr[high])
            return binarySearch(arr,low,(low+high)//2,high,target)
    return -1
    
    


def search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr)-1
    mid = (low+high) //2
    return binarySearch(arr,low,mid,high,target)


print(search([-1,0,3,5,9,12],12))