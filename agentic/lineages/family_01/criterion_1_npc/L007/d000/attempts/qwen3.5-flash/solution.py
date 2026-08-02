import sys

# Increase recursion depth for deep recursion in backtracking
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list using bitmasks for efficiency
    # adj[u] will store a bitmask where the v-th bit is set if v is a neighbor of u
    adj = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Precompute population count for 0..7
    POPCOUNT = [0, 1, 1, 2, 1, 2, 2, 3]
    
    # Colors are 1, 2, 3. Internally we use bits 0, 1, 2.
    # forbidden[u] is a bitmask of forbidden colors for node u.
    forbidden = [0] * (n + 1)
    colors = [0] * (n + 1)

    # Function to check if the remaining nodes (represented by mask) can be colored
    # given the current forbidden constraints.
    # It uses MRV (Minimum Remaining Values) heuristic.
    def can_color(mask, forbidden_state):
        if mask == 0:
            return True
        
        # Find the uncolored node with the fewest available colors
        best_u = -1
        min_avail_count = 4
        best_avail = 0
        
        temp_mask = mask
        while temp_mask:
            bit_val = temp_mask & -temp_mask
            u = bit_val.bit_length() - 1
            temp_mask ^= bit_val
            
            # Available colors are bits 0,1,2 not in forbidden_state[u]
            avail = 7 & ~forbidden_state[u]
            if avail == 0:
                return False
            
            count = POPCOUNT[avail]
            if count < min_avail_count:
                min_avail_count = count
                best_avail = avail
                best_u = u
                if count == 1:
                    break
        
        if best_u == -1:
            return False # Should not happen if mask != 0
            
        # If the chosen node has 0 available colors (checked above, but for safety)
        if min_avail_count == 0:
            return False
        
        # Try to color node best_u
        # If only 1 available color, we must take it
        if min_avail_count == 1:
            c_bit = (best_avail & -best_avail).bit_length() - 1
            # Create new forbidden state
            new_forbidden = list(forbidden_state)
            
            # Update neighbors
            neighbors = adj[best_u] & mask
            while neighbors:
                n_bit = neighbors & -neighbors
                v = n_bit.bit_length() - 1
                neighbors ^= n_bit
                new_forbidden[v] |= (1 << c_bit)
            
            new_mask = mask ^ (1 << best_u)
            return can_color(new_mask, new_forbidden)
        
        else:
            # Try all available colors
            temp_avail = best_avail
            while temp_avail:
                c_bit = (temp_avail & -temp_avail).bit_length() - 1
                temp_avail ^= (1 << c_bit)
                
                new_forbidden = list(forbidden_state)
                neighbors = adj[best_u] & mask
                while neighbors:
                    n_bit = neighbors & -neighbors
                    v = n_bit.bit_length() - 1
                    neighbors ^= n_bit
                    new_forbidden[v] |= (1 << c_bit)
                
                new_mask = mask ^ (1 << best_u)
                if can_color(new_mask, new_forbidden):
                    return True
            
            return False

    # Main loop to determine colors s_1, s_2, ..., s_n lexicographically
    for u in range(1, n + 1):
        found_c = False
        # Try colors 1, 2, 3
        for c in range(1, 4):
            # Check if c is valid for u given already colored neighbors (1..u-1)
            # The forbidden[u] already contains constraints from 1..u-1
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Tentatively assign color c to u
            # We need to check if the rest (u+1..n) can be colored
            # Prepare the forbidden state for the suffix
            
            # Current forbidden array includes constraints from 1..u-1
            # We need to add constraints from u to u+1..n
            
            # Calculate mask for nodes u+1 to n
            # Nodes are 1-indexed, so bit i corresponds to node i
            mask_suffix = ((1 << (n + 1)) - (1 << (u + 1)))
            
            # Create a copy of forbidden state to update
            new_forbidden = list(forbidden)
            
            # Update constraints for neighbors > u
            neighbors_future = adj[u] & mask_suffix
            while neighbors_future:
                n_bit = neighbors_future & -neighbors_future
                v = n_bit.bit_length() - 1
                neighbors_future ^= n_bit
                new_forbidden[v] |= (1 << (c - 1))
            
            # Check if suffix is solvable
            if can_color(mask_suffix, new_forbidden):
                colors[u] = c
                forbidden = new_forbidden # Commit the state
                found_c = True
                break
            else:
                # Backtrack: try next color, forbidden remains unchanged
                pass
        
        if not found_c:
            print("NO")
            return

    # If we successfully assigned all nodes
    print("YES")
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()