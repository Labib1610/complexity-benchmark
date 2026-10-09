import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # asset type indicator, not used
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    # Build level graph using BFS
    level = [-1] * (n + 1)
    q = deque([s])
    level[s] = 0
    while q:
        u = q.popleft()
        for v, idx in adj[u]:
            if level[v] == -1 and edges[idx][2] > 0:
                level[v] = level[u] + 1
                q.append(v)
    
    if level[t] == -1:
        print("NO")
        return
    
    # Find blocking flow using DFS
    flow = [0] * m
    ptr = [0] * (n + 1)
    
    def dfs(u, f):
        if u == t:
            return f
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            v, idx = adj[u][i]
            if level[v] == level[u] + 1 and edges[idx][2] > flow[idx]:
                pushed = dfs(v, min(f, edges[idx][2] - flow[idx]))
                if pushed > 0:
                    flow[idx] += pushed
                    return pushed
        return 0
    
    total_flow = 0
    while True:
        pushed = dfs(s, d - total_flow)
        if pushed == 0:
            break
        total_flow += pushed
        if total_flow == d:
            break
    
    if total_flow == d:
        print("YES")
        print(' '.join(map(str, flow)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()