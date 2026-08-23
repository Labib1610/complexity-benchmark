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
        u = int(input_data[idx]); v = int(input_data[idx + 1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        adj_a = adj[a]
        if len(adj_a) < 2:
            continue
        sorted_a = sorted(adj_a)
        for i in range(len(sorted_a)):
            b = sorted_a[i]
            if b < a:
                continue
            adj_b = adj[b]
            for j in range(i + 1, len(sorted_a)):
                c = sorted_a[j]
                if c < b:
                    continue
                if c in adj_b:
                    print(a, b, c)
                    return

solve()