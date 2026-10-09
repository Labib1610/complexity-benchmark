import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [None] * (n + 1)
    deg = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1
    
    for i in range(1, n + 1):
        adj[i] = [0] * deg[i]
    
    pos = [0] * (n + 1)
    for u, v in edges:
        adj[u][pos[u]] = v
        pos[u] += 1
        adj[v][pos[v]] = u
        pos[v] += 1
    
    for i in range(1, n + 1):
        adj[i].sort()
    
    best = None
    
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        
        adj_a = adj[a]
        deg_a = deg[a]
        
        if deg_a < 2:
            continue
        
        if best is not None:
            b_target = best[0]
            c_target = best[1]
            if deg_a >= 2 and adj_a[0] == b_target and adj_a[1] == c_target:
                best = (a, b_target, c_target)
                break
        
        for i in range(deg_a):
            b = adj_a[i]
            if best is not None and b >= best[1]:
                break
            
            adj_b = adj[b]
            deg_b = deg[b]
            
            j = i + 1
            k = 0
            while j < deg_a and k < deg_b:
                c_a = adj_a[j]
                c_b = adj_b[k]
                if c_a == c_b:
                    if best is None or (a, b, c_a) < best:
                        best = (a, b, c_a)
                    j += 1
                    k += 1
                elif c_a < c_b:
                    j += 1
                else:
                    k += 1
    
    print(f"{best[0]} {best[1]} {best[2]}")

solve()