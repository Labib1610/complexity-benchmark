import sys

# Increase recursion depth to handle deep recursion trees
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency bitmasks for the graph
    # adj[u] contains a bitmask of neighbors of u
    adj = [0] * n
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # s stores the color of each vertex (0, 1, 2)
    # 0 indicates uncolored.
    s = [0] * n
    
    # colored_masks[k] stores bitmask of vertices assigned color k
    # Colors are 0, 1, 2
    colored_masks = [0, 0, 0]
    
    # Function to check if the remaining uncolored vertices (given by mask) 
    # can be validly 3-colored given the current assignments.
    # This function uses MRV (Minimum Remaining Values) heuristic to speed up pruning.
    def check(mask):
        if mask == 0:
            return True
        
        min_colors = 4
        u_opt = -1
        
        # Iterate over set bits in mask to find the vertex with minimum valid colors
        temp_mask = mask
        while temp_mask:
            # Get lowest set bit
            lsb = temp_mask & -temp_mask
            # Get index (0-based)
            u = lsb.bit_length() - 1
            temp_mask ^= lsb
            
            # Count valid colors for u
            # A color c is valid if no neighbor of u has color c
            valid_c = 0
            if (adj[u] & colored_masks[0]) == 0:
                valid_c += 1
            if (adj[u] & colored_masks[1]) == 0:
                valid_c += 1
            if (adj[u] & colored_masks[2]) == 0:
                valid_c += 1
            
            if valid_c == 0:
                return False
            
            if valid_c < min_colors:
                min_colors = valid_c
                u_opt = u
                if min_colors == 1:
                    break
        
        # Try to assign a valid color to u_opt
        # We try colors 0, 1, 2. Order doesn't strictly matter for existence check,
        # but consistent ordering is good practice.
        for c in range(3):
            if (adj[u_opt] & colored_masks[c]) == 0:
                # Assign color c
                s[u_opt] = c
                colored_masks[c] |= (1 << u_opt)
                
                # Recursively check the rest
                if check(mask ^ (1 << u_opt)):
                    # If a valid completion exists, we return True.
                    # Crucially, we must restore the state so the caller sees clean state.
                    s[u_opt] = 0
                    colored_masks[c] ^= (1 << u_opt)
                    return True
                
                # Backtrack
                s[u_opt] = 0
                colored_masks[c] ^= (1 << u_opt)
                
        return False

    # Main DFS function to find the lexicographically smallest assignment
    # It iterates vertices 0 to n-1 in order.
    def main_dfs(u):
        if u == n:
            return True
        
        # Try colors 0, 1, 2 (corresponding to slots 1, 2, 3)
        # Trying in order ensures lexicographically smallest result
        for c in range(3):
            # Check if color c is valid for vertex u
            if (adj[u] & colored_masks[c]) == 0:
                # Assign color c
                s[u] = c
                colored_masks[c] |= (1 << u)
                
                # Check if the remaining vertices (u+1 to n-1) can be colored
                # mask contains all vertices from u+1 to n-1
                mask = ((1 << n) - 1) ^ ((1 << (u+1)) - 1)
                
                if check(mask):
                    return True
                
                # Backtrack
                s[u] = 0
                colored_masks[c] ^= (1 << u)
        
        return False

    # Start the search from vertex 0
    if main_dfs(0):
        print("YES")
        # Convert 0-based colors to 1-based slots
        print(" ".join(str(x + 1) for x in s))
    else:
        print("NO")

if __name__ == '__main__':
    solve()