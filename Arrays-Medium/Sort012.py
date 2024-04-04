from os import *
from sys import *
from collections import *
from math import *


def sortArray(arr, n):
	# Write your code here
	low, mid = 0, 0
	high = n - 1

	while mid <= high:
		if arr[mid] == 0:
			arr[low], arr[mid] = arr[mid], arr[low]
			low += 1
			mid += 1
		elif arr[mid] == 1:
			mid += 1
		else:
			arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1

	return arr


print(sortArray([2, 0, 2, 1, 1, 0], 6))
