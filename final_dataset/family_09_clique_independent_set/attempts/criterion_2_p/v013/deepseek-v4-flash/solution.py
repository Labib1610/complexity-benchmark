def bfs():
    from collections import deque
    q = deque()
    for u in range(nL):
        if pairU[u] == -1:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = INF
    dist[NIL] = INF
    while q:
        u = q.popleft()
        if dist[u] < dist[NIL]:
            for v in left_adj[u]:
                if pairV[v] == -1:
                    dist[NIL] = 0
                else:
                    if dist[pairV[v]] == INF:
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
    return dist[NIL] != INF