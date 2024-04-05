def printSubArrayInKadane(arr, n):
	ans = 0
	sum = 0
	start = 0
	for i in range(n):

		sum += arr[i]
		ans = max(sum, ans)

		if sum < 0:
			sum = 0
			start = i + 1

	return arr[start:i], sum


# print(printSubArrayInKadane([-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10], 15))
# print(printSubArrayInKadane([10, 20, -30, 40, -50, 60], 6))

print(printSubArrayInKadane([-2, -3, 4, -1, -2, 1, 5, -3], 8))
