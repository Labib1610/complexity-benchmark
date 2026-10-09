import sys

def solve():
    input = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(input[ptr]); ptr += 1
    E = int(input[ptr]); ptr += 1
    F = int(input[ptr]); ptr += 1
    
    targets = [int(input[ptr + i]) for i in range(F)]
    ptr += F
    
    edges = []
    for _ in range(E):
        u = int(input[ptr]); ptr += 1
        v = int(input[ptr]); ptr += 1
        w = int(input[ptr]); ptr += 1
        edges.append((w, u, v))
    
    if F <= 1:
        print(0)
        return
    
    # Kruskal's algorithm with DSU
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    
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
    
    # Sort edges by weight
    edges.sort()
    
    # Mark target registers
    is_target = [False] * (N + 1)
    for t in targets:
        is_target[t] = True
    
    total_cost = 0
    components_with_targets = F
    
    for w, u, v in edges:
        if components_with_targets == 1:
            break
        ru = find(u)
        rv = find(v)
        if ru != rv:
            # Count targets in both components before merging
            # We track this implicitly: only merge if it reduces components_with_targets
            # But we need to know how many targets are in each component
            # Since we only care about connecting targets, we can use a different approach
            pass
    
    # Reset and use a smarter approach: track target count per component
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    target_count = [0] * (N + 1)
    for t in targets:
        target_count[t] = 1
    
    total_cost = 0
    components_with_targets = F
    
    for w, u, v in edges:
        if components_with_targets == 1:
            break
        ru = find(u)
        rv = find(v)
        if ru != rv:
            # Union by rank
            if rank[ru] < rank[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            if rank[ru] == rank[rv]:
                rank[ru] += 1
            
            # Update target count and check if we're connecting target components
            tu = target_count[ru]
            tv = target_count[rv]
            if tu > 0 and tv > 0:
                # Both components have targets, merging reduces components_with_targets
                components_with_targets -= (1 if tu > 0 and tv > 0 else 0)
                # Actually: if both have targets, they were separate, now merged
                # The number of target components decreases by 1
                components_with_targets = components_with_targets  # already decremented
                total_cost += w
            target_count[ru] = tu + tv
    
    print(total_cost)

solve()