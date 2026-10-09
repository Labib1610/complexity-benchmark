import sys
from collections import deque

def hopcroft_karp(n_left, adj, match_left, match_right):
    # returns matching size
    INF = float('inf')
    result = 0
    while True:
        # BFS to build layers
        dist = [INF] * (n_left + 1)  # for left vertices
        queue = deque()
        for u in range(1, n_left + 1):
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
        # DFS augmenting
        def dfs(u):
            for v in adj[u]:
                w = match_right[v]
                if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                    match_left[u] = v
                    match_right[v] = u
                    return True
            dist[u] = INF
            return False
        for u in range(1, n_left + 1):
            if match_left[u] == 0:
                dfs(u)
        result += 1  # hmm, this isn't right; need to count augmentations
    ...