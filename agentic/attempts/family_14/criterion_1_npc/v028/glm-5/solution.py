import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    focal = set()
    for _ in range(t):
        focal.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    total_cost = 0
    edges_used = 0
    
    for w, u, v in edges:
        if union(u, v):
            total_cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solve()