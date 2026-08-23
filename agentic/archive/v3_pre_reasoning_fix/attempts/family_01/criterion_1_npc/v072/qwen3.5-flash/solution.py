import sys

# Increase recursion depth to handle deep recursion trees if necessary
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

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Precompute right_adj: only neighbors with index > u
    # This helps in the backtracking step to only update future constraints
    # Since we process workers in order 1 to n, we only need to update constraints for workers > u
    right_adj = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                right_adj[u].append(v)

    # available[u] is a bitmask of available colors for worker u.
    # Bit 0 represents Color 1, Bit 1 represents Color 2, Bit 2 represents Color 3.
    # Initially, all colors are available (111 binary = 7).
    available = [7] * (n + 1)
    
    # To store the assignment
    assignment = [0] * (n + 1)

    # Backtracking function to find the lexicographically first valid assignment
    def backtrack(u):
        if u > n:
            return True
        
        # available[u] already reflects constraints from nodes 1 to u-1
        # We try to assign the smallest valid color (1, 2, or 3) to ensure lexicographically smallest result
        for c in (1, 2, 3):
            # Check if color c is available for u
            if (available[u] >> (c - 1)) & 1:
                # Assign color c to u
                assignment[u] = c
                
                # Update constraints for neighbors v > u
                modified_neighbors = []
                possible = True
                
                for v in right_adj[u]:
                    # Remove color c from v's available set
                    mask = 1 << (c - 1)
                    if (available[v] & mask):
                        available[v] &= ~mask
                        modified_neighbors.append(v)
                        # If any neighbor loses all colors, this path is invalid
                        if available[v] == 0:
                            possible = False
                            break
                
                if possible:
                    if backtrack(u + 1):
                        return True
                
                # Backtrack: restore available colors for neighbors
                for v in modified_neighbors:
                    mask = 1 << (c - 1)
                    available[v] |= mask
        
        return False

    if backtrack(1):
        print("YES")
        # Print the assignment for workers 1 to n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()