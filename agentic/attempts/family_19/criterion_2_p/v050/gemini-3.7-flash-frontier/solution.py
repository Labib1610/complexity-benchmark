import sys
from collections import deque

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    _ = int(next(iterator))  # cargo category, always 1
    
    s = int(next(iterator))
    t = int(next(iterator))
    d = int(next(iterator))
    
    if s == t:
        if d == 0:
            print("YES")
            print(*(0 for _ in range(m)))
        else:
            print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    edges = []  # To store references to original edges
    
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        
        # forward edge: [to, cap, rev_idx, orig_cap]
        # backward edge: [to, cap, rev_idx, orig_cap]
        idx_u = len(adj[u])
        idx_v = len(adj[v])
        
        fwd = [v, c, idx_v, c]
        bwd = [u, 0, idx_u, 0]
        
        adj[u].append(fwd)
        adj[v].append(bwd)
        edges.append(fwd)
        
    level = [-1] * (n + 1)
    ptr = [0] * (n + 1)
    
    def bfs():
        for i in range(n + 1):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for edge in adj[v]:
                to, cap, _, _ = edge
                if cap > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        return level[t] != -1
    
    def dfs(v, pushed):
        if pushed == 0:
            return 0
        if v == t:
            return pushed
        for cid in range(ptr[v], len(adj[v])):
            ptr[v] = cid
            edge = adj[v][cid]
            to, cap, rev_idx, _ = edge
            if level[v] + 1 != level[to] or cap == 0:
                continue
            tr = dfs(to, min(pushed, cap))
            if tr == 0:
                continue
            edge[1] -= tr
            adj[to][rev_idx][1] += tr
            return tr
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
        ans = [fwd[3] - fwd[1] for fwd in edges]
        print(*(ans))

if __name__ == '__main__':
    solve()