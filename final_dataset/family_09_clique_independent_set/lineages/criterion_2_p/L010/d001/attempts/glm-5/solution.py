import sys
from collections import deque

def hopcroft_karp(n, adj, match_l, match_r):
    # returns matching size
    INF = float('inf')
    result = 0
    while True:
        # BFS: compute distances for left vertices
        dist = [INF] * (n+1)  # for left vertices
        queue = deque()
        for u in left vertices:
            if match_l[u] == 0:
                dist[u] = 0
                queue.append(u)
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = match_r[v]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        if not found:
            break
        # DFS: find augmenting paths
        ...