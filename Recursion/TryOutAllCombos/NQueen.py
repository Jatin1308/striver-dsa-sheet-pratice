def nQueen(n):

    def isSafe(row,col,boardRow):
        # check upper element
        duprow = row
        dupcol = col

        while row >= 0 and col >= 0:
            if boardRow[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        col = dupcol
        row = duprow
        while col >= 0:
            if boardRow[row][col] == 'Q':
                return False
            col -= 1
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if boardRow[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        return True

    def solve(col,boardRow,numberOfQueens):
        if col == numberOfQueens:
            finalRes.append(list(board))
            return
        for row in range(0,numberOfQueens):
            if isSafe(row,col,boardRow):
                board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                solve(col + 1, board, numberOfQueens)
                board[row] = board[row][:col] + '.' + board[row][col + 1:]

    board = ['.'*n for _ in range(n)]
    finalRes = []
    solve(0,board,n)
    return finalRes


print(nQueen(4))