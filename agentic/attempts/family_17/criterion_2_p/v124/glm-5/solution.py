import sys
from collections import deque

def hopcroft_karp(n_left, n_right, adj):
    # match_left[u] = matched right vertex or -1
    # match_right[v] = matched left vertex or -1
    INF = float('inf')
    match_left = [-1] * n_left
    match_right = [-1] * n_right
    dist = [0] * n_left
    
    def bfs():
        queue = deque()
        for u in range(n_left):
            if match_left[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = match_right[v]
                if w == -1:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        return found
    
    def dfs(u):
        for v in adj[u]:
            w = match_right[v]
            if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
                match_left[u] = v
                match_right[v] = u
                return True
        dist[u] = INF
        return False
    
    ...