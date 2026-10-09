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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # 2-color the graph to find bipartite partition L and R
    color = [-1] * (n + 1)
    L_nodes = []
    R_nodes = []
    
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            if color[u] == 0:
                L_nodes.append(u)
            else:
                R_nodes.append(u)
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)

    # Directed edges from L to R
    adj_L = [[] for _ in range(n + 1)]
    for u in L_nodes:
        adj_L[u] = adj[u]

    # Hopcroft-Karp algorithm for maximum bipartite matching
    match_L = [0] * (n + 1)
    match_R = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    def bfs():
        q = deque()
        for u in L_nodes:
            if match_L[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        
        found = False
        while q:
            u = q.popleft()
            for v in adj_L[u]:
                next_u = match_R[v]
                if next_u == 0:
                    found = True
                elif dist[next_u] == INF:
                    dist[next_u] = dist[u] + 1
                    q.append(next_u)
        return found

    def dfs(u):
        for v in adj_L[u]:
            next_u = match_R[v]
            if next_u == 0 or (dist[next_u] == dist[u] + 1 and dfs(next_u)):
                match_L[u] = v
                match_R[v] = u
                dist[u] = INF
                return True
        dist[u] = INF
        return False

    sys.setrecursionlimit(max(200000, n + 500))

    while bfs():
        for u in L_nodes:
            if match_L[u] == 0:
                dfs(u)

    # Reachability from unmatched vertices in L via alternating paths
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = deque()
    for u in L_nodes:
        if match_L[u] == 0:
            visited_L[u] = True
            q.append(u)

    while q:
        u = q.popleft()
        for v in adj_L[u]:
            if match_L[u] != v and not visited_R[v]:
                visited_R[v] = True
                matched_u = match_R[v]
                if matched_u != 0 and not visited_L[matched_u]:
                    visited_L[matched_u] = True
                    q.append(matched_u)

    # Maximum Independent Set = (L \cap visited_L) \cup (R \setminus visited_R)
    mis = []
    for u in L_nodes:
        if visited_L[u]:
            mis.append(u)
    for v in R_nodes:
        if not visited_R[v]:
            mis.append(v)

    if len(mis) >= k:
        print("YES")
        print(*(mis[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()