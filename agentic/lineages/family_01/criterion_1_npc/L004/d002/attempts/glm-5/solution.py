import sys

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # Check if graph is bipartite and get 2-coloring for each component
    color = [-1] * n
    components = []
    valid = True
    
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS for bipartite check
        queue = [start]
        color[start] = 0
        comp_nodes = []
        while queue:
            u = queue.pop()
            comp_nodes.append(u)
            for v in range(n):
                if (adj[u] >> v) & 1:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        valid = False
                        break
            if not valid:
                break
        if not valid:
            break
        components.append(comp_nodes)
    
    if not valid:
        print("NO")
        return
    
    # Build DP for each component
    # For each component, find all valid 3-colorings consistent with its 2-coloring
    comp_colorings = []
    for comp_nodes in components:
        size = len(comp_nodes)
        # Map local index to global index
        local_to_global = {i: node for i, node in enumerate(comp_nodes)}
        global_to_local = {node: i for i, node in enumerate(comp_nodes)}
        
        # Build local adjacency
        local_adj = [0] * size
        for i, node in enumerate(comp_nodes):
            mask = 0
            for j, other in enumerate(comp_nodes):
                if (adj[node] >> other) & 1:
                    mask |= 1 << j
            local_adj[i] = mask
        
        # Determine which group each local node belongs to (based on global color)
        group = [color[local_to_global[i]] for i in range(size)]
        
        # Find valid colorings
        valid_masks = []
        # Group 0 gets colors from {0, 1}, Group 1 gets colors from {2}
        # Or Group 0 gets colors from {2}, Group 1 gets colors from {0, 1}
        
        # Case 1: Group 0 -> {0, 1}, Group 1 -> {2}
        # Group 0 nodes can be colored 0 or 1, Group 1 nodes must be 2
        case1_valid = True
        # Check if Group 1 nodes can all be color 2 (no edges within Group 1)
        for i in range(size):
            if group[i] == 1:  # Group 1
                for j in range(size):
                    if group[j] == 1 and ((local_adj[i] >> j) & 1):
                        case1_valid = False
                        break
            if not case1_valid:
                break
        
        if case1_valid:
            # Group 0 nodes: try all subsets colored 1 (rest colored 0)
            group0_nodes = [i for i in range(size) if group[i] == 0]
            k = len(group0_nodes)
            for subset in range(1 << k):
                local_color = [0] * size
                for i in range(size):
                    if group[i] == 1:
                        local_color[i] = 2
                
                # Assign colors to group 0 nodes based on subset
                for idx, node in enumerate(group0_nodes):
                    if (subset >> idx) & 1:
                        local_color[node] = 1
                    else:
                        local_color[node] = 0
                
                # Check validity
                ok = True
                for i in range(size):
                    for j in range(i + 1, size):
                        if ((local_adj[i] >> j) & 1) and local_color[i] == local_color[j]:
                            ok = False
                            break
                    if not ok:
                        break
                
                if ok:
                    mask = 0
                    for i in range(size):
                        mask |= local_color[i] << (2 * i)
                    valid_masks.append(mask)
        
        # Case 2: Group 0 -> {2}, Group 1 -> {0, 1}
        case2_valid = True
        for i in range(size):
            if group[i] == 0:  # Group 0
                for j in range(size):
                    if group[j] == 0 and ((local_adj[i] >> j) & 1):
                        case2_valid = False
                        break
            if not case2_valid:
                break
        
        if case2_valid:
            group1_nodes = [i for i in range(size) if group[i] == 1]
            k = len(group1_nodes)
            for subset in range(1 << k):
                local_color = [0] * size
                for i in range(size):
                    if group[i] == 0:
                        local_color[i] = 2
                
                for idx, node in enumerate(group1_nodes):
                    if (subset >> idx) & 1:
                        local_color[node] = 1
                    else:
                        local_color[node] = 0
                
                ok = True
                for i in range(size):
                    for j in range(i + 1, size):
                        if ((local_adj[i] >> j) & 1) and local_color[i] == local_color[j]:
                            ok = False
                            break
                    if not ok:
                        break
                
                if ok:
                    mask = 0
                    for i in range(size):
                        mask |= local_color[i] << (2 * i)
                    valid_masks.append(mask)
        
        comp_colorings.append(valid_masks)
    
    # DP to find lexicographically smallest valid coloring
    # dp[mask] = True if mask is achievable
    # We process components in order of their smallest node index
    
    # Sort components by their minimum node index
    comp_order = sorted(range(len(components)), key=lambda i: min(components[i]))
    
    # Reorder comp_colorings according to comp_order
    ordered_colorings = [comp_colorings[i] for i in comp_order]
    ordered_components = [components[i] for i in comp_order]
    
    # dp[mask] = True if achievable
    # mask encodes colors for all nodes: 2 bits per node
    # We'll use a dictionary for sparse representation
    
    dp = {0: True}
    
    for comp_idx, colorings in enumerate(ordered_colorings):
        new_dp = {}
        comp_nodes = ordered_components[comp_idx]
        size = len(comp_nodes)
        
        for prev_mask in dp:
            for coloring_mask in colorings:
                # Combine prev_mask with coloring_mask
                new_mask = prev_mask
                for i, node in enumerate(comp_nodes):
                    color_val = (coloring_mask >> (2 * i)) & 3
                    new_mask |= color_val << (2 * node)
                if new_mask not in new_dp:
                    new_dp[new_mask] = True
        
        dp = new_dp
        if not dp:
            print("NO")
            return
    
    if not dp:
        print("NO")
        return
    
    # Find lexicographically smallest valid coloring
    # We need to find the mask that gives smallest b_1, then b_2, etc.
    best_mask = None
    for mask in dp:
        if best_mask is None:
            best_mask = mask
        else:
            # Compare lexicographically
            for node in range(n):
                c1 = (mask >> (2 * node)) & 3
                c2 = (best_mask >> (2 * node)) & 3
                if c1 < c2:
                    best_mask = mask
                    break
                elif c1 > c2:
                    break
    
    # Output result
    result = []
    for node in range(n):
        color_val = (best_mask >> (2 * node)) & 3
        result.append(str(color_val + 1))  # Convert 0-indexed to 1-indexed
    
    print("YES")
    print(" ".join(result))

solve()