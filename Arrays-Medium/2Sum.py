# def read(n: int, book: [int], target: int) -> str:
# 	d = {}
# 	for i in range(n):
# 		if book[i] not in d:
# 			d[book[i]] = 1
# 		else:
# 			d[book[i]] += 1

# 		if target - book[i] == 0:
# 			return "No"

# 		if (target - book[i]) in d:
# 			return "YES"
# 	else:
# 		return "NO"

# print(read(2,[1,2],1))



# 2 pointer optimal solution -  can only work on sorted array
'''
def twoPointer(arr,target):
	arr = sorted(arr)

	left = 0
	right = len(arr)-1
	s = 0

	while left < right:
		s = arr[left] + arr[right]

		print(s,left,right)

		if s > target:
			right-=1
		elif s < target:
			left+=1
		else:
			return left, right
	return -1,-1
		

# print(twoPointer([2,6,5,8,11],11))

print(twoPointer([3,2,4],6))
'''




# dictionary approach to return indicies

def dicApproachToReturnIndicies(arr,target):
    
	d = {}

	'''
		a+b = target
		b = target-a
	'''

	for i in range(len(arr)):
		if arr[i] not in d:
			d[arr[i]] = i
		
	for j in range(len(arr)):
		if target-arr[j] in d and j != d[target-arr[j]]:
			return [j,d[target-arr[j]]]
	else:
		return [-1,-1]
	

# print(dicApproachToReturnIndicies([3,2,4],6))

print(dicApproachToReturnIndicies([2,6,5,8,10],13))