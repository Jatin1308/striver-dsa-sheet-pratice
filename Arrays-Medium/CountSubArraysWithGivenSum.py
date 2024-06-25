# def countSubArraySum(n,arr,k):

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     def findAllSubarraysWithGivenSumBrute(arr, k):
#         n = len(arr)  # size of the given array.
#         cnt = 0  # Number of subarrays.

#         for i in range(n):  # starting index i.
#             for j in range(i, n):  # ending index j.
#                 # calculate the sum of subarray [i...j].
#                 subarray_sum = sum(arr[i:j+1])

#                 # Increase the count if sum == k.
#                 if subarray_sum == k:
#                     cnt += 1

#         return cnt
    
#     # findAllSubarraysWithGivenSumBrute(arr,k)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     def findAllSubarraysWithGivenSumOptimal(arr, k):
#         n = len(arr)  # size of the given array.
#         cnt = 0  # Number of subarrays.

#         for i in range(n):  # starting index i.
#             subarray_sum = 0
#             for j in range(i, n):  # ending index j.
#                 # calculate the sum of subarray [i...j]
#                 # sum of [i..j-1] + arr[j]
#                 subarray_sum += arr[j]

#                 # Increase the count if sum == k.
#                 if subarray_sum == k:
#                     cnt += 1

#         return cnt
    
#     # findAllSubarraysWithGivenSumOptimal(arr,k)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     from collections import defaultdict
#     def findAllSubarraysWithGivenSumMostOptimal(arr, k):
#         n = len(arr) # size of the given array.
#         mpp = defaultdict(int)
#         preSum = 0
#         cnt = 0

#         mpp[0] = 1 # Setting 0 in the map.
#         for i in range(n):
#             # add current element to prefix Sum:
#             preSum += arr[i]

#             # Calculate x-k:
#             remove = preSum - k

#             # Add the number of subarrays to be removed:
#             cnt += mpp[remove]

#             # Update the count of prefix sum
#             # in the map.
#             mpp[preSum] += 1

#         return cnt
    
#     findAllSubarraysWithGivenSumMostOptimal(arr,k)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def countSubArrayWithSumK(arr,k):
    count = 0
    d = {}
    prefSum = 0

    for i in range(len(arr)):
        prefSum += arr[i]

        if prefSum == k:
            count+=1
        
        if prefSum-k in d:
            count += d[prefSum-k]
        

        # here i will be storing the count of prefSum-k in the dict, 
        if prefSum not in d:
            d[prefSum] = 1
        else:
            d[prefSum]+=1
    
    print(count)



countSubArrayWithSumK([1,2,3],3)

countSubArrayWithSumK([1,1,1],2)

countSubArrayWithSumK([1],0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`


# def countSubArrayWithSumK(arr,k):
#     d = {}
#     d[0]=1
#     pre = 0
#     cnt = 0
#     for i in range(len(arr)):
#         pre+=arr[i]
#         rem = pre-k
#         cnt+=d[rem]
#         d[pre] +=1
#     return cnt



