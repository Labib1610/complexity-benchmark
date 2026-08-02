import sys

# Increase recursion depth to handle deep recursion if necessary
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

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Precompute neighbors < u and > u for faster processing
    prev_neighbors = [[] for _ in range(n + 1)]
    next_neighbors = [[] for _ in range(n + 1)]
    
    for u in range(1, n + 1):
        for v in adj[u]:
            if v < u:
                prev_neighbors[u].append(v)
            else:
                next_neighbors[u].append(v)

    # color[u] stores the assigned color (1, 2, 3) for worker u, 0 if unassigned
    color = [0] * (n + 1)
    # forbidden[u] is a bitmask of colors forbidden for worker u
    # bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    forbidden = [0] * (n + 1)
    # To store the result
    ans = [0] * (n + 1)
    
    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to find lexicographically smallest
        for c in range(1, 4):
            # Check compatibility with previous neighbors (already assigned)
            valid = True
            for v in prev_neighbors[u]:
                if color[v] == c:
                    valid = False
                    break
            if not valid:
                continue
            
            # Assign c to u
            color[u] = c
            ans[u] = c
            
            # Update forbidden states for next neighbors (unassigned)
            mask = 1 << (c - 1)
            changed_next = []
            conflict_found = False
            
            for v in next_neighbors[u]:
                old_val = forbidden[v]
                forbidden[v] |= mask
                if old_val != forbidden[v]:
                    changed_next.append(v)
                
                if forbidden[v] == 7: # All 3 colors forbidden
                    conflict_found = True
                    break
            
            if conflict_found:
                # Backtrack: revert changes
                for v in changed_next:
                    forbidden[v] &= ~mask
                color[u] = 0
                ans[u] = 0
                continue
            
            # Recurse
            if backtrack(u + 1):
                return True
            
            # Backtrack: revert changes
            for v in changed_next:
                forbidden[v] &= ~mask
            color[u] = 0
            ans[u] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(ans[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()