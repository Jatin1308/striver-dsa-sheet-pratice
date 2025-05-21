def wordSearch(grid,word):
    # row count
    ROWS = len(grid)
    # column count
    COLS = len(grid[0])
    path = set() # for checking no revisiting

    def exist(r,c,i):
        if i == len(word):
            return True

        # checking for invalid pos, if currChar!=gridChar or if its the same path we are revisiting
        if r<0 or c<0 or r>=ROWS or c >= COLS or word[i] != grid[r][c] or (r,c) in path:
            return False

        # the curr character is same as character in grid that's why we moved forward
        path.add((r,c))
        res = exist(r+1,c,i+1) or exist(r-1,c,i+1) or exist(r,c+1,i+1) or exist(r,c-1,i+1)
        path.remove((r,c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if exist(r,c,0):
                return True
    return False

print(wordSearch([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))