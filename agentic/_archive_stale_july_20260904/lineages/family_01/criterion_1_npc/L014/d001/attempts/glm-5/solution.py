import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # Precompute connected components
    comp_id = [0] * (n + 1)
    comp_nodes = []
    cid = 0
    for i in range(1, n + 1):
        if comp_id[i] == 0:
            cid += 1
            comp_id[i] = cid
            stack = [i]
            nodes = [i]
            while stack:
                u = stack.pop()
                nb = adj[u]
                while nb:
                    b = nb & -nb
                    v = b.bit_length() - 1
                    if comp_id[v] == 0:
                        comp_id[v] = cid
                        stack.append(v)
                        nodes.append(v)
                    nb ^= b
            comp_nodes.append(nodes)
    
    # For each component, find all valid 3-colorings
    comp_colorings = []
    for nodes in comp_nodes:
        k = len(nodes)
        if k > 3:
            print("NO")
            return
        # Map local index
        local_idx = {node: i for i, node in enumerate(nodes)}
        # Build local adjacency
        local_adj = [0] * k
        for node in nodes:
            li = local_idx[node]
            nb = adj[node]
            while nb:
                b = nb & -nb
                v = b.bit_length() - 1
                if v in local_idx:
                    local_adj[li] |= 1 << local_idx[v]
                nb ^= b
        # Enumerate all 3^k colorings
        colorings = []
        for mask in range(3 ** k):
            ok = True
            for i in range(k):
                ci = (mask // (3 ** i)) % 3
                nb = local_adj[i]
                while nb:
                    b = nb & -nb
                    j = b.bit_length() - 1
                    cj = (mask // (3 ** j)) % 3
                    if ci == cj:
                        ok = False
                        nb = 0
                        break
                    nb ^= b
                if not ok:
                    break
            if ok:
                colorings.append(mask)
        if not colorings:
            print("NO")
            return
        comp_colorings.append(colorings)
    
    # DP over components to find lexicographically smallest coloring
    # State: for each component, which coloring index is used
    # We process departments 1..n in order, but components are independent
    # To get lexicographically smallest, we need to choose colorings per component
    # such that the resulting assignment is lexicographically smallest.
    
    # Since components are independent, we can process them one by one,
    # but lexicographic order depends on the global sequence.
    # We'll use DP where we track the best assignment for processed components.
    
    # Actually, since components are independent, the lexicographically smallest
    # global assignment is obtained by choosing for each component the coloring
    # that is lexicographically smallest when placed in its positions.
    # But components' positions may interleave, so we need to be careful.
    
    # Let's do a DP over components, tracking the partial assignment.
    # Since n <= 40, and each component has at most 3 nodes, total states manageable.
    
    # We'll process components in order of their smallest node (which is natural).
    # For each component, we try all its colorings, and combine with the best previous.
    
    # Represent assignment as tuple of length n (1-indexed, we'll use 0-indexed internally)
    
    # But comparing tuples of length 40 is fine.
    
    # Initialize with empty assignment
    best = None
    for colorings in comp_colorings:
        nodes = comp_nodes[comp_colorings.index(colorings)]
        # Actually we need to process in order, let's restructure
        pass
    
    # Let's restructure properly
    # comp_nodes and comp_colorings are aligned by index
    num_comps = len(comp_nodes)
    # Sort components by their minimum node to process in order
    comp_order = sorted(range(num_comps), key=lambda c: min(comp_nodes[c]))
    
    # DP: best assignment (as tuple) after processing some components
    # Start with empty tuple
    dp = [()]
    # We need to map component index to its colorings
    comp_col_map = [comp_colorings[c] for c in comp_order]
    comp_nodes_map = [comp_nodes[c] for c in comp_order]
    
    for ci in range(num_comps):
        nodes = comp_nodes_map[ci]
        colorings = comp_col_map[ci]
        k = len(nodes)
        new_dp = None
        for partial in dp:
            for mask in colorings:
                # Build assignment for this component
                # partial is tuple of length processed so far
                # We need to insert the new assignments at correct positions
                # Since we process components in order of min node, and components are disjoint,
                # the new nodes are all > all previously processed nodes? Not necessarily.
                # Actually, components are disjoint, but their node ranges can interleave.
                # So we need to merge.
                pass
        # This approach is getting complicated. Let's think differently.
        break
    
    # Alternative: Since each component has at most 3 nodes, and n <= 40,
    # we can do a backtracking search over all departments 1..n in order,
    # trying colors 1,2,3 and pruning invalid ones.
    # With good pruning, this should be fast enough.
    
    # Let's implement backtracking with lexicographic order (try 1, then 2, then 3)
    color = [0] * (n + 1)
    
    def backtrack(i):
        if i > n:
            return True
        for c in range(1, 4):
            # Check neighbors j < i
            nb = adj[i]
            valid = True
            while nb:
                b = nb & -nb
                j = b.bit_length() - 1
                if j < i and color[j] == c:
                    valid = False
                    nb = 0
                    break
                nb ^= b
            if valid:
                color[i] = c
                if backtrack(i + 1):
                    return True
                color[i] = 0
        return False
    
    if backtrack(1):
        print("YES")
        print(' '.join(str(color[i]) for i in range(1, n + 1)))
    else:
        print("NO")

solve()