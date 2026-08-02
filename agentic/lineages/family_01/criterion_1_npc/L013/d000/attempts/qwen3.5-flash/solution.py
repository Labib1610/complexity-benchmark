import sys

# Increase recursion depth just in case
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

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # ans array to store colors (0, 1, 2)
    ans = [-1] * (n + 1)

    # Helper function to check if the remaining nodes (start to end) can be colored
    # given the current available colors (avail) and assigned nodes (assigned_mask).
    # assigned_mask has bit u set if node u is already colored.
    # avail[u] is a bitmask of available colors for node u.
    def can_color(start, end, assigned_mask, avail):
        # Base case: if start > end, all nodes in range are assigned
        if start > end:
            return True
        
        # Find the unassigned node with the minimum number of available colors (MRV heuristic)
        min_colors = 4
        best_u = -1
        
        # Iterate over the range [start, end]
        # Since N is small (<= 40), linear scan is efficient enough
        for u in range(start, end + 1):
            if not ((assigned_mask >> u) & 1):
                # Count available colors
                # avail[u] is a bitmask. We can use bin().count() or precomputed
                # But bin().count() is fast for small integers
                cnt = bin(avail[u]).count('1')
                if cnt < min_colors:
                    min_colors = cnt
                    best_u = u
                    if min_colors == 0:
                        break
        
        if best_u == -1:
            return True # All nodes in range are assigned
        
        if min_colors == 0:
            return False # No valid color for the most constrained node
        
        # Try each available color for best_u
        # We iterate colors 0, 1, 2
        for c in range(3):
            if (avail[best_u] >> c) & 1:
                # If color c is available
                # Create new state
                new_assigned = assigned_mask | (1 << best_u)
                new_avail = avail[:] # Copy list
                
                # Update neighbors in the range [start, end]
                # Neighbors outside range are either fixed (handled during avail init) or irrelevant
                for v in adj[best_u]:
                    if start <= v <= end:
                        # If v is not assigned yet (it shouldn't be if we are backtracking correctly, 
                        # but check just in case)
                        if not ((new_assigned >> v) & 1):
                            new_avail[v] &= ~(1 << c)
                
                if can_color(start, end, new_assigned, new_avail):
                    return True
        
        return False

    # Main loop to determine the lexicographically first valid assignment
    for i in range(1, n + 1):
        found_c = False
        for c in range(3): # Try colors 0, 1, 2
            # Check if c conflicts with already assigned neighbors (1 to i-1)
            conflict = False
            for v in adj[i]:
                if v < i:
                    if ans[v] == c:
                        conflict = True
                        break
            if conflict:
                continue
            
            # Tentatively assign c to ans[i] (conceptually)
            # But we need to check if the rest of the graph (i+1 to n) can be colored
            
            # Prepare available masks for nodes i+1 to n
            # These masks are based on constraints from ans[1...i]
            avail = [0] * (n + 1)
            
            # Initialize avail for 1...i (not used in check but good for completeness)
            # Actually we only need avail for i+1...n
            # But to be safe and consistent, let's fill all.
            # However, check only accesses i+1...n.
            
            # We can initialize avail for i+1...n
            # But we need to compute it based on ans[1...i]
            # Note: ans[i] is currently c. ans[1...i-1] are fixed.
            
            # Optimization: We can just compute avail for i+1...n
            for u in range(i + 1, n + 1):
                mask = 7 # 111 binary, all colors available
                for v in adj[u]:
                    if v <= i:
                        # Neighbor is already assigned
                        # Subtract its color
                        # ans[v] is 0, 1, 2
                        mask &= ~(1 << ans[v])
                avail[u] = mask
            
            # Initial assigned mask for check should include 1...i
            # Since check is for i+1...n, nodes 1...i are considered assigned
            assigned_mask = 0
            for v in range(1, i + 1):
                assigned_mask |= (1 << v)
            
            # Check feasibility
            if can_color(i + 1, n, assigned_mask, avail):
                ans[i] = c
                found_c = True
                break
        
        if not found_c:
            print("NO")
            return

    print("YES")
    # Output ans[1...n] converted to 1, 2, 3
    print(" ".join(str(x + 1) for x in ans[1:]))

if __name__ == '__main__':
    solve()