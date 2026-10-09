import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    terminals = set()
    for _ in range(t):
        terminals.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u - 1, v - 1))
    
    # If t <= 1, no edges needed
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    parent = list(range(n))
    rank = [0] * n
    comp_count = [1] * n  # number of terminals in component
    for i in range(n):
        if i + 1 in terminals:
            comp_count[i] = 1
        else:
            comp_count[i] = 0
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
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
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            # Merge terminal counts
            comp_count[pu] += comp_count[pv]
            total_cost += w
            edges_used += 1
            if comp_count[pu] == t:
                break
    
    print(total_cost)

if __name__ == "__main__":
    solve()