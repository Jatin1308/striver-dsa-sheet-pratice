# from typing import *
#
#
# def longestSuccessiveElements(a: List[int]) -> int:
# 	print("Inputs: ",a)
# 	ind = 1
# 	maxLen = 1
#
# 	ans = 0
#
# 	x = sorted(a)
#
# 	print("Sorted: ",x)
#
# 	while ind < len(a):
#
# 		if (x[ind] - x[ind - 1]) == 1:
# 			ind += 1
# 			maxLen += 1
# 			ans = max(ans,maxLen)
# 		else:
# 			ind += 1
# 			maxLen = 1
# 			ans = max(ans,maxLen)
#
# 	print("Op: ",maxLen)
# 	return ans
#
#
# # print(longestSuccessiveElements([5,8,3,2,1,4]))
#
# # print(longestSuccessiveElements([1, 2, 2, 1]))
#
# # print(longestSuccessiveElements([5,4,3]))
# #
# # print(longestSuccessiveElements([15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]))
#
#
#
# # print(longestSuccessiveElements([9,1,4,7,3,-1,0,5,8,-1,6]))
#
#
# # print(longestSuccessiveElements([100,4,200,1,3,2]))
#
# print(longestSuccessiveElements([1,2,0,1]))
# # print(longestSuccessiveElements([0,0]))






def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)


