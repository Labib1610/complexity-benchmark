import sys
sys.setrecursionlimit(300000)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

def main():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    catalysts = [int(next(it)) - 1 for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((w, u, v))
    
    # Build MST using Kruskal
    edges.sort()
    dsu = DSU(n)
    mst_edges = []
    for w, u, v in edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
    
    # Build adjacency for MST
    adj = [[] for _ in range(n)]
    for idx, (u, v, w) in enumerate(mst_edges):
        adj[u].append((v, w, idx))
        adj[v].append((u, w, idx))
    
    # Mark catalyst nodes
    is_catalyst = [False] * n
    for c in catalysts:
        is_catalyst[c] = True
    
    # DFS to find for each edge the minimum weight on path between terminals
    # We'll do a multi-source BFS/DFS from each catalyst to find min edge on path to another catalyst
    # Simpler: For each catalyst, run DFS to find min edge to any other catalyst, mark that edge for removal.
    # But we need global min cut: we can use the fact that in MST, the min edge on path between any two terminals must be cut.
    # We can find all such edges by processing MST edges in decreasing weight and using DSU to connect components.
    
    # Sort MST edges by weight descending
    mst_edges_sorted = sorted(mst_edges, key=lambda x: -x[2])
    dsu2 = DSU(n)
    cut_edges = []
    total_cost = 0
    
    # Initially each catalyst is its own component
    # We'll process edges from largest to smallest, union components.
    # If an edge connects two components that both contain catalysts, we must cut it.
    comp_has_catalyst = [is_catalyst[i] for i in range(n)]
    
    for u, v, w in mst_edges_sorted:
        ru, rv = dsu2.find(u), dsu2.find(v)
        if ru == rv:
            continue
        if comp_has_catalyst[ru] and comp_has_catalyst[rv]:
            # This edge must be cut
            cut_edges.append((u, v))
            total_cost += w
        else:
            # Union
            new_has = comp_has_catalyst[ru] or comp_has_catalyst[rv]
            dsu2.parent[ru] = rv
            comp_has_catalyst[rv] = new_has
    
    if total_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u+1, v+1)
    else:
        print("NO")

if __name__ == "__main__":
    main()