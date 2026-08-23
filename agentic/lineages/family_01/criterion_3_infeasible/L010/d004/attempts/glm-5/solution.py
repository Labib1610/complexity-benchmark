import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        neighbors_a = sorted(adj[a])
        # Filter neighbors > a
        neighbors_a = [x for x in neighbors_a if x > a]
        len_na = len(neighbors_a)
        for i in range(len_na):
            b = neighbors_a[i]
            adj_b = adj[b]
            for j in range(i + 1, len_na):
                c = neighbors_a[j]
                if c in adj_b:
                    print(f"{a} {b} {c}")
                    return

solve()