import sys

# Increase recursion depth to accommodate the recursive calls, 
# although for N=40 the default limit is usually sufficient.
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list to store the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Precompute neighbors with index > u to optimize the forward checking step.
    # This allows us to only check constraints on unassigned vertices.
    greater_neighbors = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                greater_neighbors[u].append(v)

    # avail[i] is a bitmask of available colors for person i.
    # Colors: 1 -> bit 0, 2 -> bit 1, 3 -> bit 2.
    # Initially all colors available: 111 binary -> 7.
    avail = [7] * (n + 1)
    assignment = [0] * (n + 1)

    def backtrack(u):
        # If we have assigned all personnel, we found a valid assignment
        if u > n:
            return True
        
        # Optimization: if no colors are available for u, this path is invalid
        if avail[u] == 0:
            return False

        # Try colors 1, 2, 3 in order to ensure lexicographically smallest assignment
        for c in range(1, 4):
            # Check if color c is available for u (conflict with assigned neighbors < u)
            if not ((avail[u] >> (c - 1)) & 1):
                continue
            
            # Forward checking: Check if assigning c to u makes any neighbor v > u impossible.
            # (i.e., avail[v] becomes 0 after blocking color c)
            blocked = False
            for v in greater_neighbors[u]:
                # If c is already blocked for v, no change in avail[v]
                # If c is NOT blocked, we check if it becomes blocked
                if not ((avail[v] >> (c - 1)) & 1):
                    # If adding this bit makes avail[v] 0
                    if (avail[v] & ~(1 << (c - 1))) == 0:
                        blocked = True
                        break
            
            if blocked:
                continue
            
            # If valid, apply changes and recurse
            # Apply changes
            changed_nodes = []
            for v in greater_neighbors[u]:
                if not ((avail[v] >> (c - 1)) & 1):
                    avail[v] &= ~(1 << (c - 1))
                    changed_nodes.append(v)
            
            assignment[u] = c
            
            if backtrack(u + 1):
                return True
            
            # Backtrack: Undo changes
            assignment[u] = 0
            for v in changed_nodes:
                avail[v] |= (1 << (c - 1))
        
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()