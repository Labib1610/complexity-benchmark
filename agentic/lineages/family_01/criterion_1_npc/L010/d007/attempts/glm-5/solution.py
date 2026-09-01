import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # Precompute neighbors for each node
    neighbors = []
    for i in range(n):
        nb = []
        for j in range(n):
            if adj[i][j]:
                nb.append(j)
        neighbors.append(nb)
    
    # We need to find a lexicographically smallest assignment f[0..n-1] in {1,2,3}
    # such that for all colors c in {0,1,2}, no two adjacent nodes have color c.
    # This is equivalent to 3-coloring the complement graph.
    
    # Backtracking with pruning
    # We assign colors to nodes 0, 1, ..., n-1 in order.
    # For each node i, we try colors 0, 1, 2 in order (corresponding to multipliers 1, 2, 3).
    # We maintain for each node the set of available colors.
    # Since we want lexicographically smallest, we try colors in order 0, 1, 2.
    
    # To speed up, we can use forward checking or constraint propagation.
    # But for n <= 40, basic backtracking might be too slow without heuristics.
    # Let's use a simple heuristic: MRV (Minimum Remaining Values) - choose the node with fewest remaining colors.
    # But since we need lexicographically smallest, we must assign in order 0, 1, ..., n-1.
    # So we cannot reorder nodes. We can only prune.
    
    # Let's use a simple recursive function with pruning.
    # We maintain an array `color` where color[i] is the assigned color (0, 1, 2) or -1 if unassigned.
    # We also maintain for each node a bitmask of forbidden colors due to assigned neighbors.
    
    color = [-1] * n
    # forbidden[i] will be a bitmask of colors that node i cannot take due to assigned neighbors.
    # Initially 0.
    forbidden = [0] * n
    
    # We'll use recursion with backtracking
    # To make it faster, we can use a stack instead of recursion to avoid Python recursion limit and overhead.
    # But let's try recursion first with pruning.
    
    # We can also use bit operations for speed.
    # Colors are 0, 1, 2. Bitmask: bit 0 = color 0, bit 1 = color 1, bit 2 = color 2.
    # forbidden[i] has bits set for colors that are forbidden.
    
    # We'll use a recursive function that assigns color to node i.
    # Before assigning, we check if any color is available.
    # If not, we backtrack.
    
    # To make it faster, we can use a heuristic: if a node has only one available color, assign it immediately.
    # But since we need lexicographically smallest, we must assign in order.
    # So we can't use that heuristic directly.
    
    # Let's try a simple recursive function with pruning.
    
    # We'll use a list to store the solution.
    solution = None
    
    # We'll use a recursive function with early termination.
    # To speed up, we can use a global flag to stop when solution is found.
    # But since we need lexicographically smallest, we can't stop early.
    # We must explore all possibilities in order.
    
    # Let's use a recursive function that returns True if a solution is found.
    # We'll use a global variable to store the first solution found.
    
    # Since we try colors in order 0, 1, 2, the first solution found will be lexicographically smallest.
    
    # We'll use a recursive function with pruning.
    
    # To make it faster, we can use a heuristic: if a node has no available colors, backtrack immediately.
    
    # Let's implement the recursive function.
    
    # We'll use a closure to capture the variables.
    
    found = False
    
    def backtrack(i):
        nonlocal found, solution
        if found:
            return
        if i == n:
            # All nodes assigned
            found = True
            solution = color[:]
            return
        
        # Try colors 0, 1, 2 in order
        for c in range(3):
            if (forbidden[i] >> c) & 1:
                continue  # color c is forbidden
            
            # Assign color c to node i
            color[i] = c
            
            # Update forbidden for neighbors
            # We need to save the old forbidden values to restore on backtrack
            saved_forbidden = []
            for j in neighbors[i]:
                if color[j] == -1:  # only update unassigned neighbors
                    saved_forbidden.append((j, forbidden[j]))
                    forbidden[j] |= (1 << c)
            
            # Check if any neighbor has no available colors
            valid = True
            for j in neighbors[i]:
                if color[j] == -1:
                    # Check if all colors are forbidden
                    if forbidden[j] == 0b111:
                        valid = False
                        break
            
            if valid:
                backtrack(i + 1)
                if found:
                    return
            
            # Restore forbidden for neighbors
            for j, old_val in saved_forbidden:
                forbidden[j] = old_val
            
            # Unassign color
            color[i] = -1
        
        # No color worked
        return
    
    backtrack(0)
    
    if found:
        print("YES")
        # Convert colors to multipliers (1, 2, 3)
        multipliers = [c + 1 for c in solution]
        print(" ".join(map(str, multipliers)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()