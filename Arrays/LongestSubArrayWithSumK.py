# def longestSubarrayWithSumK(a: [int], k: int) -> int:
# 	n = len(a)

# 	left, right = 0, 0
# 	Sum = a[0]
# 	maxLen = 0

# 	while right < n:
# 		while left <= right and Sum > k:
# 			Sum -= a[left]
# 			left += 1
# 		if Sum == k:
# 			maxLen = max(maxLen, right - left + 1)
# 		right += 1

# 		if right < n:
# 			Sum += a[right]
# 	return maxLen



#optimal

# def longestSubArrayWithHashingTech(arr,k):
# 	n = len(arr)
# 	d = {}
# 	maxLen = 0
# 	sum = 0

# 	for i in range(n):
# 		sum+=arr[i]

# 		if sum == k:
# 			maxLen = max(maxLen,i+1)

# 		remaining = sum-k

# 		if remaining in d:
# 			lenOfSubArr = i - d[remaining]
# 			maxLen = max(lenOfSubArr,maxLen)

# 		if sum not in d:
# 			d[sum] = i

# 		# d[sum] = i
# 	return maxLen

# a = [1,1,-1,1, 3, 5, 1, 9]
# k = 10
# # a = [2,0,0,3]
# # k = 3
# print(longestSubArrayWithHashingTech(a,k))




# BEST SOLUTION - 2 pointer greedy approach


def twoPointerApproach(a,k):
    
	i = 0
	j = 0
	s= 0
	maxLen = float('-inf')
	while j < len(a) and i <len(a):
		s += a[j]
		j+=1

		if s > k:
			while s > k:
				s -= a[i]
				i+=1
		if s == k:
			maxLen = max(maxLen,j-i)
	return maxLen


a = [1,1,-1,1, 3, 5, 1, 9]
k = 10


a = [2,0,0,3]
k = 3
print(twoPointerApproach(a,k))