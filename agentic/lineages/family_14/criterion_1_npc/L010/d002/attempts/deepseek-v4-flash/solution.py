import sys
import heapq

def min_cost_to_connect_terminals(n, m, t, terminals, edges):
    if t <= 1:
        return 0
    
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, w in edges:
        u -= 1
        v -= 1
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    terminals = [x-1 for x in terminals]
    k = len(terminals)
    
    dp = [[math.inf] * (1 << k) for _ in range(k)]
    for i in range(k):
        dp[i][1 << i] = 0
    
    for mask in range(1 << k):
        for i in range(k):
            if not (mask & (1 << i)):
                continue
            if dp[i][mask] == math.inf:
                continue
            for j in range(k):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                new_cost = dp[i][mask] + dist[terminals[i]][terminals[j]]
                if new_cost < dp[j][new_mask]:
                    dp[j][new_mask] = new_cost
    
    full_mask = (1 << k) - 1
    ans = min(dp[i][full_mask] for i in range(k))
    
    # Now try Steiner tree-like approach: pick a center set of non-terminal nodes
    # For n <= 100, we can also enumerate all possible Steiner nodes subset (but too big)
    # This is a metric TSP approach, but since the terminals need to be connected not necessarily as a cycle,
    # the minimal tree is the MST over the terminal distance matrix.
    # Use Prim's MST on terminals
    min_mst = 0
    visited = [False] * k
    visited[0] = True
    edges_mst = []
    for _ in range(k-1):
        best = math.inf
        u = -1
        v = -1
        for i in range(k):
            if visited[i]:
                for j in range(k):
                    if not visited[j]:
                        if dist[terminals[i]][terminals[j]] < best:
                            best = dist[terminals[i]][terminals[j]]
                            u, v = i, j
        visited[v] = True
        min_mst_temp = 0
        # Actually MST on complete graph with terminal distances
        # above is Prim's algorithm
        # We'll compute properly below outside loop
        pass
    
    # Prim's MST
    visited = [False] * k
    min_dist = [math.inf] * k
    min_dist[0] = 0
    mst_cost = 0
    for _ in range(k):
        u = -1
        best = math.inf
        for i in range(k):
            if not visited[i] and min_dist[i] < best:
                best = min_dist[i]
                u = i
        visited[u] = True
        mst_cost += best
        for v in range(k):
            if not visited[v] and dist[terminals[u]][terminals[v]] < min_dist[v]:
                min_dist[v] = dist[terminals[u]][terminals[v]]
    
    return mst_cost

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    terminals = [int(next(it)) for _ in range(t)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    result = min_cost_to_connect_terminals(n, m, t, terminals, edges)
    print(result)

if __name__ == "__main__":
    solve()