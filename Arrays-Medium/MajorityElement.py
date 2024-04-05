# def majorityElement(v: [int]) -> int:
# 	n = len(v)
# 	half = n // 2
# 	d = {}
# 	maj = float("inf")
# 	for i in range(n):
# 		if v[i] not in d:
# 			d[v[i]] = 1
# 		else:
# 			d[v[i]] += 1
#
# 		if d[v[i]] > half:
# 			return v[i]

def majorityElement(v: [int]) -> int:
	currEle = None
	count = 0

	for i in range(len(v)):

		if count == 0:
			currEle = v[i]
			count += 1
		elif currEle == v[i]:
			count += 1
		else:
			count -= 1

	c = 0
	for i in range(len(v)):
		if v[i] == currEle:
			c+=1

	if c > (len(v)//2):
		return currEle
	return -1





print(majorityElement([2, 2, 1, 3, 1, 1, 3, 1, 1]))
