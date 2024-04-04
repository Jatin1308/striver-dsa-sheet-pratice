def longestSubarrayWithSumK(a: [int], k: int) -> int:
	n = len(a)

	left, right = 0, 0
	Sum = a[0]
	maxLen = 0

	while right < n:
		while left <= right and Sum > k:
			Sum -= a[left]
			left += 1
		if Sum == k:
			maxLen = max(maxLen, right - left + 1)
		right += 1

		if right < n:
			Sum += a[right]
	return maxLen


a = [2, 3, 5, 1, 9]
k = 10

print(longestSubarrayWithSumK(a, k))