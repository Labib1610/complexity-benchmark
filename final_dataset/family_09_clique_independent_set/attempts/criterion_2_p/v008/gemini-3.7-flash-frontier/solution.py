import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # 1. 2-color the graph to find bipartition (L and R)
    color = [-1] * (n + 1)
    L = []
    R = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            L.append(i)
            queue = deque([i])
            while queue:
                u = queue.popleft()
                c = color[u]
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - c
                        if color[v] == 0:
                            L.append(v)
                        else:
                            R.append(v)
                        queue.append(v)

    # 2. Hopcroft-Karp Algorithm for Maximum Bipartite Matching
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = float('inf')

    def bfs():
        q = deque()
        for u in L:
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    sys.setrecursionlimit(200000)
    
    matching = 0
    while bfs():
        for u in L:
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    # 3. Find Maximum Independent Set via König's theorem
    # In bipartite graph:
    # Reachable from unmatched vertices in L via alternating paths (L -> R via non-matching, R -> L via matching)
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = deque()
    for u in L:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v != pair_u[u] and not visited_R[v]:
                visited_R[v] = True
                matched_u = pair_v[v]
                if matched_u != 0 and not visited_L[matched_u]:
                    visited_L[matched_u] = True
                    q.append(matched_u)

    # Independent Set = (L that are visited) union (R that are NOT visited)
    independent_set = []
    for u in L:
        if visited_L[u]:
            independent_set.append(u)
    for v in R:
        if not visited_R[v]:
            independent_set.append(v)

    if len(independent_set) >= k:
        print("YES")
        print(*(independent_set[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()