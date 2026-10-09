import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    
    for a in range(1, n + 1):
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        sorted_a = sorted(adj_a)
        len_a = len(sorted_a)
        for i in range(len_a):
            b = sorted_a[i]
            if best is not None and b >= best[1]:
                break
            adj_b = adj[b]
            for j in range(i + 1, len_a):
                c = sorted_a[j]
                if best is not None and c >= best[2]:
                    break
                if c in adj_b:
                    best = (a, b, c)
                    break
            if best is not None and best[0] == a and best[1] == b:
                break
        if best is not None and best[0] == a:
            break
    
    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}")

solve()