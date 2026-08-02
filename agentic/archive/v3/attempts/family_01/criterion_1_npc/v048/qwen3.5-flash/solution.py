import sys

# Increase recursion depth to accommodate deep search trees if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list using sets to avoid duplicate edges
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert sets to lists for faster iteration
    adj = [list(s) for s in adj]
    
    # color[i] stores the window assigned to staff i (1, 2, or 3)
    color = [0] * (n + 1)
    
    # valid[i] stores a bitmask of allowed colors for staff i
    # 1 (binary 001) -> window 1
    # 2 (binary 010) -> window 2
    # 4 (binary 100) -> window 3
    # Initial state: all colors allowed (7 = 111)
    valid = [7] * (n + 1)
    
    # We need to find the lexicographically smallest assignment.
    # We try to assign colors 1, 2, 3 in order for each staff member.
    # We use backtracking with forward checking (constraint propagation).
    
    def backtrack(u):
        # If we have assigned all staff, we found a solution
        if u > n:
            return True
        
        # Pruning: if no colors are valid for u based on constraints from 1..u-1,
        # this path is dead. valid[u] tracks allowed colors based on assigned neighbors.
        if valid[u] == 0:
            return False
        
        # Try colors 1, 2, 3 to find the lexicographically smallest solution
        for c in [1, 2, 3]:
            # Check if color c is allowed for u.
            # valid[u] contains colors not forbidden by assigned neighbors (v < u).
            if not (valid[u] & (1 << (c - 1))):
                continue
            
            # Assign color c to u
            color[u] = c
            
            # Forward checking: update valid colors for unassigned neighbors (v > u)
            # This helps prune the search space early by detecting conflicts sooner.
            mask_c = 1 << (c - 1)
            modified = []
            conflict = False
            
            for v in adj[u]:
                if v > u:
                    # If v has color c available, remove it
                    if valid[v] & mask_c:
                        valid[v] &= ~mask_c
                        modified.append(v)
                        # If v has no colors left, this assignment is invalid
                        if valid[v] == 0:
                            conflict = True
                            break
            
            if conflict:
                # Backtrack: revert valid colors changes
                for v in modified:
                    valid[v] |= mask_c
                color[u] = 0
                continue
            
            # Recurse to next staff member
            if backtrack(u + 1):
                return True
            
            # Backtrack: revert valid colors changes
            for v in modified:
                valid[v] |= mask_c
            color[u] = 0
        
        return False

    if backtrack(1):
        print("YES")
        # Print the assignment for staff 1 to n
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()