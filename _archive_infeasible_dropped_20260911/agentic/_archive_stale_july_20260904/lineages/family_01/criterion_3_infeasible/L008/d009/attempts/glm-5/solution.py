import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    deg = [0] * (n + 1)
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1
    
    adj_set = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj_set[u].add(v)
        adj_set[v].add(u)
    
    best = None
    
    for u, v in edges:
        if deg[u] > deg[v] or (deg[u] == deg[v] and u > v):
            u, v = v, u
        adj_set[u].add(v)
    
    for u in range(1, n + 1):
        neighbors = list(adj_set[u])
        ln = len(neighbors)
        for i in range(ln):
            x = neighbors[i]
            for j in range(i + 1, ln):
                y = neighbors[j]
                if x in adj_set[y]:
                    a, b, c = sorted([u, x, y])
                    if best is None or (a, b, c) < best:
                        best = (a, b, c)
    
    print(best[0], best[1], best[2])

solve()