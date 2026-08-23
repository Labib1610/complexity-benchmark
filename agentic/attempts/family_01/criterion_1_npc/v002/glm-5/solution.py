import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [0] * n
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Check if the graph is 3-colorable
    # We use a DP approach: dp[mask] = True if the subgraph induced by mask is 3-colorable
    # A subgraph is 3-colorable iff it can be partitioned into 3 independent sets
    # Equivalently, mask = I1 U I2 U I3 where Ij are disjoint independent sets
    # This is equivalent to mask being a subset of the union of 3 independent sets
    # Or simply: mask can be covered by 3 independent sets.
    # We precompute all independent sets.
    
    is_independent = [True] * (1 << n)
    # is_independent[mask] is True if mask is an independent set
    # We can compute this using DP: 
    # mask is independent if (mask & adj[lsb]) == 0 and mask ^ lsb is independent
    # Or simply iterate all masks and check.
    # Since n <= 40, 2^n is too large. 
    # Wait, the standard DP for chromatic number works for n <= 20 or so.
    # For n=40, we need a different approach.
    
    # However, the problem asks for 3-colorability.
    # We can use the recursive search with pruning (backtracking).
    # To find the lexicographically smallest valid assignment, we assign colors
    # to vertices 0, 1, ..., n-1 in order, trying colors 1, 2, 3.
    # This naturally finds the lexicographically smallest solution.
    # We need to prune efficiently.
    
    # Let's implement a backtracking search.
    # State: assigned colors for vertices 0..k-1.
    # Try to assign color to vertex k.
    # Colors are 1, 2, 3.
    
    assignment = [0] * n
    
    # Optimization: reorder vertices?
    # No, because we need lexicographically smallest assignment (s1, s2, ...).
    # So we must assign vertex 0 first, then 1, etc.
    
    # Simple backtracking might be slow for n=40 if the graph is sparse.
    # But for 3-coloring, it's often fast enough.
    # We can add basic forward checking.
    
    def backtrack(index):
        if index == n:
            return True
        
        u = index
        neighbors = adj[u]
        
        # Determine available colors
        # We iterate colors 1, 2, 3 to ensure lexicographically smallest
        for color in range(1, 4):
            conflict = False
            # Check neighbors with smaller indices (already assigned)
            # We only need to check v < u because v > u are not assigned yet
            # neighbors mask contains all neighbors.
            # We iterate through set bits in neighbors that are < index?
            # Actually, just checking assigned neighbors is enough.
            
            # Iterate neighbors v where v < u
            # (v > u are not assigned yet, so no conflict)
            n_mask = neighbors & ((1 << u) - 1)
            temp = n_mask
            while temp:
                v = (temp & -temp).bit_length() - 1
                temp &= temp - 1
                if assignment[v] == color:
                    conflict = True
                    break
            
            if not conflict:
                assignment[u] = color
                if backtrack(index + 1):
                    return True
                assignment[u] = 0 # backtrack
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()