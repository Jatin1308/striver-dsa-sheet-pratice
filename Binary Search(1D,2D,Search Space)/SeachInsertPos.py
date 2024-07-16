import time
def searchInsert(arr,target):
    if arr[-1] < target:
        return len(arr)
    if arr[0] > target:
        return 0
    low = 0
    high = len(arr)-1
    ans = len(arr)

    



    return ans

# def searchInsert(arr,target):
    # if arr[-1] < target:
    #     return len(arr)
    # if arr[0] > target:
    #     return 0
#     def searchPosUsingBS(arr,target):
#         low = 0
#         high = len(arr)-1
#         mid = (low+high)//2
#         while low <= high:
#             time.sleep(1)
#             if arr[mid] == target:
#                 print("Equal","low:",arr[low],"mid:",arr[mid],"high:",arr[high],low,mid,high)
#                 return mid
#             elif arr[mid] > target:
#                 print("MidGreater: ","low:",arr[low],"mid:",arr[mid],"high:",arr[high],low,mid,high)
#                 if arr[mid-1] < target and target < arr[mid]:
#                     return mid
#                 high = mid - 1
#             else:
#                 print("MidLesser","low:",arr[low],"mid:",arr[mid],"high:",arr[high],low,mid,high)
#                 if arr[mid+1] > target and target > arr[mid-1]:
#                     return mid
#                 low = mid + 1
#             mid = ( low + high )//2
#     return searchPosUsingBS(arr,target)
    

print(searchInsert([1,3],2))
print(searchInsert([1,3,5],4))