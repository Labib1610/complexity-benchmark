import sys
from collections import deque

def hopcroft_karp(n, adj):
    # n = number of left nodes (1-indexed), right nodes also 1..n
    INF = float('inf')
    match_l = [0]*(n+1)  # 0 = unmatched (NIL)
    match_r = [0]*(n+1)
    dist = [0]*(n+1)
    
    def bfs():
        queue = deque()
        for u in range(1, n+1):
            if match_l[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
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
        return found
    
    def dfs(u):
        for v in adj[u]:
            w = match_r[v]
            if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                match_l[u] = v
                match_r[v] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, n+1):
            if match_l[u] == 0:
                if dfs(u):
                    matching += 1
    return matching, match_l