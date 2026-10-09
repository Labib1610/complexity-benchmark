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
    
    for a in range(1, n + 1):
        neighbors_gt = sorted(x for x in adj[a] if x > a)
        k = len(neighbors_gt)
        for i in range(k):
            b = neighbors_gt[i]
            for j in range(i + 1, k):
                c = neighbors_gt[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

solve()