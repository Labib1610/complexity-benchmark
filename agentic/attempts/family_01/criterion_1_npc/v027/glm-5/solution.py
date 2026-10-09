import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    # Check bipartite components and assign colors 1 or 2
    is_bipartite = True
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print("NO")
        return
    
    # Build conflict graph between bipartite components
    # Nodes are component indices
    comp_id = [-1] * n
    comp_color = []  # color of first node in component
    comp_nodes = []  # list of nodes in each component
    num_comp = 0
    for i in range(n):
        if comp_id[i] == -1:
            comp_id[i] = num_comp
            comp_color.append(color[i])
            comp_nodes.append([i])
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = num_comp
                        comp_nodes[num_comp].append(v)
                        stack.append(v)
            num_comp += 1
    
    # Conflict between components
    conflict = [set() for _ in range(num_comp)]
    for u in range(n):
        for v in adj[u]:
            cu, cv = comp_id[u], comp_id[v]
            if cu != cv:
                conflict[cu].add(cv)
                conflict[cv].add(cu)
    
    # DP: dp[mask] = True if mask is achievable
    # dp[mask] can transition to dp[mask | (1<<c)] if component c can be added
    # A component c can be added with color 3 if:
    # - For all neighbors n in conflict[c] that are in mask, they have color != 3
    # - For all neighbors n in conflict[c] that are in mask, they have color != color[c]
    # Actually, we need to track which components are colored 3 vs 1/2
    
    # Let's use dp[mask] = True/False
    # For each mask, we know which components are assigned
    # We need to track which are colored 3
    # Let's use dp[mask] = set of possible "colored 3" subsets within mask
    
    # To optimize, we can use dp[mask] = bitmask of components colored 3
    # But we need to track multiple possibilities
    
    # Alternative: dp[mask] = True if achievable
    # We also track parent[mask] = (prev_mask, component_added, color_added)
    
    # Let's use a simpler approach:
    # dp[mask] = set of possible "colored 3" subsets
    # This can be large, but for n <= 40 and num_comp <= 40, it might be manageable
    
    # Actually, let's use dp[mask] = bitmask representing which components in mask are colored 3
    # We iterate through masks in increasing order
    
    # But we need to track multiple possible "colored 3" configurations for each mask
    # Let's use a dictionary: dp[mask] = set of possible "colored 3" bitmasks
    
    # To reduce complexity, we can use the fact that the graph is bipartite
    # and conflicts are between components
    
    # Let's use a different approach:
    # dp[mask] = True if mask is achievable
    # We also track which components in mask are colored 3 using a separate structure
    
    # Actually, let's just use a simple DP with backtracking
    
    # dp[mask] = set of possible "colored 3" configurations
    # For each mask, we try to add a component c not in mask
    
    from collections import defaultdict
    
    dp = defaultdict(set)
    dp[0].add(0)  # mask 0, colored_3 = 0
    
    parent = {}  # parent[mask, colored_3] = (prev_mask, prev_colored_3, comp, color)
    
    full_mask = (1 << num_comp) - 1
    
    for mask in range(1 << num_comp):
        if mask not in dp:
            continue
        for colored_3 in dp[mask]:
            # Try to add each component not in mask
            for c in range(num_comp):
                if mask & (1 << c):
                    continue
                new_mask = mask | (1 << c)
                
                # Check if we can color component c with color 3
                can_color_3 = True
                for nb in conflict[c]:
                    if nb < c:  # Only check neighbors with smaller index to avoid double counting
                        if (mask & (1 << nb)) and (colored_3 & (1 << nb)):
                            can_color_3 = False
                            break
                
                # Also check neighbors with larger index
                for nb in conflict[c]:
                    if nb > c:
                        if mask & (1 << nb):
                            if colored_3 & (1 << nb):
                                can_color_3 = False
                                break
                
                if can_color_3:
                    new_colored_3 = colored_3 | (1 << c)
                    if new_colored_3 not in dp[new_mask]:
                        dp[new_mask].add(new_colored_3)
                        parent[(new_mask, new_colored_3)] = (mask, colored_3, c, 3)
                
                # Check if we can color component c with its original color (1 or 2)
                can_color_orig = True
                orig_color = comp_color[c]
                for nb in conflict[c]:
                    if mask & (1 << nb):
                        nb_is_3 = (colored_3 & (1 << nb)) != 0
                        if nb_is_3:
                            continue  # nb is color 3, no conflict with orig_color
                        else:
                            # nb has its original color
                            nb_orig_color = comp_color[nb]
                            if nb_orig_color == orig_color:
                                can_color_orig = False
                                break
                
                if can_color_orig:
                    new_colored_3 = colored_3  # c is not colored 3
                    if new_colored_3 not in dp[new_mask]:
                        dp[new_mask].add(new_colored_3)
                        parent[(new_mask, new_colored_3)] = (mask, colored_3, c, orig_color)
    
    if full_mask not in dp or len(dp[full_mask]) == 0:
        print("NO")
        return
    
    # Reconstruct the solution
    colored_3 = next(iter(dp[full_mask]))
    mask = full_mask
    
    comp_final_color = [0] * num_comp
    while mask > 0:
        prev_mask, prev_colored_3, c, col = parent[(mask, colored_3)]
        comp_final_color[c] = col
        mask = prev_mask
        colored_3 = prev_colored_3
    
    # Assign colors to all nodes
    result = [0] * n
    for c in range(num_comp):
        col = comp_final_color[c]
        if col == 3:
            for node in comp_nodes[c]:
                result[node] = 3
        else:
            for node in comp_nodes[c]:
                result[node] = color[node]
    
    print("YES")
    print(" ".join(map(str, result)))

solve()