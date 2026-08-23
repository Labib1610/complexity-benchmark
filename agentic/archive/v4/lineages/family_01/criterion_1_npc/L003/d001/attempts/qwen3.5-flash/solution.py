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

    # adj_after[u] will store neighbors v where v > u
    # This optimization avoids checking v < u inside the recursion
    adj_after = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        if u < v:
            adj_after[u].append(v)
        else:
            adj_after[v].append(u)

    # dom[u] is a bitmask of available colors for device u
    # Bit 0 (value 1) -> Color 1
    # Bit 1 (value 2) -> Color 2
    # Bit 2 (value 4) -> Color 3
    # Initial state: all colors available (7 = 111 binary)
    dom = [7] * (n + 1)
    assignment = [0] * (n + 1)
    
    # Precompute inverse masks for removing colors efficiently
    # clear_masks[c] has 0 at the bit corresponding to color c
    # clear_masks[1] = ~1 (removes bit 0)
    # clear_masks[2] = ~2 (removes bit 1)
    # clear_masks[3] = ~4 (removes bit 2)
    clear_masks = [0, ~1, ~2, ~4]
    
    def backtrack(u):
        # If all devices are assigned, we found a valid solution
        if u > n:
            return True
        
        # Try assigning colors 1, 2, 3 in increasing order to ensure lexicographically smallest
        for c in range(1, 4):
            # Check if color c is available for u
            # dom[u] has already been filtered by neighbors < u (neighbors with index < u)
            if not (dom[u] & (1 << (c - 1))):
                continue
            
            # Tentatively assign color c to u
            assignment[u] = c
            changes = []
            possible = True
            
            # Propagate constraints to neighbors > u (neighbors with index > u)
            for v in adj_after[u]:
                old_dom_v = dom[v]
                # If v could take color c, remove it from its domain
                if old_dom_v & (1 << (c - 1)):
                    dom[v] &= clear_masks[c]
                    changes.append((v, old_dom_v))
                    # If v has no colors left, this choice is invalid (forward checking)
                    if dom[v] == 0:
                        possible = False
                        break
            
            if possible:
                # Recurse to next device
                if backtrack(u + 1):
                    return True
            
            # Backtrack: restore dom values of neighbors
            for v, old_dom_v in changes:
                dom[v] = old_dom_v
            
            # Unassign u
            assignment[u] = 0
        
        return False

    if backtrack(1):
        print("YES")
        # Print the assignment sequence s_1, s_2, ..., s_n
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()