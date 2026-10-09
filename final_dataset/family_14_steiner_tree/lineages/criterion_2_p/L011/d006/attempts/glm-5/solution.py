import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1
    
    mandatory = [False] * (n + 1)
    for _ in range(t):
        a = int(data[idx]); idx += 1
        mandatory[a] = True
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
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
    
    edges.sort(key=lambda e: e[2])
    
    total = 0
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if mandatory[ru] and mandatory[rv]:
            total += w
            union(ru, rv)
        else:
            union(ru, rv)
    
    print(total)

solve()