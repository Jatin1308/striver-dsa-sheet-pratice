def ratInAMaze(grid):
    n = len(grid)
    res = []
    visited = set()
    def solve(r,c,curr):
        print(r,c)
        if r == n-1 and c == n-1:
            print("got the answer")
            res.append("".join(list(curr)))
            return

        if  r+1<n and (r+1,c) not in visited and grid[r+1][c] == 1:
            curr.append("D")
            visited.add((r+1,c))
            solve(r+1,c,curr)
            curr.pop()
            visited.remove((r + 1, c))

        if c-1 > -1 and (r,c-1) not in visited and grid[r][c-1] == 1:
            visited.add((r,c-1))
            curr.append("L")
            solve(r,c-1,curr)
            curr.pop()
            visited.remove((r, c - 1))

        if c+1 < n and (r,c+1) not in visited and grid[r][c+1] == 1:
            visited.add((r,c+1))
            curr.append("R")
            solve(r,c+1,curr)
            curr.pop()
            visited.remove((r,c+1))

        if r-1 >-1 and (r-1,c) not in visited and grid[r-1][c] == 1:
            visited.add((r-1,c))
            curr.append("U")
            solve(r-1,c,curr)
            curr.pop()
            visited.remove((r-1,c))


    solve(0,0,[])
    return res if len(res) != 0 else -1

print(ratInAMaze([ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]))