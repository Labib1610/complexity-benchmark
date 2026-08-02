import sys

# Increase recursion depth to handle deep recursion trees if necessary
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

    # Build adjacency list for the graph
    # Using 1-based indexing for cores
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # assignment[i] stores the bus assigned to core i (1-indexed)
    assignment = [0] * (n + 1)
    
    # forbidden[v] is a bitmask representing the colors used by neighbors of v
    # that have already been assigned.
    # Bit 0 represents color 1, Bit 1 represents color 2, Bit 2 represents color 3.
    # We only care about neighbors v < u when we are at step u.
    forbidden = [0] * (n + 1)

    def backtrack(u):
        # If we have successfully assigned all cores
        if u > n:
            return True
        
        # If all 3 colors are forbidden for the current core u, then this path is invalid.
        # forbidden[u] contains colors of neighbors v < u.
        # If forbidden[u] == 7 (binary 111), no color is valid.
        if forbidden[u] == 7:
            return False

        # Try assigning colors 1, 2, 3 in increasing order to ensure lexicographically smallest result
        for c in range(1, 4):
            # Check if color c is valid with respect to already assigned neighbors (v < u)
            # If the corresponding bit is set in forbidden[u], it's invalid.
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            # Forward Checking (Lookahead):
            # Check if assigning color c to u will make any unassigned neighbor (v > u) impossible to color.
            # An unassigned neighbor v becomes impossible if all 3 colors are forbidden for it.
            # We update forbidden[v] temporarily for neighbors v > u and check.
            
            changes = []
            invalid_lookahead = False
            
            for v in adj[u]:
                if v > u:
                    mask_bit = 1 << (c - 1)
                    # If c is not already forbidden for v
                    if not (forbidden[v] & mask_bit):
                        old_mask = forbidden[v]
                        forbidden[v] |= mask_bit
                        changes.append((v, old_mask))
                        # If forbidden[v] becomes 111 (7), then v has no valid color
                        if forbidden[v] == 7:
                            invalid_lookahead = True
                            break
            
            if invalid_lookahead:
                # Restore the forbidden masks for neighbors and try next color
                for v, old_mask in changes:
                    forbidden[v] = old_mask
                continue
            
            # Assign color c to u
            assignment[u] = c
            
            # Recurse to the next core
            if backtrack(u + 1):
                return True
            
            # Backtrack: reset assignment
            assignment[u] = 0
            
            # Restore forbidden masks for neighbors v > u
            for v, old_mask in changes:
                forbidden[v] = old_mask
                
        return False

    # Start the backtracking process from core 1
    if backtrack(1):
        print("YES")
        # Print the assignment sequence s_1, s_2, ..., s_n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()