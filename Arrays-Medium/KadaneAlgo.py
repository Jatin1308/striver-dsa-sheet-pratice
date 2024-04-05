def maxSubarraySum(arr, n):
	ans = 0
	sum = 0
	for i in range(n):
		sum += arr[i]
		ans  = max(sum,ans)
		if sum < 0:
			sum  = 0

	return ans

print(maxSubarraySum([-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10], 15))

# print(maxSubArraySum([-7, -8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10], 15))
