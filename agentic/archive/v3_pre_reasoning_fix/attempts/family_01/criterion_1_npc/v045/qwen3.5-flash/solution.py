import sys

# Increase recursion depth to handle depth N=40 safely
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

    # Adjacency list for graph
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # assignment stores the color (0, 1, 2) for each vertex
    assignment = [0] * n
    
    # forbidden_mask[i] stores a bitmask of colors forbidden for vertex i
    # Bit 0 set -> color 0 forbidden
    # Bit 1 set -> color 1 forbidden
    # Bit 2 set -> color 2 forbidden
    forbidden_mask = [0] * n
    
    def backtrack(u):
        # If we have assigned all vertices, we found a solution
        if u == n:
            return True
        
        # Optimization: If u is already forbidden all colors, prune immediately
        # 7 is 111 in binary, meaning all 3 colors are forbidden
        if forbidden_mask[u] == 7:
            return False
            
        # Try colors 0, 1, 2 in order (for lexicographically smallest)
        for c in range(3):
            # Check if color c is valid for u (not forbidden by neighbors < u)
            if (forbidden_mask[u] >> c) & 1:
                continue
            
            # Lookahead check:
            # If we assign color c to u, does it make any neighbor v > u impossible to color?
            # A neighbor v > u becomes impossible if (forbidden_mask[v] | (1 << c)) == 7.
            # Also we need to update forbidden_mask for neighbors v > u.
            
            # We need to track which neighbors' masks are changed to revert them on backtrack
            changed_neighbors = []
            possible = True
            
            # Iterate over neighbors of u
            for v in adj[u]:
                if v > u:
                    # Check if assigning c makes v impossible
                    # Note: forbidden_mask[v] currently contains colors from neighbors < v
                    # which includes neighbors < u. We are adding u's color c.
                    if (forbidden_mask[v] | (1 << c)) == 7:
                        possible = False
                        break
                    
                    # If valid, update forbidden_mask[v]
                    # We only add if c is not already forbidden for v
                    if not ((forbidden_mask[v] >> c) & 1):
                        forbidden_mask[v] |= (1 << c)
                        changed_neighbors.append(v)
            
            if possible:
                assignment[u] = c
                if backtrack(u + 1):
                    return True
                # Backtrack: undo assignment of u
                assignment[u] = 0
                # Revert changes to forbidden_mask
                for v in changed_neighbors:
                    forbidden_mask[v] &= ~(1 << c)
            else:
                # If possible is False, it means assigning c to u makes some v > u impossible.
                # We must revert any changes made to forbidden_mask in the loop before breaking.
                # Note: 'changed_neighbors' contains the updates made before 'break'.
                for v in changed_neighbors:
                    forbidden_mask[v] &= ~(1 << c)
        
        return False

    if backtrack(0):
        print("YES")
        # Convert 0-based colors to 1-based shifts
        print(" ".join(str(x + 1) for x in assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()