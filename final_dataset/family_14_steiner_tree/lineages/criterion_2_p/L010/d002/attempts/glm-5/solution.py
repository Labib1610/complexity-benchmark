import sys
from sys import setrecursionlimit

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    terminals = set()
    for _ in range(t):
        terminals.add(int(data[idx])); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    setrecursionlimit(1 << 25)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    parent_edge = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    
    root = next(iter(terminals))
    stack = [(root, 0, 0, 0)]
    visited[root] = True
    
    while stack:
        u, p, d, pe = stack.pop()
        parent[u] = p
        depth[u] = d
        parent_edge[u] = pe
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, u, d + 1, w))
    
    LOG = max(1, (n).bit_length())
    up = [[0] * (n + 1) for _ in range(LOG)]
    up[0] = parent[:]
    for j in range(1, LOG):
        up_j = up[j]
        up_j_1 = up[j - 1]
        for v in range(1, n + 1):
            up_j[v] = up_j_1[up_j_1[v]]
    
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        j = 0
        while diff:
            if diff & 1:
                u = up[j][u]
            diff >>= 1
            j += 1
        if u == v:
            return u
        for j in range(LOG - 1, -1, -1):
            if up[j][u] != up[j][v]:
                u = up[j][u]
                v = up[j][v]
        return parent[u]
    
    marked = [False] * (n + 1)
    for x in terminals:
        marked[x] = True
    
    for u in order:
        if u == root:
            continue
        p = parent[u]
        if marked[u]:
            marked[p] = True
    
    total = 0
    for u in order:
        if u == root:
            continue
        if marked[u]:
            total += parent_edge[u]
    
    print(total)

main()