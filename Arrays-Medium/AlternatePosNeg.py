from typing import *


def alternateNumbers(a: List[int]) -> List[int]:
	ans = [0] * len(a)
	pos = 0
	neg = 1
	for x in a:
		if x < 0:
			ans[neg] = x
			neg += 2

		elif x >= 0:
			ans[pos] = x
			pos += 2

	return ans


print(alternateNumbers([1, 2, -4, -5]))
