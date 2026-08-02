import sys

# Increase recursion depth to handle deep recursion for N=40
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

    # used_masks[c] stores a bitmask of nodes colored with color c (c in 1, 2, 3)
    used_masks = [0] * 4
    
    # s stores the assignment for each task (1-indexed)
    s = [0] * (n + 1)
    
    # adj_masks[u] stores a bitmask of neighbors of u
    adj_masks = [0] * (n + 1)
    
    # adj_greater[u] stores a list of neighbors v of u such that v > u
    # This is used for forward checking
    adj_greater = [[] for _ in range(n + 1)]
    
    # Parse edges
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        
        # Update adjacency bitmasks
        adj_masks[u] |= (1 << (v - 1))
        adj_masks[v] |= (1 << (u - 1))
        
        # Update adjacency list for forward checking (only store v > u)
        if u < v:
            adj_greater[u].append(v)
        else:
            adj_greater[v].append(u)
            
    def backtrack(u):
        # Base case: all tasks assigned
        if u > n:
            return True
        
        # Try assigning colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check if color c is valid for task u
            # It is valid if no neighbor of u has been colored c
            if (adj_masks[u] & used_masks[c]) == 0:
                # Assign color c to task u
                used_masks[c] |= (1 << (u - 1))
                s[u] = c
                
                # Forward checking: check if this assignment leads to any uncolored neighbor having no valid colors
                valid_branch = True
                for v in adj_greater[u]:
                    # Check if node v has at least one valid color
                    # A color k is valid for v if no neighbor of v has color k
                    # Note: u is a neighbor of v and is colored c, so c is invalid for v
                    # We check if there exists any k in {1, 2, 3} such that (adj_masks[v] & used_masks[k]) == 0
                    
                    has_valid = False
                    for k in range(1, 4):
                        # If k == c, it's invalid because u is colored c and u is a neighbor of v
                        # However, the bitwise check handles this implicitly since adj_masks[v] contains u
                        if (adj_masks[v] & used_masks[k]) == 0:
                            has_valid = True
                            break
                    
                    if not has_valid:
                        # Node v cannot be colored, so this branch is invalid
                        valid_branch = False
                        break
                
                if valid_branch:
                    # Recurse to the next task
                    if backtrack(u + 1):
                        return True
                
                # Backtrack: remove assignment
                used_masks[c] &= ~(1 << (u - 1))
                s[u] = 0
        
        return False

    # Start backtracking from task 1
    if backtrack(1):
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()