class Solution:
    #Back-end complete function Template for Python 3

    #global variable to count total inversions
    inversion_count = 0

    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        global inversion_count
        inversion_count = 0
        self.merge_sort(arr, 0, n - 1)
        #returning the count of inversions in the array.
        return inversion_count

    #Function to sort and merge two parts of array.
    def merge(self, arr, start, mid, end):
        global inversion_count
        temp = [0 for i in range(end - start + 1)]

        #i is pointer for left subarray.
        #j is pointer for right subarray.
        #k is index for resultant merged subarray.
        i, j, k = start, mid + 1, 0

        #Using two pointers over the array which helps in storing the
        #smaller element and thus merging the subarray.
        while i <= mid and j <= end:
            #Comparing element of the array at pointers i and j and accordingly
            #storing the smaller element and updating the pointers.
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                k += 1
                i += 1
            else:
                temp[k] = arr[j]
                k += 1
                j += 1
                #Adding the inversions which is the number of elements which
                #are smaller than arr[j] in the left half of the array.
                inversion_count += mid - i + 1

        #Copying the remaining elements of left subarray(if there are any) to temp.
        while i <= mid:
            temp[k] = arr[i]
            k += 1
            i += 1

        #Copying the remaining elements of right subarray(if there are any) to temp.
        while j <= end:
            temp[k] = arr[j]
            k += 1
            j += 1

        #Copying back the merged elements to original array.
        for i in range(start, end + 1):
            arr[i] = temp[i - start]

    #Function to mergesort the array, which uses divide and conquer algorithm
    #on left and right halves of array for mergesort operation.
    def merge_sort(self, arr, start, end):
        if start < end:
            mid = (start + end) // 2
            #Calling recursive function to sort left half of the array.
            self.merge_sort(arr, start, mid)
            #Calling recursive function to sort right half of the array.
            self.merge_sort(arr, mid + 1, end)
            #Calling merge function which sorts and merges both halves
            #of the array obtained after calling both recursive function.
            self.merge(arr, start, mid, end)
        




    '''
    TC: O(n^2)

    invCount = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j] and i<j:
                print(arr[i],arr[j])
                invCount+=1
    return invCount'''

print(countInversions([2, 4, 1, 3, 5]))

# print(countInversions([10,10,10]))

# print(countInversions([2, 3, 4, 5, 6]))
