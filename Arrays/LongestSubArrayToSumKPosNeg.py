def getLongestSubarray(a, k):
	prefixSum = 0
	d = {}
	maxLen = 0

	for i in range(len(a)):
		prefixSum += a[i]
		if prefixSum == k:
			maxLen = max(maxLen,i + 1)

		rem = prefixSum - k
		if rem in d:
			maxLen = max(maxLen, i - d[prefixSum - k])

		if prefixSum not in d:
			d[prefixSum] = i

	return maxLen


print(getLongestSubarray([-50, 0, 52], 2))

# print(getLongestSubarray([-1,0,1,1,1], 3))