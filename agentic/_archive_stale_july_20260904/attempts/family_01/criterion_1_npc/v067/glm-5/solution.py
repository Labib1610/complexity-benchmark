import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Precompute connected components
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                v_mask = adj[u]
                v = 0
                while v_mask:
                    if v_mask & 1:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                    v_mask >>= 1
                    v += 1
            components.append(comp)
    
    # For each component, find all valid colorings
    # A coloring is valid if no two adjacent nodes have same color
    # We need to find lexicographically smallest global coloring
    
    # For each component, precompute valid colorings
    comp_colorings = []
    
    for comp in components:
        k = len(comp)
        if k == 1:
            # Single node, can be any of 1, 2, 3
            comp_colorings.append([(comp[0], c) for c in [1, 2, 3]])
            continue
        
        # Map local index to global index
        idx_map = {comp[i]: i for i in range(k)}
        
        # Build local adjacency
        local_adj = [0] * k
        for i, u in enumerate(comp):
            for j, v in enumerate(comp):
                if adj[u] & (1 << v):
                    local_adj[i] |= 1 << j
        
        valid_colorings = []
        
        # Try all 3^k colorings
        for mask in range(3**k):
            colors = []
            temp = mask
            valid = True
            for _ in range(k):
                colors.append(temp % 3 + 1)
                temp //= 3
            
            # Check validity
            for i in range(k):
                if not valid:
                    break
                c_i = colors[i]
                neighbors = local_adj[i]
                j = 0
                while neighbors:
                    if neighbors & 1:
                        if colors[j] == c_i:
                            valid = False
                            break
                    neighbors >>= 1
                    j += 1
            
            if valid:
                # Store as list of (node, color) sorted by node index
                coloring = [(comp[i], colors[i]) for i in range(k)]
                coloring.sort()  # Sort by node index
                valid_colorings.append(coloring)
        
        if not valid_colorings:
            print("NO")
            return
        
        # Sort colorings lexicographically by colors
        valid_colorings.sort(key=lambda x: [c for _, c in x])
        comp_colorings.append(valid_colorings)
    
    # Now we need to find lexicographically smallest global coloring
    # by combining one coloring from each component
    
    # Sort components by their minimum node index
    comp_indices = sorted(range(len(components)), key=lambda i: min(components[i]))
    
    # We need to find the combination that gives lexicographically smallest result
    # Since components are independent, we can greedily choose the smallest valid coloring
    # for each component in order of their minimum node index
    
    # But we need to be careful: the global order depends on all nodes
    # So we need to merge the colorings properly
    
    # Actually, since components are independent, the lexicographically smallest
    # global coloring is achieved by choosing the lexicographically smallest
    # coloring for each component (when sorted by node indices)
    
    # Let's verify this: if we have two components A and B where all nodes in A
    # have smaller indices than all nodes in B, then we should minimize A's coloring
    # first, then B's. This is exactly what we get by sorting components by min index.
    
    # But if components interleave (which shouldn't happen since they're disconnected),
    # we'd need to be more careful. Since they're disconnected, components can't interleave.
    
    # So we can just concatenate the sorted colorings
    result = [0] * n
    
    for i in comp_indices:
        coloring = comp_colorings[i][0]  # Take the smallest valid coloring
        for node, color in coloring:
            result[node] = color
    
    print("YES")
    print(" ".join(map(str, result)))

solve()