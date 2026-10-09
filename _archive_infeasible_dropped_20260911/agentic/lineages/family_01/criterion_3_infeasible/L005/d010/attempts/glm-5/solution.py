import sys

def solve():
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
    
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            for c in neighbors_a:
                if c > b and c in adj[b]:
                    print(f"{a} {b} {c}")
                    return
    
    # Should never reach here per problem guarantees
    print("-1 -1 -1")

solve()