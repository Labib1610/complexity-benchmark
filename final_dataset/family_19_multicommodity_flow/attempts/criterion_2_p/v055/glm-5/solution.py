import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    _ = int(next(it))  # asset type, not used
    s = int(next(it))
    t = int(next(it))
    d = int(next(it))
    
    edges_input = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        cap = int(next(it))
        edges_input.append((u, v, cap))
    
    # Build graph for max flow
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    def add_edge(u, v, cap):
        edges.append([v, cap, 0])
        edges.append([u, 0, 0])
        adj[u].append(len(edges) - 2)
        adj[v].append(len(edges) - 1)
    
    for u, v, cap in edges_input:
        add_edge(u, v, cap)
    
    # Dinic's algorithm
    level = [0] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        nonlocal level
        level = [0] * (n + 1)
        level[s] = 1
        q = deque([s])
        while q:
            u = q.popleft()
            for idx in adj[u]:
                v, cap, flow = edges[idx]
                if cap > flow and level[v] == 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] != 0
    
    def dfs(u, pushed):
        if pushed == 0:
            return 0
        if u == t:
            return pushed
        for i in range(ptr[u], len(adj[u])):
            ptr[u] = i
            idx = adj[u][i]
            v, cap, flow = edges[idx]
            if level[v] != level[u] + 1:
                continue
            tr = dfs(v, min(pushed, cap - flow))
            if tr == 0:
                continue
            edges[idx][2] += tr
            edges[idx ^ 1][2] -= tr
            return tr
        return 0
    
    total_flow = 0
    while bfs():
        ptr = [0] * (n + 1)
        while True:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed
            if total_flow == d:
                break
        if total_flow == d:
            break
    
    if total_flow < d:
        print("NO")
        return
    
    print("YES")
    result = []
    for i in range(m):
        idx = 2 * i
        result.append(str(edges[idx][2]))
    print(" ".join(result))

if __name__ == "__main__":
    solve()