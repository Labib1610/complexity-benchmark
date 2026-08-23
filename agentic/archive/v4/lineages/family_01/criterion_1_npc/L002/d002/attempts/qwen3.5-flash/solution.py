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

    # Adjacency list for the graph (1-based indexing)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # colors[i] stores the vault assigned to material i (1, 2, or 3)
    colors = [0] * (n + 1)
    # forbidden_masks[i] stores a bitmask of colors forbidden for material i
    # by already assigned neighbors. 
    # Bit 0 for color 1, Bit 1 for color 2, Bit 2 for color 3.
    # Mask 7 (111 binary) means all 3 colors are forbidden -> impossible to color i.
    # This is maintained for unassigned vertices based on assigned neighbors.
    forbidden_masks = [0] * (n + 1)

    # DFS to find the lexicographically smallest assignment
    # We assign vaults for materials 1 to n in order.
    def dfs(u):
        # If we have assigned all materials, we found a valid assignment
        if u > n:
            return True
        
        # If u is already impossible to color (all 3 colors forbidden by neighbors < u)
        # This check is crucial for pruning.
        if forbidden_masks[u] == 7:
            return False

        # Try colors 1, 2, 3 in order to ensure lexicographically smallest result
        for c in [1, 2, 3]:
            # Check if c is forbidden by already assigned neighbors (stored in forbidden_masks[u])
            # forbidden_masks[u] contains bits set for colors forbidden by neighbors < u
            if not (forbidden_masks[u] & (1 << (c - 1))):
                colors[u] = c
                
                # Propagate constraints to neighbors > u
                # We need to save state to revert during backtracking
                updates = []
                valid_branch = True
                
                for v in adj[u]:
                    if v > u:
                        old_mask = forbidden_masks[v]
                        forbidden_masks[v] |= (1 << (c - 1))
                        updates.append((v, old_mask))
                        
                        # If v now has all 3 colors forbidden, this branch is invalid
                        if forbidden_masks[v] == 7:
                            valid_branch = False
                            break
                
                if valid_branch:
                    if dfs(u + 1):
                        return True
                
                # Backtrack: revert changes
                colors[u] = 0
                for v, old_mask in updates:
                    forbidden_masks[v] = old_mask
        
        return False

    # Start DFS from material 1
    if dfs(1):
        print("YES")
        # Output s_1 ... s_n
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()