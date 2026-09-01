import sys

def solve():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    m = int(data[ptr])
    ptr += 1
    
    adj = [set() for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        ptr += 2
        adj[u].add(v)
        adj[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    for i in range(1, n + 1):
        adj_list[i].sort()
    
    for u in range(1, n + 1):
        neighbors_u = [v for v in adj_list[u] if v > u]
        
        for i, v in enumerate(neighbors_u):
            for w in neighbors_u[i + 1:]:
                if w in adj[v]:
                    print(u, v, w)
                    return

solve()