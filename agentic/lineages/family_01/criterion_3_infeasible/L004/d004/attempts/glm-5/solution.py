import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Find a triangle
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if adj[u][v]:
                for w in range(v + 1, n + 1):
                    if adj[u][w] and adj[v][w]:
                        print(u, v, w)
                        return
    
    # Find an independent set of size 3
    # Pick u with minimum degree
    u = 1
    for i in range(2, n + 1):
        if deg[i] < deg[u]:
            u = i
    
    # Find v not adjacent to u
    v = -1
    for i in range(1, n + 1):
        if i != u and not adj[u][i]:
            v = i
            break
    
    # Find w not adjacent to u and not adjacent to v
    w = -1
    for i in range(1, n + 1):
        if i != u and i != v and not adj[u][i] and not adj[v][i]:
            w = i
            break
    
    if u > v:
        u, v = v, u
    if u > w:
        u, w = w, u
    if v > w:
        v, w = w, v
    
    print(u, v, w)

solve()