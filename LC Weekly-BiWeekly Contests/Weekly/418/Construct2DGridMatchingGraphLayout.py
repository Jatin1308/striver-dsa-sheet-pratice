from collections import defaultdict,deque

def construct_grid(edges):

# build graph - adjacency list
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

# find grid size
    n = len(graph)  # number of nodes is the length of edges
    size = int(n**0.5) # size of the grid assuming the square grip


# create a grid initialized with -1
    grid = [[-1] * size for _ in range(size)]
    print("grid: ",grid)

# dfs to fill the grid

    def dfs(node,r,c):

        
        if r<0 or r>=size or c<0 or c>=size or grid[r][c] != -1: # out of bound condition check
            return False
        
        grid[r][c] = node  # place the node in the grid

        for neighbor in graph[node]:
            if dfs(neighbor,r+1,c) or dfs(neighbor,r,c+1):
                continue
        return True
    
    dfs(0,0,0)

    result = [cell for row in grid for cell in row if cell != -1]

    return result


edges = [[0,1],[1,3],[2,3],[2,4]]

print("Final Ans: ",construct_grid(edges))