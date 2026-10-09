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
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    for v in range(1, n + 1):
        neighbors = sorted(x for x in adj[v] if x > v)
        for i in range(len(neighbors)):
            u = neighbors[i]
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                if w in adj[u]:
                    print(f"{v} {u} {w}")
                    return
    
solve()