import sys

# Increase recursion depth to handle up to N=40 safely, though default is usually sufficient.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        # Ensure no duplicates in adjacency list for efficiency
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    # Precompute neighbors greater than u for forward checking optimization
    adj_greater = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                adj_greater[u].append(v)

    # colors[i] stores the assigned color for person i (0 if unassigned)
    # We use 1-based indexing for convenience
    colors = [0] * (n + 1)
    
    # possible[i] is a bitmask of available colors for node i
    # Colors 1, 2, 3 correspond to bits 0, 1, 2 (values 1, 2, 4)
    # Initially all colors are available (111 binary = 7)
    possible = [7] * (n + 1)
    
    def dfs(u):
        # If we have assigned colors for all n personnel, we found a solution
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is available for u
            # (possible[u] >> (c-1)) & 1 checks if the (c-1)-th bit is set
            if not ((possible[u] >> (c - 1)) & 1):
                continue
            
            # Tentative assignment: check if assigning c to u makes any future node uncolorable
            modified = []
            valid_step = True
            bit = 1 << (c - 1)
            
            for v in adj_greater[u]:
                # If color c is available for v, we must remove it
                if possible[v] & bit:
                    # If c is the only available color for v, removing it makes v uncolorable
                    if possible[v] == bit:
                        valid_step = False
                        break
                    else:
                        # Record the change to restore later
                        modified.append((v, bit))
                        possible[v] &= ~bit
            
            if not valid_step:
                # This color c for u is invalid because it leaves a neighbor with no options
                continue
            
            # Assign color c to u
            colors[u] = c
            
            # Recurse to the next node
            if dfs(u + 1):
                return True
            
            # Backtrack: unassign color c
            colors[u] = 0
            
            # Restore possible sets for neighbors
            for v, bit in modified:
                possible[v] |= bit
                
        return False

    # Start the backtracking search from node 1
    if dfs(1):
        print("YES")
        # Print the assigned colors for nodes 1 to n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()