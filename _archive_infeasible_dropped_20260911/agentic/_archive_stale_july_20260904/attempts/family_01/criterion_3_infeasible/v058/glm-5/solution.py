import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    for a in range(1, n + 1):
        if best is not None and best[0] < a:
            break
        neighbors = adj[a]
        if len(neighbors) < 2:
            continue
        sorted_neighbors = sorted(neighbors)
        # We need b, c in neighbors with b < c and c in adj[b]
        # Since a < b < c, and we want lexicographically smallest (a, b, c)
        for i in range(len(sorted_neighbors)):
            b = sorted_neighbors[i]
            if best is not None and best[1] < b:
                break
            adj_b = adj[b]
            for j in range(i + 1, len(sorted_neighbors)):
                c = sorted_neighbors[j]
                if c in adj_b:
                    best = (a, b, c)
                    break
            if best is not None and best[0] == a and best[1] == b:
                break
        if best is not None and best[0] == a:
            break
    
    if best is not None:
        sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()