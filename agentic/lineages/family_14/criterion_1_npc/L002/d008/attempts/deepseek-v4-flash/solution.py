import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    target = set()
    for _ in range(t):
        target.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((w, u, v))
    
    # If t == 1 or n-t == 1, that side needs no edges
    # We need MST for target set and non-target set separately.
    
    # Helper: MST cost for a given set of nodes
    def mst_cost(nodes):
        nodes = list(nodes)
        if len(nodes) <= 1:
            return 0
        node_set = set(nodes)
        # Kruskal
        parent = {x: x for x in nodes}
        rank = {x: 0 for x in nodes}
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True
        
        cost = 0
        used = 0
        for w, u, v in sorted(edges):
            if u in node_set and v in node_set:
                if union(u, v):
                    cost += w
                    used += 1
                    if used == len(nodes) - 1:
                        break
        if used != len(nodes) - 1:
            return float('inf')
        return cost
    
    target_nodes = list(target)
    non_target_nodes = [x for x in range(1, n+1) if x not in target]
    
    cost1 = mst_cost(target_nodes)
    cost2 = mst_cost(non_target_nodes)
    
    print(cost1 + cost2)

if __name__ == "__main__":
    solve()