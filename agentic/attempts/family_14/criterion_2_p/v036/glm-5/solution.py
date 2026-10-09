import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    research_centers = [int(next(it)) for _ in range(t)]
    is_research = [False] * (n + 1)
    for x in research_centers:
        is_research[x] = True
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    # Build virtual tree using Kruskal-like approach
    # Sort edges by weight
    edges = []
    for u in range(1, n + 1):
        for v, w in adj[u]:
            if u < v:
                edges.append((w, u, v))
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    research_count = [0] * (n + 1)
    for x in research_centers:
        research_count[x] = 1
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    total_cost = 0
    
    for w, u, v in edges:
        pu = find(u)
        pv = find(v)
        if pu != pv:
            # Union by rank
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            parent[pv] = pu
            research_count[pu] += research_count[pv]
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            
            # If this edge connects research centers to research centers
            if research_count[pu] == t:
                total_cost += w
                break
            elif research_count[pu] > 0:
                # This edge is needed if it connects research components
                total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()