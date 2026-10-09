import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges for deterministic processing
    edges.sort()
    
    best = None
    marked = [0] * (n + 1)
    stamp = 0
    
    for u, v in edges:
        # Find smallest common neighbor w
        # Mark neighbors of u (only those > max(u,v) won't help for lex order,
        # but we need all common neighbors)
        stamp += 1
        for w in adj[u]:
            marked[w] = stamp
        
        for w in adj[v]:
            if marked[w] == stamp:
                # Found triangle (u, v, w)
                a, b, c = sorted([u, v, w])
                if best is None or (a, b, c) < best:
                    best = (a, b, c)
                    # Can't break early - need lex smallest overall
    
    print(best[0], best[1], best[2])

main()