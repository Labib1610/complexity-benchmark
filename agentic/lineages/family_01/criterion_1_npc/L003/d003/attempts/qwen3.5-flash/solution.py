import sys

# Increase recursion depth to handle up to N=40 comfortably, 
# though default 1000 is sufficient for depth 40.
sys.setrecursionlimit(2000)

def main():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency lists split into before (u < v) and after (u > v)
    # Since we process modules 1 to n, 'before' neighbors are already assigned,
    # and 'after' neighbors are unassigned.
    adj_before = [[] for _ in range(n + 1)]
    adj_after = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        # Store edges in both directions
        if v < u:
            adj_before[u].append(v)
            adj_after[v].append(u)
        else:
            adj_before[v].append(u)
            adj_after[u].append(v)

    # colors[i] stores the phase assigned to module i (0 if unassigned)
    colors = [0] * (n + 1)
    
    # available[i] is a bitmask of allowed colors for module i
    # Bits 1, 2, 3 correspond to colors 1, 2, 3.
    # Initial state: all colors allowed (binary 1110 = 14)
    # We use 1-based indexing for colors in bitmasks: (1<<c)
    available = [14] * (n + 1)
    
    # Helper function for DFS
    def dfs(u):
        if u > n:
            return True
        
        # Try phases 1, 2, 3 in order to satisfy lexicographical requirement
        for c in (1, 2, 3):
            # Check conflicts with already assigned neighbors (before)
            conflict = False
            for v in adj_before[u]:
                if colors[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            
            # If no conflict, tentatively assign c
            # Perform forward checking: update available colors for unassigned neighbors (after)
            changes = []
            possible = True
            
            for v in adj_after[u]:
                # Remove color c from available colors for v
                old_val = available[v]
                new_val = available[v] & ~(1 << c)
                available[v] = new_val
                changes.append((v, old_val))
                
                # If a neighbor has no available colors, this path is invalid
                if new_val == 0:
                    possible = False
                    break
            
            if possible:
                colors[u] = c
                if dfs(u + 1):
                    return True
                # Backtrack: reset color
                colors[u] = 0
            
            # Restore available colors
            for v, old_val in changes:
                available[v] = old_val
                
        return False

    # Start DFS from module 1
    if dfs(1):
        print("YES")
        # Print phases for modules 1 to n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    main()