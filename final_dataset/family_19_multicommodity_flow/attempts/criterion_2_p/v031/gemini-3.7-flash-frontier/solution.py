import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = next(iterator)  # the '1' in line 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        cap = int(next(iterator))
        
        # forward edge
        edges.append([v, cap, 0, len(adj[v])])
        adj[u].append(len(edges) - 1)
        
        # backward edge
        edges.append([u, 0, 0, len(adj[u]) - 1])
        adj[v].append(len(edges) - 1)

    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for edge_idx in adj[v]:
                to, cap, flow, _ = edges[edge_idx]
                if cap - flow > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] != -1

    def dfs(v, pushed):
        if pushed == 0 or v == t:
            return pushed
        for cid in range(ptr[v], len(adj[v])):
            ptr[v] = cid
            edge_idx = adj[v][cid]
            to, cap, flow, rev_idx = edges[edge_idx]
            tr = cap - flow
            if level[v] + 1 != level[to] or tr == 0:
                continue
            tr = min(pushed, tr)
            push = dfs(to, tr)
            if push == 0:
                continue
            edges[edge_idx][2] += push
            edges[adj[to][rev_idx]][2] -= push
            return push
        return 0

    total_flow = 0
    while total_flow < d and bfs():
        for i in range(n + 1):
            ptr[i] = 0
        while total_flow < d:
            pushed = dfs(s, d - total_flow)
            if pushed == 0:
                break
            total_flow += pushed

    if total_flow < d:
        print("NO")
    else:
        print("YES")
        ans = []
        for i in range(m):
            ans.append(edges[2 * i][2])
        print(*(ans))

if __name__ == '__main__':
    solve()