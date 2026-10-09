import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return
    
    # Convert 1-based module IDs to 0-based indices
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
    
    # Greedy heuristic: place modules in order of decreasing connectivity degree
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    # Sort module indices by degree descending, then by index for stability
    modules_by_degree = sorted(range(n), key=lambda i: (-degree[i], i))
    
    # Greedy placement: assign modules to bays in this order
    # High degree modules get placed first and occupy central positions to minimize total distances
    positions = [0] * n
    bay_pos = 0
    # To centralize high-degree modules, we can use positions from 0 to n-1
    # We iterate and assign sequential positions; the order of modules determines the layout
    
    # Alternative strategy: interleave positions to centralize?
    # Classic greedy for linear arrangement: calculate position score.
    # Heuristic used here simply follows the degree sort.
    
    # We try to construct a position mapping. 
    # Simple mapping: module at rank k gets position k.
    placement_plan = list(range(n)) # This will map bay_index -> module_index
    
    # We need to map module_index -> bay_position (1-based)
    # So we iterate over modules in sorted order and assign them to bays 0..n-1
    for rank, mod_idx in enumerate(modules_by_degree):
        positions[mod_idx] = rank
    
    # Calculate total length
    total_len = 0
    for u, v in edges:
        dist = abs(positions[u] - positions[v])
        total_len += dist
        if total_len > B:
            break
    
    if total_len <= B:
        # Construct output: for bays 0 to n-1, which module is there?
        # We need to print position of module 1..n
        # positions[mod] is the 0-based bay.
        output_bays = [0] * n
        for mod_idx in range(n):
            output_bays[mod_idx] = positions[mod_idx] + 1
        
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, output_bays)) + "\n")
        return
    
    # If greedy failed, use BFS/Local Search since n is small
    
    # Start solution: Identity permutation
    current_pos = list(range(n))
    
    def calculate_cost(pos_vector, edges_list):
        s = 0
        for u, v in edges_list:
            s += abs(pos_vector[u] - pos_vector[v])
        return s
    
    current_cost = calculate_cost(current_pos, edges)
    
    if current_cost <= B:
        sys.stdout.write("YES\n")
        out = [0] * n
        for i in range(n):
            out[i] = current_pos[i] + 1
        sys.stdout.write(" ".join(map(str, out)) + "\n")
        return
    
    # BFS Setup to find a solution within cost budget B
    # Since B is small, we can use BFS on states: (permutation_tuple)
    # But we don't need to explore all reachable states, just those with cost <= B.
    # However, if there are NO solutions with cost <= B, we might explore many.
    # To manage worst case, we use a timeout mechanism.
    
    import time
    start_time = time.time()
    timeout_seconds = 4.0
    
    from collections import deque
    
    visited = {tuple(current_pos): 0} # stores min cost found for a state
    q = deque()
    q.append((list(current_pos), current_cost))
    
    found = False
    final_pos = None
    
    # Optimize by considering only swaps of adjacent elements in permutation
    # This generates the symmetric group S_n
    
    while q and not found:
        if time.time() - start_time > timeout_seconds:
            break
        
        state, cost = q.popleft()
        
        # If cost is already worse than B, we might have pushed it,
        # but we check before expanding and processing.
        if cost > B:
            continue
        
        # This is a valid solution
        if cost <= B:
            found = True
            final_pos = state
            break
        
        # Try all swaps of adjacent elements
        # For a permutation of size n, there are n-1 such swaps
        for i in range(n - 1):
            # swap elements at indices i and i+1 in the state array
            new_state = list(state)
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            
            # Optimization: calculate new cost based on change involving modules at i, i+1
            # A swap of positions i and i+1 changes the position of two modules.
            # Let the modules swapped be `a` (previously at i) and `b` (previously at i+1).
            # `a` moves from i to i+1 (change +1)
            # `b` moves from i+1 to i (change -1)
            # New cost = Old cost - sum(|i - pos[v]| for v conn to a) - sum(|i+1 - pos[v]| for v conn to b)
            #            + sum(|i+1 - pos[v]| for v conn to a) + sum(|i - pos[v]| for v conn to b)
            # Since i+1 = i + 1, we can simplify the change.
            # Let P_a = i, P_b = i+1.
            # Consider a neighbor v of 'a'. 
            # Old dist |P_a - pos[v]| = |i - pos[v]|.
            # New dist |P_b - pos[v]| = |i+1 - pos[v]|.
            # The difference for this neighbor is (|i+1 - pos[v]| - |i - pos[v]|).
            # If pos[v] <= i:  (i+1 - pos[v]) - (i - pos[v]) = 1.
            # If pos[v] >= i+1: (pos[v] - (i+1)) - (pos[v] - i) = -1.
            # If pos[v] == i (v is b): |i+1 - i| - |i - i| = 1.
            
            # Heuristic calculation of new cost is tricky in constant time without pos array.
            # But n is small (<=10), full recalculation is fast enough.
            
            new_cost = 0
            for u_node, v_node in edges:
                new_cost += abs(new_state[u_node] - new_state[v_node])
            
            if new_cost > B:
                continue
            
            tup_state = tuple(new_state)
            if tup_state not in visited:
                visited[tup_state] = new_cost
                q.append((new_state, new_cost))
                if new_cost <= B:
                    found = True
                    final_pos = new_state
                    break
        
        if found:
            break
    
    if found and final_pos is not None:
        sys.stdout.write("YES\n")
        # final_pos maps module_index -> position_index (0-based)
        out = [str(p + 1) for p in final_pos]
        sys.stdout.write(" ".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()