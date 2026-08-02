import sys

# Increase recursion depth to handle potential deep recursion trees
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

    # Build adjacency structure for forward checking
    # neighbors_greater[u] contains v such that u is connected to v and v > u
    # This allows us to update allowed colors for unassigned neighbors efficiently
    neighbors_greater = [[] for _ in range(n + 1)]

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            neighbors_greater[u].append(v)
        else:
            neighbors_greater[v].append(u)
    
    # Deduplicate neighbors to avoid redundant updates
    for i in range(1, n + 1):
        neighbors_greater[i] = list(set(neighbors_greater[i]))

    # allowed[u] is a bitmask of allowed colors for unit u
    # Bits: 0 -> color 1, 1 -> color 2, 2 -> color 3
    # Initially all colors are allowed (111 binary = 7)
    allowed = [7] * (n + 1)
    
    # result[u] stores the chosen color for unit u
    result = [0] * (n + 1)

    def backtrack(u):
        # If we have assigned colors for all units, we found a solution
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to satisfy lexicographical requirement
        for c in [1, 2, 3]:
            # Check if color c is allowed for u
            # This check implicitly validates against already assigned neighbors (w < u)
            # because allowed[u] was updated by those neighbors during their processing.
            if not (allowed[u] & (1 << (c - 1))):
                continue
            
            # Assign color c to u
            result[u] = c
            
            # Forward checking: update allowed colors for unassigned neighbors (v > u)
            # We need to revert these changes if this branch fails, so we track them.
            updated = []
            possible = True
            mask = 1 << (c - 1)
            
            for v in neighbors_greater[u]:
                allowed[v] &= ~mask
                updated.append(v)
                if allowed[v] == 0:
                    possible = False
                    break
            
            if possible:
                if backtrack(u + 1):
                    return True
                # Backtrack: restore allowed colors
                # Note: We must revert even if backtrack returned False
                for v in updated:
                    allowed[v] |= mask
            else:
                # Pruning: valid colors exhausted for some neighbor
                # Revert changes
                for v in updated:
                    allowed[v] |= mask
        
        # If no color works for u, backtrack
        return False

    if backtrack(1):
        print("YES")
        print(*(result[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()