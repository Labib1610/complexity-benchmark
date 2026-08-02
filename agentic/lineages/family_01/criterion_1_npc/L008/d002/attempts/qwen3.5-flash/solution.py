import sys

# Increase recursion depth to handle N=40 safely
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

    # Adjacency list for the graph
    # We only store neighbors v such that v > u to optimize forward checking
    # This ensures that when we are at vertex u, we only update unassigned neighbors
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u > v:
            u, v = v, u
        adj[u].append(v)
    
    # allowed[v] is a bitmask representing the set of allowed colors for vertex v.
    # Bit 0 corresponds to color 1, bit 1 to color 2, bit 2 to color 3.
    # Initially, all colors are allowed (111 binary = 7).
    allowed = [7] * (n + 1)
    assignment = [0] * (n + 1)
    
    # Backtracking function to find the lexicographically smallest assignment
    def backtrack(idx):
        # If we have assigned all vertices, we found a solution
        if idx > n:
            return True
        
        u = idx
        # Try assigning colors 1, 2, 3 in increasing order to ensure lexicographical minimality
        for c in range(1, 4):
            # Check if color c is allowed for vertex u
            # This check ensures consistency with already assigned neighbors (v < u)
            # because allowed[u] has been updated by all v < u.
            if (allowed[u] >> (c - 1)) & 1:
                assignment[u] = c
                
                # Forward checking: update allowed colors for unassigned neighbors (v > u)
                valid = True
                modified = []
                
                for v in adj[u]:
                    # If v is already invalid (no allowed colors), this path is dead
                    if allowed[v] == 0:
                        valid = False
                        break
                    
                    # Remove color c from allowed set of v
                    if (allowed[v] >> (c - 1)) & 1:
                        allowed[v] &= ~(1 << (c - 1))
                        modified.append(v)
                        # If v's allowed set becomes empty, this path is dead
                        if allowed[v] == 0:
                            valid = False
                            break
                
                if valid:
                    # Recurse to the next vertex
                    if backtrack(idx + 1):
                        return True
                
                # Backtrack: restore allowed colors for neighbors that were modified
                for v in modified:
                    allowed[v] |= (1 << (c - 1))
                
                # Reset assignment for u
                assignment[u] = 0
        
        return False
    
    # Start the backtracking from the first vertex
    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()