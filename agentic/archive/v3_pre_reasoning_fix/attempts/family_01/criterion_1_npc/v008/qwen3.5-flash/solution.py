import sys

# Increase recursion depth to handle N=40
sys.setrecursionlimit(10000)

def solve():
    # Read all input from stdin
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

    # Remove duplicates to avoid redundant checks
    for i in range(1, n + 1):
        adj[i] = list(set(adj[i]))

    # Precompute neighbors greater than u for each u
    # This helps in forward checking
    adj_greater = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                adj_greater[u].append(v)

    s = [0] * (n + 1)
    used_masks = [0] * (n + 1)

    # Backtracking function
    def backtrack(u):
        if u > n:
            return True

        # Try colors 1, 2, 3 in order for lexicographically smallest sequence
        for c in [1, 2, 3]:
            # Check conflict with already assigned neighbors (< u)
            conflict = False
            for v in adj[u]:
                if v < u and s[v] == c:
                    conflict = True
                    break
            if conflict:
                continue

            # Forward checking: check if assigning c blocks any neighbor v > u
            # A neighbor v is blocked if it has neighbors with all 3 colors assigned.
            # used_masks[v] stores the colors used by assigned neighbors (< u).
            # Map color c to bit (c-1).
            # If we assign c to u, the new set of used colors for v is used_masks[v] | (1 << (c-1)).
            # If this equals 7 (binary 111), v is blocked.
            
            possible = True
            for v in adj_greater[u]:
                if (used_masks[v] | (1 << (c - 1))) == 7:
                    possible = False
                    break
            
            if possible:
                # Record old masks to restore later
                old_masks = []
                for v in adj_greater[u]:
                    old_masks.append((v, used_masks[v]))
                    used_masks[v] |= (1 << (c - 1))
                
                s[u] = c
                if backtrack(u + 1):
                    return True
                
                # Backtrack: restore state
                s[u] = 0
                for v, old_val in old_masks:
                    used_masks[v] = old_val
        
        return False

    if backtrack(1):
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()