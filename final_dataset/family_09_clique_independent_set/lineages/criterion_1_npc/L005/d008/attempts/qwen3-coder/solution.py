from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Store edges as a set of frozensets for fast lookup
    edges = set()
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        edge = frozenset([u, v])
        edges.add(edge)
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all combinations of k nodes
    for combo in combinations(range(1, n + 1), k):
        selected = set(combo)
        
        total_ref_count = 0
        boundary_size = 0
        
        # For each selected node, count its references
        for node in selected:
            ref_count = 0
            for neighbor in adj[node]:
                if frozenset([node, neighbor]) in edges:
                    ref_count += 1
            total_ref_count += ref_count
        
        # Count boundary size: edges where exactly one endpoint is selected
        for edge in edges:
            edge_list = list(edge)
            u, v = edge_list[0], edge_list[1]
            if (u in selected) != (v in selected):  # Exactly one is selected
                boundary_size += 1
        
        if total_ref_count == boundary_size:
            print("YES")
            print(*combo)
            return
    
    print("NO")

solve()