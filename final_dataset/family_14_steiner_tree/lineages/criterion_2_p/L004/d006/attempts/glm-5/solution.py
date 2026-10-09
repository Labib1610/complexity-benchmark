import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(data[idx]) - 1)
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((w, u, v))
    
    edges.sort()
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    total_cost = 0
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if ru in critical and rv in critical:
            total_cost += w
            union(u, v)
        else:
            union(u, v)
    
    print(total_cost)

solve()