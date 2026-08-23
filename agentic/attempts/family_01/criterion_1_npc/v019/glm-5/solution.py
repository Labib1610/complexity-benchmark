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
    
    # We need to find the lexicographically smallest valid assignment.
    # Since n <= 40, we can use meet-in-the-middle.
    # Split vertices into two halves: left (0..n1-1) and right (n1..n-1).
    # For each half, enumerate all valid assignments.
    # For the right half, we need to check compatibility with the left half.
    
    n1 = n // 2
    n2 = n - n1
    
    left_indices = list(range(n1))
    right_indices = list(range(n1, n))
    
    # Precompute internal edges for each half
    left_edges = []
    for u in left_indices:
        for v in adj[u]:
            if v > u and v < n1:
                left_edges.append((u, v))
    
    right_edges = []
    for u in right_indices:
        for v in adj[u]:
            if v > u:
                right_edges.append((u - n1, v - n1))
    
    # Cross edges: between left and right halves
    # For each right vertex, store list of left neighbors
    cross_adj = [[] for _ in range(n2)]
    for u in left_indices:
        for v in adj[u]:
            if v >= n1:
                cross_adj[v - n1].append(u)
    
    # Enumerate valid assignments for left half
    # Returns list of (assignment_tuple, forbidden_mask_for_each_right_vertex)
    # forbidden_mask: bitmask of tags forbidden for right vertex due to this left assignment
    # Tags are 1, 2, 3 -> we use bits 0, 1, 2 for tags 1, 2, 3
    
    left_assignments = []
    
    # DFS for left half
    # We iterate in lex order to get sorted assignments
    # But we need to store all valid ones
    
    def dfs_left(u, current_assign, results):
        if u == n1:
            # Compute forbidden masks for right vertices
            forbidden = [0] * n2
            for r in range(n2):
                mask = 0
                for l_neighbor in cross_adj[r]:
                    tag = current_assign[l_neighbor]
                    mask |= (1 << (tag - 1))
                forbidden[r] = mask
            results.append((tuple(current_assign), forbidden))
            return
        
        for tag in [1, 2, 3]:
            valid = True
            for (a, b) in left_edges:
                if b == u:
                    if current_assign[a] == tag:
                        valid = False
                        break
                elif a == u:
                    # a == u, b > u, but b not assigned yet
                    pass
            if valid:
                current_assign[u] = tag
                dfs_left(u + 1, current_assign, results)
                current_assign[u] = 0
    
    dfs_left(0, [0] * n1, left_assignments)
    
    if not left_assignments:
        print("NO")
        return
    
    # For right half, we need to find valid assignments given forbidden masks from left
    # We use a dictionary: for each (forbidden_tuple), store the lexicographically smallest right assignment
    # forbidden_tuple is a tuple of n2 integers (bitmasks)
    
    # But forbidden_tuple can be large. Instead, we process right half independently first.
    # Enumerate all valid right assignments (ignoring cross edges).
    # Then for each left assignment, we check which right assignments are compatible.
    
    # Enumerate valid right assignments
    right_valid_assignments = []
    
    def dfs_right(u, current_assign, results):
        if u == n2:
            results.append(tuple(current_assign))
            return
        
        for tag in [1, 2, 3]:
            valid = True
            for (a, b) in right_edges:
                if b == u:
                    if current_assign[a] == tag:
                        valid = False
                        break
            if valid:
                current_assign[u] = tag
                dfs_right(u + 1, current_assign, results)
                current_assign[u] = 0
    
    dfs_right(0, [0] * n2, right_valid_assignments)
    
    if not right_valid_assignments:
        print("NO")
        return
    
    # Sort right assignments lexicographically
    right_valid_assignments.sort()
    
    # For each left assignment, find the first compatible right assignment
    best_left = None
    best_right = None
    
    for left_assign, forbidden in left_assignments:
        # Find the first right assignment that is compatible
        for right_assign in right_valid_assignments:
            compatible = True
            for r in range(n2):
                tag = right_assign[r]
                if forbidden[r] & (1 << (tag - 1)):
                    compatible = False
                    break
            if compatible:
                # This is the best right assignment for this left assignment
                # Since left_assignments are generated in lex order, the first found is optimal
                best_left = left_assign
                best_right = right_assign
                break
        if best_left is not None:
            break
    
    if best_left is None:
        print("NO")
        return
    
    # Construct final answer
    result = list(best_left) + list(best_right)
    print("YES")
    print(' '.join(map(str, result)))

solve()