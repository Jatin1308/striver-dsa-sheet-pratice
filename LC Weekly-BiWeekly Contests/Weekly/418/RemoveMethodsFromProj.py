


from collections import defaultdict, deque

def remainingMethods(n,k,invocations):
    # build graoh G and reverse G_reverse
    G = defaultdict(list)
    G_reverse = defaultdict(list)
    # print(invocations)
    for a,b in invocations:
        G[a].append(b)
        G_reverse[b].append(a)
    # print(G)
    # print(G_reverse)
        # print("~~~~~~~~")

    # find all methods reachable from method k (suspicious methods)
    def find_suspicious_methods(start):
        suspicious = set()
        queue = deque([start])
        # print("generated dequeue: ",queue)
        while queue:
            method = queue.popleft()
            # print("Popped method: ",method)
            if method not in suspicious:
                suspicious.add(method)
                # print("Suspicious method list: ",suspicious)
                for neighbor in G[method]:
                    queue.append(neighbor)
                    # print("Queue after appending: ",queue," from G[method]: ",G[method]," and neighbour: ",neighbor)
        return suspicious
    suspicious_methods = find_suspicious_methods(k)


    # check for external invocations
    for method in suspicious_methods:
        for invoker in G_reverse[method]:
            if invoker not in suspicious_methods:
                return list(range(n))
    # return the remaining methods
    return [i for i in range(n) if i not in suspicious_methods]

n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]

print(remainingMethods(n,k,invocations))