import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

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
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    # 2-color the graph
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = [i]
            for u in q:
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        q.append(v)

    # Hopcroft-Karp bipartite matching
    # L: color == 0, R: color == 1
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    def bfs():
        q = []
        for u in range(1, n + 1):
            if color[u] == 0:
                if pair_u[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = INF
        dist[0] = INF
        
        for u in q:
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    while bfs():
        for u in range(1, n + 1):
            if color[u] == 0 and pair_u[u] == 0:
                dfs(u)

    # Find reachable vertices in alternating paths from unmatched L
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = []
    for u in range(1, n + 1):
        if color[u] == 0 and pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    for u in q:
        for v in adj[u]:
            if not visited_R[v] and pair_u[u] != v:
                visited_R[v] = True
                pu = pair_v[v]
                if pu != 0 and not visited_L[pu]:
                    visited_L[pu] = True
                    q.append(pu)

    # Maximum independent set: (L and visited) union (R and not visited)
    mis = []
    for i in range(1, n + 1):
        if color[i] == 0:
            if visited_L[i]:
                mis.append(i)
        else:
            if not visited_R[i]:
                mis.append(i)
                
    if len(mis) >= k:
        print("YES")
        print(*(mis[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()