import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    critical = [int(next(it)) - 1 for _ in range(t)]
    is_critical = [False] * n
    for v in critical:
        is_critical[v] = True
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
    
    parent = list(range(n))
    rank = [0] * n
    critical_count = [1 if is_critical[i] else 0 for i in range(n)]
    
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
            rx, ry = ry, rx
        parent[ry] = rx
        critical_count[rx] += critical_count[ry]
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    edges.sort(key=lambda e: e[2])
    
    total_cost = 0
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        if critical_count[ru] > 0 and critical_count[rv] > 0:
            total_cost += w
        union(u, v)
    
    print(total_cost)

if __name__ == "__main__":
    solve()