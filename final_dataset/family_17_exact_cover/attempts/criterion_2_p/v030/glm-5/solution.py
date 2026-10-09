INF = float('inf') or a large number
queue = deque of free left vertices
dist = [INF]*q
for u free: dist[u]=0, queue.append(u)
while queue:
    u = queue.popleft()
    for v in adj[u]:
        u2 = pair_v[v]
        if u2 == -1: found free right vertex -> record shortest augmenting path length
        elif dist[u2] == INF: dist[u2] = dist[u]+1; queue.append(u2)