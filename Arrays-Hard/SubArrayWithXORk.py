def longestSubArrayWithXORk(arr,k):
    prefXor = 0
    count = 0
    d = {}     # prefXor,count
    d[0] = 1
    for i in range(len(arr)):

        ''' 
            x^k = XR
            x^k^k = XR^k
            x = XR^k 
        '''
        prefXor ^= arr[i]
        x = k^prefXor
        count += d.get(x,0)
        d[prefXor] = d.get(prefXor,0)+1 
    return count




print(longestSubArrayWithXORk([4, 2, 2, 6, 4],6))



'''
    is there are subarray ending at 6 & having XOR of k
'''