import sys

# Increase recursion depth to accommodate the depth of the recursion tree
sys.setrecursionlimit(5000)

def main():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Precompute neighbors_greater for Forward Checking optimization
    # neighbors_greater[u] contains all neighbors v of u such that v > u
    # This allows us to update domains of unassigned neighbors
    neighbors_greater = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                neighbors_greater[u].append(v)
    
    # Domains: bitmask of available colors for each node.
    # Initially all nodes can be 1, 2, or 3.
    # Represent colors as bits: 1 -> 1, 2 -> 2, 3 -> 4.
    # 7 is binary 111.
    domains = [7] * (n + 1)
    
    # Assignment: stores the chosen color mask for each node.
    assignment = [0] * (n + 1)
    
    # Recursive backtracking function with Forward Checking
    def backtrack(u):
        # Base case: if all nodes assigned successfully
        if u > n:
            return True
        
        # Pruning: if no color is available for current node u
        # domains[u] is updated by neighbors v < u during their processing
        if domains[u] == 0:
            return False
        
        # Try to assign a color to node u
        # We try colors in order 1, 2, 3 (masks 1, 2, 4) to ensure lexicographically smallest
        # sequence s_1, s_2, ..., s_n
        for color_mask in (1, 2, 4):
            # Check if color_mask is available for u
            # This implicitly checks constraints from already assigned neighbors (v < u)
            if (domains[u] & color_mask) == 0:
                continue
            
            # Forward Checking:
            # Update domains of neighbors v > u to remove the current color
            changes = []
            possible = True
            
            for v in neighbors_greater[u]:
                old_domain = domains[v]
                # If color is already forbidden for v, no change needed
                if (old_domain & color_mask) == 0:
                    continue
                
                new_domain = old_domain & ~color_mask
                domains[v] = new_domain
                
                if new_domain == 0:
                    possible = False
                    # Revert the change for v immediately
                    domains[v] = old_domain
                    break
                
                changes.append((v, old_domain))
            
            if not possible:
                # If any neighbor's domain became empty, this color is invalid for u
                # Revert all changes made in this iteration
                for v, old_domain in changes:
                    domains[v] = old_domain
                continue
            
            # If valid, assign color and recurse
            assignment[u] = color_mask
            
            if backtrack(u + 1):
                return True
            
            # Backtrack: unassign and revert domains
            assignment[u] = 0
            for v, old_domain in changes:
                domains[v] = old_domain
        
        return False

    # Start backtracking from node 1
    if backtrack(1):
        print("YES")
        # Convert masks (1, 2, 4) to values (1, 2, 3)
        result = []
        for i in range(1, n + 1):
            val = assignment[i]
            if val == 1:
                result.append(1)
            elif val == 2:
                result.append(2)
            else:
                result.append(3)
        print(*(result))
    else:
        print("NO")

if __name__ == '__main__':
    main()