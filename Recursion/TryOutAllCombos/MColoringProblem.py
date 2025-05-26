def mColoringProblem(n,m,edges):

    def isSafe(node, color, graph, n, col):
        for k in range(n):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
        return True

    def solve(node, col, m, n , graph):
        if node == n:
            return True

        for i in range(1, m + 1):
            if isSafe(node, color, graph, n, i):
                color[node] = i
                if solve(node + 1, color, m, n, graph):
                    return True
                color[node] = 0
        return False

    graph = [[0 for i in range(101)] for j in range(101)]
    color = [0 for _ in range(n)]
    # Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    graph[0][1] = 1
    graph[1][0] = 1
    graph[1][2] = 1
    graph[2][1] = 1
    graph[2][3] = 1
    graph[3][2] = 1
    graph[3][0] = 1
    graph[0][3] = 1
    graph[0][2] = 1
    graph[2][0] = 1

    return solve(0,color,m,n,graph)


print(mColoringProblem(4,3,[(0,1),(1,2),(2,3),(3,0),(0,2)]))

