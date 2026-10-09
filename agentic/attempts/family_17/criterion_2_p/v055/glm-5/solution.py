import sys
from collections import deque

def hopcroft_karp(n, m, edges):
    # n = number of left vertices (modules), m = right (ports)
    # adjacency: adj[u] = list of v
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
    
    # match_left[u] = matched v or 0 (1-indexed right vertices)
    # match_right[v] = matched u or 0
    match_left = [0] * (n + 1)
    match_right = [0] * (m + 1)
    
    INF = float('inf')
    
    result = 0
    while True:
        # BFS
        dist = [INF] * (n + 1)
        queue = deque()
        for u in range(1, n + 1):
            if match_left[u] == 0:
                dist[u] = 0
                queue.append(u)
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                w = match_right[v]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        if not found:
            break
        
        # DFS
        def dfs(u):
            for v in adj[u]:
                w = match_right[v]
                if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                    match_left[u] = v
                    match_right[v] = u
                    return True
            dist[u] = INF
            return False
        
        for u in range(1, n + 1):
            if match_left[u] == 0:
                if dfs(u):
                    result += 1
    ...