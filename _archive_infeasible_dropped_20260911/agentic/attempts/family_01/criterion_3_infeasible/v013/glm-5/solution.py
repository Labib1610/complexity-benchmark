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
        neighbors = sorted(x for x in adj[a] if x > a)
        na = adj[a]
        for i in range(len(neighbors)):
            b = neighbors[i]
            nb = adj[b]
            for j in range(i + 1, len(neighbors)):
                c = neighbors[j]
                if c in nb:
                    print(a, b, c)
                    return

solve()