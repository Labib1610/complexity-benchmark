import sys

# Increase recursion depth just in case, but iterative is preferred
sys.setrecursionlimit(300000)

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
        
    # Step 1: 2-color the graph into bipartite sets L (color 0) and R (color 1)
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            queue = [i]
            for u in queue:
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        queue.append(v)
                        
    # Directed bipartite graph: only keep edges from L (color 0) to R (color 1)
    # Hopcroft-Karp algorithm
    pair_u = [0] * (n + 1)  # pair for u in L
    pair_v = [0] * (n + 1)  # pair for v in R
    dist = [0] * (n + 1)
    INF = 10**9
    
    # Pre-filter adjacency for L vertices to only point to R
    adj_L = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        if color[u] == 0:
            adj_L[u] = adj[u]

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
        
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            if dist[u] < dist[0]:
                for v in adj_L[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj_L[u]:
                pu = pair_v[v]
                if dist[pu] == dist[u] + 1:
                    if dfs(pu):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if color[u] == 0 and pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    # Find reachable vertices in alternating graph to get Konig's min vertex cover
    # Start BFS from all unmatched vertices in L
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    q = []
    
    for u in range(1, n + 1):
        if color[u] == 0 and pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v in adj_L[u]:
            if not visited_R[v] and v != pair_u[u]:
                visited_R[v] = True
                matched_l = pair_v[v]
                if matched_l != 0 and not visited_L[matched_l]:
                    visited_L[matched_l] = True
                    q.append(matched_l)

    # Maximum Independent Set:
    # L_in_MIS = {u in L | visited_L[u]}
    # R_in_MIS = {v in R | not visited_R[v]}
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