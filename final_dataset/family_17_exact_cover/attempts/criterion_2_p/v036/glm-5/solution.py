import sys
from collections import deque

def hopcroft_karp(n, adj, match_l, match_r):
    # adj: list of lists for left vertices (0-indexed)
    INF = float('inf')
    result = 0
    # match_l[i] = matched right vertex or -1
    # match_r[j] = matched left vertex or -1
    dist = [0] * n
    
    def bfs():
        queue = deque()
        for u in range(n):
            if match_l[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = match_r[v]
                if w == -1:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        return found
    
    def dfs(u):
        for v in adj[u]:
            w = match_r[v]
            if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
                match_l[u] = v
                match_r[v] = u
                return True
        dist[u] = INF
        return False
    
    while bfs():
        for u in range(n):
            if match_l[u] == -1:
                if dfs(u):
                    result += 1
    return result