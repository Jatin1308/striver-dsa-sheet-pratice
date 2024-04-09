from sys import *
from collections import *
from math import *


"""Better Approach ->  using two arrays for column and rows"""

def zeroMatrixBetter(matrix, n, m):

	cols = [0 for i in range(m)]
	rows = [0 for j in range(n)]

	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				cols[j] = 1
				rows[i] = 1

	for i in range(n):
		for j in range(m):
			if rows[i] or cols[j]:
				matrix[i][j] = 0

	print(matrix)



	# print(rows)
	# print(cols)


# zeroMatrixBetter([[1, 1, 1], [1, 0, 1], [1, 1, 1]],3,3)


def zeroMatrixOptimal(matrix,n,m):
	col0 = 1
	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				matrix[i][0] = 0

				if j!=0:
					matrix[0][j] = 0
				else:
					col0 = 0


	for i in range(1, n):
		for j in range(1, m):
			if matrix[i][j] != 0:
				# check for col & row:
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0


	if matrix[0][0] == 0:
		for j in range(m):
			matrix[0][j] = 0
	if col0 == 0:
		for i in range(n):
			matrix[i][0] = 0

	return matrix

print(zeroMatrixOptimal([[2, 4, 3], [1, 0, 0]],2,3))