import sys
from bisect import insort

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
        deg[u] += 1
        deg[v] += 1
    
    # Build directed edges: low-degree -> high-degree (tie-break by vertex id)
    out_adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        du = deg[u]
        for v in adj[u]:
            dv = deg[v]
            if du < dv or (du == dv and u < v):
                out_adj[u].append(v)
    
    for u in range(1, n + 1):
        out_adj[u].sort()
    
    best = None
    best_a = n + 1
    
    for a in range(1, n + 1):
        if a >= best_a:
            break
        out_a = out_adj[a]
        la = len(out_a)
        # Check all pairs in out_a
        for i in range(la):
            b = out_a[i]
            if best is not None and a == best_a and b >= best[1]:
                continue
            adj_b = adj[b]
            # Find smallest c in out_a[i+1:] that's also in adj_b
            for j in range(i + 1, la):
                c = out_a[j]
                if c in adj_b:
                    if best is None or a < best_a or (a == best_a and (b < best[1] or (b == best[1] and c < best[2]))):
                        best = (a, b, c)
                        best_a = a
                    break
    
    print(best[0], best[1], best[2])

main()