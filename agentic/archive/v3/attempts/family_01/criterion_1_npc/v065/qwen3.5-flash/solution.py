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
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # s[i] stores the color assigned to reagent i (1, 2, or 3)
    s = [0] * (n + 1)
    
    # forbidden[i] is a bitmask representing forbidden colors for reagent i.
    # Bit 0 corresponds to color 1, Bit 1 to color 2, Bit 2 to color 3.
    # Initially 0 (no colors forbidden).
    forbidden = [0] * (n + 1)

    # Recursive function for backtracking with forward checking
    def backtrack(idx):
        # If we have successfully assigned colors to all reagents 1..n
        if idx > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest sequence
        for c in range(1, 4):
            # Check if color c is allowed for current reagent idx
            # (forbidden[idx] contains constraints from already colored neighbors)
            if (forbidden[idx] >> (c - 1)) & 1:
                continue
            
            # Tentatively assign color c to reagent idx
            s[idx] = c
            mask = 1 << (c - 1)
            
            # Forward checking: update forbidden colors for uncolored neighbors (v > idx)
            changes = []
            pruned = False
            
            for v in adj[idx]:
                if v > idx: # Only care about neighbors not yet colored
                    if not (forbidden[v] & mask):
                        forbidden[v] |= mask
                        changes.append(v)
                        # If all colors are forbidden for v (mask 7 = 111 binary), this path is invalid
                        if forbidden[v] == 7:
                            pruned = True
                            break
            
            if not pruned:
                # If not pruned, continue to next reagent
                if backtrack(idx + 1):
                    return True
            
            # Backtrack: undo the changes to forbidden array for neighbors
            for v in changes:
                forbidden[v] &= ~mask
        
        return False

    if backtrack(1):
        print("YES")
        # Print the assignment sequence for reagents 1 to n
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()