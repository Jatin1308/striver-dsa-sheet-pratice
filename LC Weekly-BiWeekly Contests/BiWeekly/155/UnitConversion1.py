"""
    here we are given the graph type structure where nodes are represented 0 - n-1
    and root node is 0, and distance b/w each node which are connected is given
    so answer is the array of numbers where each arr[i] represents the cost of reaching that node
    from 0. multiplying each edge weight with each other while traversing
"""

'''
    so here traversal is required -> GRAPH/TREE BASED PROGRAM, here these are directed edges in this ques
    best we can follow is BFS - breadth first search
    
    C++
    ````
    
    we could have -> vector<vector<pair<int,int>>> adj
    adj[1].pushback({2,3}) -> ~~~~~[1 = source node, 2 = target node, 3 = edge weight]~~~~~
    
    
    Python
    ``````
    g ={}
    and g can look like: {'A':[('B',2),('C',5)]}
    here -> "key": source node
            "value" -> List of tuples -> tuple contains ("targetNode","edgeWeight")
            
'''

from typing import List
from collections import deque
MOD = 10**9+7
def solveUnitConversion(conversions: List[List[int]]):
    n = len(conversions)+1
    adj = [[] for _ in range(n)]

    for source,target,factor in conversions:
        adj[source].append((target,factor))


    print(adj)

    baseUnitConversionResult = [0]*n
    baseUnitConversionResult[0] = 1

    visited = [False]*n

    q = deque([0])
    visited[0] = True

    while q:
        u = q.popleft()
        for v, factor in adj[u]:
            if not visited[v]:
                baseUnitConversionResult[v]  = (baseUnitConversionResult[u]*factor)%MOD
                visited[v] = True
                q.append(v)

    return baseUnitConversionResult

    # while q[0] is not None:
    #     frontEle = q[0]
    #     q.pop()
    #
    #     for [a,b] in adj[frontEle]:
    #         print([a,b])
    #         if val[a] == -1:
    #             val[a] = val[frontEle]*b
    #             q.append(a)
    # return val






print(solveUnitConversion([[0,1,2],[1,2,3]]))



