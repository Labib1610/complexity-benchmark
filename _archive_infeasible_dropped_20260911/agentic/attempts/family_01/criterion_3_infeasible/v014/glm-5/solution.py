import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    best = None
    for a in range(1, n + 1):
        if best is not None and a >= best[0]:
            break
        adj_a = adj[a]
        for b in adj_a:
            if b <= a:
                continue
            if best is not None and b >= best[1]:
                continue
            for c in adj_a:
                if c <= b:
                    continue
                if best is not None and c >= best[2]:
                    continue
                if c in adj[b]:
                    best = (a, b, c)
                    break
    
    sys.stdout.write(f"{best[0]} {best[1]} {best[2]}\n")

solve()