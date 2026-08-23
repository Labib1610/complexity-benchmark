import sys

# Increase recursion depth to handle N=40 safely
sys.setrecursionlimit(5000)

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

    # masks[i] stores the bitmask of available colors for node i
    # Bit 0 represents color 1, Bit 1 represents color 2, Bit 2 represents color 3
    # Initially all colors are available (binary 111 = 7)
    masks = [7] * (n + 1)
    
    # colors[i] stores the assigned color for node i (0 if unassigned)
    colors = [0] * (n + 1)
    
    # We need to find the lexicographically smallest assignment.
    # We iterate chambers 1 to n. For each chamber, we try colors 1, 2, 3 in order.
    
    def backtrack(idx):
        if idx > n:
            return True
        
        # Try colors 1, 2, 3
        for c in range(1, 4):
            # Check conflict with already assigned neighbors
            # Neighbors with colors[v] != 0 are already assigned (since we process 1..n)
            conflict = False
            for v in adj[idx]:
                if colors[v] != 0 and colors[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            
            # Forward checking for unassigned neighbors
            # Unassigned neighbors have colors[v] == 0.
            # Since we process in order 1..n, these must be > idx.
            
            possible = True
            changes = []
            
            for v in adj[idx]:
                if colors[v] == 0:
                    # v is unassigned
                    old_mask = masks[v]
                    # Remove color c from available colors for v
                    new_mask = old_mask & ~(1 << (c - 1))
                    masks[v] = new_mask
                    
                    if new_mask == 0:
                        possible = False
                        # We need to revert the changes made to masks to restore state
                        for u, old_m in changes:
                            masks[u] = old_m
                        break
                    
                    changes.append((v, old_mask))
            
            if not possible:
                continue
            
            # Assign color c to node idx
            colors[idx] = c
            
            # Recurse
            if backtrack(idx + 1):
                return True
            
            # Backtrack: unassign node idx and restore masks
            colors[idx] = 0
            for v, old_mask in changes:
                masks[v] = old_mask
                
        return False

    if backtrack(1):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()