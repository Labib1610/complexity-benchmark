INF = float('inf')
pairU = [-1]*(nU)  # matched to which R
pairV = [-1]*(nV)
dist = [0]*nU

def bfs():
    queue = deque()
    for u in range(nU):
        if pairU[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = INF
    found = False
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            w = pairV[v]
            if w == -1:
                found = True
            elif dist[w] == INF:
                dist[w] = dist[u]+1
                queue.append(w)
    return found

def dfs(u):
    stack = ...
    for v in adj[u]:
        w = pairV[v]
        if w == -1 or (dist[w] == dist[u]+1 and dfs(w)):
            pairU[u] = v
            pairV[v] = u
            return True
    dist[u] = INF
    return False