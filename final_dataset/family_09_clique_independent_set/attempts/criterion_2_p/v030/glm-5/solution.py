INF = float('inf')  # or a large int

def hopcroft_karp(nL, nR, adj):
    matchL = [0]*(nL+1)  # 1-indexed, 0 = NIL
    matchR = [0]*(nR+1)
    dist = [0]*(nL+1)
    
    result = 0
    while True:
        # BFS
        queue = []
        for u in range(1, nL+1):
            if matchL[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        head = 0
        found_free = False
        while head < len(queue):
            u = queue[head]; head += 1
            if dist[u] < dist[0]:  # hmm, standard: if dist[u] < dist[NIL]
                for v in adj[u]:
                    w = matchR[v]
                    if dist[w] ...