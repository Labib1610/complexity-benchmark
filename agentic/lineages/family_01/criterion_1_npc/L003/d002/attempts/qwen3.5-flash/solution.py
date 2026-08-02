import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
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

    # Build adjacency list
    # Nodes are 1-indexed
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # rem_colors[i] stores a bitmask of available colors for module i.
    # Colors 1, 2, 3 correspond to bits 0, 1, 2.
    # Initially, all colors are available (binary 111 = 7).
    rem_colors = [7] * (n + 1)
    
    # To store the assignment result
    assignment = [0] * (n + 1)
    
    # Recursive backtracking function
    # idx: Current module index we are trying to assign (1 to n)
    # current_rem_colors: Bitmask of available colors for unassigned modules based on assignments 1..idx-1
    def backtrack(idx, current_rem_colors):
        if idx > n:
            # All modules assigned successfully
            return True
        
        # Try assigning colors 1, 2, 3 in increasing order to ensure lexicographically smallest solution
        for color in range(1, 4):
            # Check if the color is available for the current module 'idx'
            # This is determined by the constraints from already assigned neighbors (1..idx-1)
            if not (current_rem_colors[idx] & (1 << (color - 1))):
                continue
            
            # Forward Checking: Determine if assigning 'color' to 'idx' leaves any future module (neighbor > idx) with no valid colors
            # We create a copy of the state to pass to the next recursion level
            next_rem_colors = list(current_rem_colors)
            valid = True
            
            for neighbor in adj[idx]:
                if neighbor > idx:
                    # Remove the chosen color from the neighbor's available colors
                    next_rem_colors[neighbor] &= ~(1 << (color - 1))
                    # If the neighbor's available colors become empty, this assignment is invalid
                    if next_rem_colors[neighbor] == 0:
                        valid = False
                        break
            
            if valid:
                assignment[idx] = color
                if backtrack(idx + 1, next_rem_colors):
                    return True
                # If the recursive call returns False, we backtrack and try the next color.
                # We don't need to explicitly undo changes because next_rem_colors is local to this iteration.
        
        return False

    if backtrack(1, rem_colors):
        print("YES")
        # Print the assignment sequence s_1 ... s_n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()