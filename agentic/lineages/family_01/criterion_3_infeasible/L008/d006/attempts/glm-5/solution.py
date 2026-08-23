import sys
from sys import stdin

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
    
    # Try to find triangle with minimum (a, b, c) lexicographically
    for a in range(1, n + 1):
        neighbors_a = sorted(x for x in adj[a] if x > a)
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

solve()