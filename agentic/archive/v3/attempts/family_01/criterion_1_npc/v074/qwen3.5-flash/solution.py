import sys

# Increase recursion depth to accommodate the recursion for N=40
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

    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # s[i] stores the slot assigned to operator i
    s = [0] * (n + 1)
    # used_mask[i] stores a bitmask of colors forbidden for operator i by already assigned neighbors
    # Bit k (0-indexed) is set if color k+1 is used by a neighbor
    used_mask = [0] * (n + 1)

    # Depth First Search to find the lexicographically smallest valid assignment
    def dfs(idx):
        # Base case: all operators assigned
        if idx > n:
            return True

        # Try assigning slots 1, 2, 3 in order for lexicographical minimality
        for c in range(1, 4):
            # Check if color c is valid for current operator idx
            # A color is invalid if any already assigned neighbor uses it
            # Since we iterate 1..n, neighbors < idx are already assigned
            if (used_mask[idx] >> (c - 1)) & 1:
                continue
            
            # Tentatively assign color c
            s[idx] = c
            
            # Forward Checking:
            # Update the forbidden masks for unassigned neighbors (> idx)
            # and check if any unassigned neighbor becomes impossible to color (mask == 7)
            changes = []
            valid_forward = True
            
            for neighbor in adj[idx]:
                if neighbor > idx:
                    old_mask = used_mask[neighbor]
                    new_mask = old_mask | (1 << (c - 1))
                    
                    # If all 3 colors are forbidden for this neighbor, this path is invalid
                    if new_mask == 7: # 111 in binary
                        valid_forward = False
                        break
                    
                    used_mask[neighbor] = new_mask
                    changes.append((neighbor, old_mask))
            
            if valid_forward:
                if dfs(idx + 1):
                    return True
            
            # Backtrack: restore state
            for neighbor, old_mask in changes:
                used_mask[neighbor] = old_mask
            s[idx] = 0
            
        return False

    # Start DFS from the first operator
    if dfs(1):
        print("YES")
        # Print the assignment for operators 1 to n
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()