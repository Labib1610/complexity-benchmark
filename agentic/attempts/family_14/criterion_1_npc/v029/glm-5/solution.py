import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    core = set()
    for _ in range(t):
        core.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u - 1, v - 1))
    
    if t <= 1:
        print(0)
        return
    
    # Kruskal's algorithm with modified union-find
    edges.sort()
    parent = list(range(n))
    rank = [0] * n
    core_count = [0] * n
    for i in range(n):
        if i + 1 in core:
            core_count[i] = 1
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    total_cost = 0
    edges_used = 0
    
    for w, u, v in edges:
        pu = find(u)
        pv = find(v)
        if pu != pv:
            # Union by rank
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            core_count[pu] += core_count[pv]
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            total_cost += w
            edges_used += 1
            if core_count[pu] == t:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solve()