import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n+1)]
    edges = set()
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
        edges.add((u, v) if u < v else (v, u))
    
    for a in range(1, n+1):
        neighbors_a = sorted([x for x in adj[a] if x > a])
        if len(neighbors_a) < 2:
            continue
        neighbor_set = set(neighbors_a)
        for b in neighbors_a:
            for c in adj[b]:
                if c > b and c in neighbor_set:
                    print(f"{a} {b} {c}")
                    return

solve()