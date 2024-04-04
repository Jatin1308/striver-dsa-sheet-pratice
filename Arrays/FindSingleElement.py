from typing import *


def getSingleElement(arr: List[int]) -> int:
	ans = arr[0]
	for i in range(1, len(arr)):
		ans = ans ^ arr[i]

	return ans


# print(getSingleElement([1, 1, 2, 3, 3, 4, 4]))

print(getSingleElement([8,8,2,2,0,3,3]))