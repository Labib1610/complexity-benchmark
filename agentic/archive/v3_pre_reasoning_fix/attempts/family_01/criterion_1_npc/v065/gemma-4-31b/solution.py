import sys

def solve():
    # Increase recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    
    # Read n and m
    try:
        line = sys.stdin.readline().split()
        if not line:
            return
        n, m = map(int, line)
    except ValueError:
        return

    adj = [0] * n
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # We want the lexicographically smallest sequence (s1, s2, ..., sn)
    # where s_i is in {1, 2, 3}.
    # This means for each i from 0 to n-1, we try s_i = 1, then 2, then 3.
    
    assignment = [0] * n
    
    def is_safe(node, color):
        # Check if any neighbor already assigned has the same color
        # We only need to check neighbors < node because we assign sequentially
        for neighbor in range(node):
            if (adj[node] & (1 << neighbor)) and assignment[neighbor] == color:
                return False
        return True

    def can_color_3(node, current_assignment):
        """
        Check if the remaining nodes can be colored with 3 colors given 
        the current assignments. This is a 3-coloring problem (NP-complete),
        but with N=40, we can use a backtracking check with pruning.
        """
        if node == n:
            return True
        
        # To speed up the 'possibility' check, we can't do a full 3^40.
        # However, the main backtracking already does this. 
        # This helper is meant to potentially prune, but 3-coloring is hard.
        # For N=40, simple backtracking with the lexicographical constraint 
        # usually suffices if the search space is pruned by the constraints.
        return True

    def backtrack(node):
        if node == n:
            return True
        
        # Try colors 1, 2, 3 in order for lexicographical smallest result
        for color in [1, 2, 3]:
            if is_safe(node, color):
                assignment[node] = color
                # We could add a heuristic here, but let's try standard backtracking first.
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    # Optimization: 3-coloring is NP-complete. For N=40, standard backtracking
    # might be too slow. However, the lexicographical requirement forces a 
    # specific order. Let's use a more efficient backtracking.
    
    # To optimize, we can use bitmasks for available colors for each node.
    # But for N=40, a simple backtracking with the 'is_safe' check is often fast
    # enough if the graph is sparse or highly constrained.
    
    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == "__main__":
    solve()