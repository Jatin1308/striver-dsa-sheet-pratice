from os import *
from sys import *
from collections import *
from math import *


# def sortArray(arr, n):
# 	# Write your code here
# 	low, mid = 0, 0
# 	high = n - 1

# 	while mid <= high:
# 		if arr[mid] == 0:
# 			arr[low], arr[mid] = arr[mid], arr[low]
# 			low += 1
# 			mid += 1
# 		elif arr[mid] == 1:
# 			mid += 1
# 		else:
# 			arr[mid], arr[high] = arr[high], arr[mid]
# 			high -= 1

# 	return arr


# print(sortArray([2, 0, 2, 1, 1, 0], 6))




# we will use DNF(Dutch National Flag ) algo
'''
use 3 pointers - low, mid , high

0 ... low-1 -> extreme left (sorted) contains 0
low ... mid-1 -> contains 1
high+1 ... n-1 -> extreme right contains 2

we know from 0 ... mid-1 is sorted
and from high+1 ... n-1 is sorted

And we infer [mid,high] is unsorted
Initially we will start with entire array which is unsorted, so mid = 0 high = n-1
'''

def dnf(arr):
	mid = 0
	high = len(arr)-1
	low = 0

	while mid <= high:
		if arr[mid] == 0:
			arr[low],arr[mid] = arr[mid],arr[low]
			low+=1
			mid+=1
		elif arr[mid] == 1:
			mid+=1
		
		else:
			arr[mid],arr[high] = arr[high],arr[mid]
			high-=1

	
	return arr

print(dnf([2,0,1,2,1,1,0,1,0]))

print(dnf([2,0,0,0,0]))
print(dnf([2,1,1,1,1]))
print(dnf([2,2,2,2,0]))