import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    
    # Collaborative load table
    # load[a][b] gives the load for agencies a and b (1-indexed)
    load = [[0]*4 for _ in range(4)]
    load[1][1] = 10
    load[2][2] = 16
    load[3][3] = 26
    load[1][2] = load[2][1] = 5
    load[1][3] = load[3][1] = 10
    load[2][3] = load[3][2] = 13
    
    # Precompute for each edge (u,v) and each assignment (f_u, f_v) the contribution
    # to the equation: load(f_u, f_v) - f_u^2 - f_v^2
    # We need sum of these contributions to be 0.
    
    # For efficiency, precompute edge_contrib[edge_idx][f_u][f_v]
    # But since n <= 40, we can compute on the fly or store in a dict
    
    # Let's identify connected components
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            components.append(comp)
    
    # For each component, we need to find valid assignments
    # Since n <= 40, we can use meet-in-the-middle for large components
    
    # Sort components by size (process smaller ones first for efficiency)
    components.sort(key=len)
    
    # We'll store valid assignments for each component
    # For small components, we can enumerate all possibilities
    # For large components, we use meet-in-the-middle
    
    # Global assignment
    final_assignment = [0] * (n + 1)
    
    for comp in components:
        size = len(comp)
        if size == 0:
            continue
        
        # Map local index to global department number
        idx_to_dept = {i: comp[i] for i in range(size)}
        dept_to_idx = {comp[i]: i for i in range(size)}
        
        # Collect edges within this component
        comp_edges = []
        for u, v in edges:
            if u in dept_to_idx and v in dept_to_idx:
                comp_edges.append((dept_to_idx[u], dept_to_idx[v]))
        
        # For each node, compute its contribution to the equation
        # The equation is: sum over edges of (load - f_u^2 - f_v^2) = 0
        # Rearranging: sum over edges of load = sum over nodes of (degree * f^2)
        # But we can think of it as:
        # For each edge (u,v): contribution = load(f_u, f_v) - f_u^2 - f_v^2
        # Sum of contributions = 0
        
        # For a single node u with degree d_u:
        # Its contribution to the sum is: -d_u * f_u^2 (from the -f_u^2 term for each edge)
        # Plus the load terms from edges involving u
        
        # Let's compute for each assignment the total contribution
        # We need sum = 0
        
        if size <= 12:
            # Enumerate all 3^size possibilities
            best = None
            for mask in range(3**size):
                assignment = [0] * size
                temp = mask
                for i in range(size):
                    assignment[i] = (temp % 3) + 1
                    temp //= 3
                
                # Compute total contribution
                total = 0
                for u, v in comp_edges:
                    fu = assignment[u]
                    fv = assignment[v]
                    total += load[fu][fv] - fu*fu - fv*fv
                
                if total == 0:
                    if best is None or assignment < best:
                        best = assignment[:]
            
            if best is None:
                print("NO")
                return
            
            for i in range(size):
                final_assignment[idx_to_dept[i]] = best[i]
        else:
            # Meet in the middle
            # Split into two halves
            half = size // 2
            left_indices = list(range(half))
            right_indices = list(range(half, size))
            
            # Precompute which edges are internal to left, internal to right, and crossing
            left_internal = []
            right_internal = []
            crossing = []
            
            for u, v in comp_edges:
                if u < half and v < half:
                    left_internal.append((u, v))
                elif u >= half and v >= half:
                    right_internal.append((u - half, v - half))
                else:
                    if u < half:
                        crossing.append((u, v - half))
                    else:
                        crossing.append((v, u - half))
            
            # For left half: enumerate all 3^half assignments
            # Store (total_contribution, assignment) in a dict
            # Key: contribution from left internal edges + contribution from left nodes in crossing edges
            # We need to be careful about how we split the contribution
            
            # Actually, let's think differently:
            # For each edge (u,v):
            # - If both in left: contribution depends only on left assignment
            # - If both in right: contribution depends only on right assignment
            # - If crossing: contribution = load(f_u, f_v) - f_u^2 - f_v^2
            #   This can be split as: (load(f_u, f_v) - f_u^2) + (-f_v^2)
            #   Or: (-f_u^2) + (load(f_u, f_v) - f_v^2)
            #   Or we can keep it together and match based on the crossing edge values
            
            # Let's use a different approach:
            # For crossing edges, we'll match based on the required contribution from the right side
            
            # For each left assignment, compute:
            # - Contribution from left internal edges
            # - For each crossing edge (u, v) where u is in left:
            #   We need load(f_u, f_v) - f_u^2 - f_v^2
            #   The part depending only on left is: -f_u^2
            #   The part depending on both is: load(f_u, f_v)
            #   The part depending only on right is: -f_v^2
            
            # So for a crossing edge (u, v) with u in left, v in right:
            # contribution = load(f_u, f_v) - f_u^2 - f_v^2
            # We can rewrite this as:
            # contribution = (load(f_u, f_v) - f_v^2) - f_u^2
            # The term (load(f_u, f_v) - f_v^2) depends on both f_u and f_v
            # The term -f_u^2 depends only on f_u
            
            # Alternative: for each crossing edge, we'll match based on f_u and f_v
            # We can enumerate all possible (f_u, f_v) pairs and their contributions
            
            # Let's use a cleaner approach:
            # For each left assignment, compute the total contribution from:
            # 1. Left internal edges
            # 2. The -f_u^2 part from crossing edges where u is in left
            # 
            # For each right assignment, compute the total contribution from:
            # 1. Right internal edges
            # 2. The -f_v^2 part from crossing edges where v is in right
            # 3. The load(f_u, f_v) part from crossing edges (this depends on both)
            
            # Actually, let's think of it as:
            # total = left_internal_contrib + right_internal_contrib + crossing_contrib
            # 
            # For crossing edges, we need to match left and right assignments
            # 
            # Let's define:
            # left_contrib = sum over left internal edges of (load - f_u^2 - f_v^2)
            #              + sum over crossing edges of (-f_u^2) where u is in left
            # 
            # right_contrib = sum over right internal edges of (load - f_u^2 - f_v^2)
            #               + sum over crossing edges of (-f_v^2) where v is in right
            # 
            # crossing_contrib = sum over crossing edges of load(f_u, f_v)
            # 
            # We need: left_contrib + right_contrib + crossing_contrib = 0
            # 
            # For each left assignment, we compute left_contrib
            # For each right assignment, we compute right_contrib
            # 
            # The crossing_contrib depends on both, so we need to match them
            # 
            # We can use a dict to store for each (left_contrib, crossing_pattern) the best left assignment
            # where crossing_pattern encodes the f_u values for crossing edges
            # 
            # Then for each right assignment, we compute right_contrib and crossing_pattern
            # and look for a matching left_contrib
            
            # Let's simplify: for each crossing edge (u, v) with u in left, v in right:
            # We need to match f_u and f_v
            # 
            # We can encode the crossing pattern as a tuple of (f_u for each crossing edge)
            # 
            # For each left assignment, we compute:
            # - left_contrib (from left internal edges and -f_u^2 from crossing edges)
            # - crossing_pattern_left: tuple of f_u values for each crossing edge
            # 
            # For each right assignment, we compute:
            # - right_contrib (from right internal edges and -f_v^2 from crossing edges)
            # - crossing_pattern_right: tuple of f_v values for each crossing edge
            # 
            # Then we need to find pairs where:
            # left_contrib + right_contrib + sum over crossing edges of load(f_u, f_v) = 0
            # 
            # We can use a dict: key = (left_contrib, crossing_pattern_left)
            # value = best left assignment (lexicographically smallest)
            # 
            # Then for each right assignment, we iterate over all possible crossing_pattern_left
            # and check if there's a valid match
            
            # But this might be slow if there are many crossing edges
            # 
            # Let's optimize: for each crossing edge, we precompute the load table
            # 
            # Actually, let's use a different encoding:
            # For each left assignment, we compute:
            # - left_contrib
            # - For each crossing edge, we store f_u
            # 
            # We use a dict: key = left_contrib
            # value = dict mapping crossing_pattern_left to best left assignment
            # 
            # For each right assignment, we compute:
            # - right_contrib
            # - For each crossing edge, we store f_v
            # 
            # Then we need: left_contrib + right_contrib + crossing_load = 0
            # where crossing_load = sum over crossing edges of load(f_u, f_v)
            # 
            # For each right assignment, we iterate over all possible left_contrib values
            # and check if there exists a crossing_pattern_left such that
            # left_contrib + right_contrib + crossing_load = 0
            
            # This is still complex. Let me think of a simpler approach.
            
            # Alternative: for each left assignment, compute left_contrib and crossing_pattern_left
            # Store in dict: key = (left_contrib, crossing_pattern_left), value = best assignment
            # 
            # For each right assignment, compute right_contrib and crossing_pattern_right
            # Then compute crossing_load = sum over crossing edges of load(f_u, f_v)
            # Check if there exists a left_contrib such that left_contrib + right_contrib + crossing_load = 0
            # 
            # We can iterate over all stored left_contrib values and check
            
            # Let's implement this
            
            left_dict = {}  # key: (left_contrib, tuple of f_u for crossing edges), value: best left assignment
            
            for mask in range(3**half):
                assignment = [0] * half
                temp = mask
                for i in range(half):
                    assignment[i] = (temp % 3) + 1
                    temp //= 3
                
                # Compute left_contrib
                left_contrib = 0
                for u, v in left_internal:
                    fu = assignment[u]
                    fv = assignment[v]
                    left_contrib += load[fu][fv] - fu*fu - fv*fv
                
                # Compute -f_u^2 for crossing edges where u is in left
                crossing_pattern_left = []
                for u, v in crossing:
                    fu = assignment[u]
                    left_contrib -= fu * fu
                    crossing_pattern_left.append(fu)
                
                crossing_pattern_left = tuple(crossing_pattern_left)
                
                key = (left_contrib, crossing_pattern_left)
                if key not in left_dict or assignment < left_dict[key]:
                    left_dict[key] = assignment
            
            # Now process right half
            right_size = size - half
            best_left = None
            best_right = None
            best_left_key = None
            
            for mask in range(3**right_size):
                assignment = [0] * right_size
                temp = mask
                for i in range(right_size):
                    assignment[i] = (temp % 3) + 1
                    temp //= 3
                
                # Compute right_contrib
                right_contrib = 0
                for u, v in right_internal:
                    fu = assignment[u]
                    fv = assignment[v]
                    right_contrib += load[fu][fv] - fu*fu - fv*fv
                
                # Compute -f_v^2 for crossing edges where v is in right
                crossing_pattern_right = []
                for u, v in crossing:
                    fv = assignment[v]
                    right_contrib -= fv * fv
                    crossing_pattern_right.append(fv)
                
                crossing_pattern_right = tuple(crossing_pattern_right)
                
                # Now we need to find a left assignment such that
                # left_contrib + right_contrib + crossing_load = 0
                # where crossing_load = sum over crossing edges of load(f_u, f_v)
                
                # For each stored left assignment, compute crossing_load
                for (left_contrib, crossing_pattern_left), left_assignment in left_dict.items():
                    crossing_load = 0
                    for i, (u, v) in enumerate(crossing):
                        fu = crossing_pattern_left[i]
                        fv = crossing_pattern_right[i]
                        crossing_load += load[fu][fv]
                    
                    total = left_contrib + right_contrib + crossing_load
                    if total == 0:
                        # Found a valid assignment
                        # Check if this is the best (lexicographically smallest)
                        full_assignment = left_assignment + assignment
                        if best_left is None:
                            best_left = left_assignment[:]
                            best_right = assignment[:]
                            best_left_key = (left_contrib, crossing_pattern_left)
                        else:
                            # Compare full assignments
                            current_full = left_assignment + assignment
                            best_full = best_left + best_right
                            if current_full < best_full:
                                best_left = left_assignment[:]
                                best_right = assignment[:]
                                best_left_key = (left_contrib, crossing_pattern_left)
            
            if best_left is None:
                print("NO")
                return
            
            # Reconstruct the full assignment
            for i in range(half):
                final_assignment[idx_to_dept[i]] = best_left[i]
            for i in range(right_size):
                final_assignment[idx_to_dept[half + i]] = best_right[i]
    
    # Output the result
    print("YES")
    print(" ".join(map(str, final_assignment[1:])))

if __name__ == "__main__":
    solve()