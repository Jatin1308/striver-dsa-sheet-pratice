from typing import List


    



# def rotateMatrix(matrix: List[List[int]]) -> List[List[int]]:
#     n = len(matrix)
#     rotated = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             rotated[j][n - i - 1] = matrix[i][j]
#             print(rotated)
#     return rotated


def rotateMatrix(self,matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
    # def rotate(self,matrix: List[List[int]]) -> List[List[int]]:
    #     n = len(matrix)
    #     rotated = [[0 for _ in range(n)] for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             rotated[j][n - i - 1] = matrix[i][j]
    #     matrix =  rotated


rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])