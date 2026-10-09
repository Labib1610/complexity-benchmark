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
    
    # Find lexicographically smallest triangle
    # Iterate x1 from 1 to n, then x2 from x1+1, check if x2 is neighbor of x1
    # then for each x3 > x2 that is neighbor of both x1 and x2
    for x1 in range(1, n + 1):
        neighbors_x1 = sorted(v for v in adj[x1] if v > x1)
        neighbor_set_x1 = adj[x1]
        for i in range(len(neighbors_x1)):
            x2 = neighbors_x1[i]
            for j in range(i + 1, len(neighbors_x1)):
                x3 = neighbors_x1[j]
                if x3 in adj[x2]:
                    print(f"{x1} {x2} {x3}")
                    return

solve()