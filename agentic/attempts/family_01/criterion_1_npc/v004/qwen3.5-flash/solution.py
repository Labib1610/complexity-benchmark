import sys

# Increase recursion depth to accommodate N=40 comfortably
sys.setrecursionlimit(2000)

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
    # Using 1-based indexing for workers
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # mask[i] will store the bitmask of allowed shifts for worker i
    # Bit 0 -> Shift 1, Bit 1 -> Shift 2, Bit 2 -> Shift 3
    # Initially, all shifts are allowed (1 | 2 | 4 = 7)
    mask = [7] * (n + 1)
    
    # s[i] will store the assigned shift for worker i
    s = [0] * (n + 1)
    
    # Backtracking function with forward checking
    # Tries to assign a shift to worker u, then recurses to u+1
    # Ensures lexicographically smallest sequence by trying shifts 1, 2, 3 in order
    def dfs(u):
        # Base case: all workers have been assigned a shift
        if u > n:
            return True
        
        # Try shifts 1, 2, 3 in increasing order
        for c in range(1, 4):
            # Check if shift c is compatible with already assigned workers (1 to u-1)
            # This information is maintained in mask[u] by previous steps
            if (mask[u] >> (c - 1)) & 1:
                # Tentatively assign shift c to worker u
                # We need to update the allowed shifts for future workers (v > u)
                changes = []
                possible = True
                
                for v in adj[u]:
                    if v > u:
                        # Save current mask to restore later
                        old_mask = mask[v]
                        # Remove shift c from allowed shifts for v
                        mask[v] &= ~(1 << (c - 1))
                        changes.append((v, old_mask))
                        
                        # Forward checking: if v has no allowed shifts left, this path is invalid
                        if mask[v] == 0:
                            possible = False
                            break
                
                if possible:
                    s[u] = c
                    # Recurse to the next worker
                    if dfs(u + 1):
                        return True
                    
                    # Backtrack: Restore s[u] and mask values
                    s[u] = 0
                    for v, old in changes:
                        mask[v] = old
                else:
                    # If this choice is invalid, restore mask changes made so far
                    for v, old in changes:
                        mask[v] = old
                        
        return False

    # Start the search from worker 1
    if dfs(1):
        print("YES")
        # Print shifts for workers 1 to n
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()