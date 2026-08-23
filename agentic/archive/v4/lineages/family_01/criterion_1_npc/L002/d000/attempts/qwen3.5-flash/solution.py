import sys

# Increase recursion depth to handle N=40 safely
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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # color[i] stores the color assigned to person i (1, 2, or 3)
    # 0 means unassigned
    color = [0] * (n + 1)
    
    # count[i][c] stores the number of assigned neighbors of i that have color c
    # c is 1, 2, 3. Index 0 unused.
    # We only update this for unassigned vertices to optimize.
    count = [[0] * 4 for _ in range(n + 1)]
    
    def backtrack(u):
        # Base case: all vertices assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 to maintain lexicographical order
        for c in range(1, 4):
            # Check if color c is allowed for u (no neighbor has color c)
            if count[u][c] > 0:
                continue
            
            # Lookahead (Forward Checking):
            # Check if assigning c to u makes any unassigned neighbor "dead" (no valid colors left).
            # A neighbor v becomes dead if all 3 colors become forbidden.
            # Since v is unassigned, it currently has at most 2 forbidden colors.
            # We check if c is the 3rd forbidden color for any v.
            dead_neighbor_found = False
            for v in adj[u]:
                if color[v] == 0: # Only check unassigned neighbors
                    # Check if v has other 2 colors forbidden
                    if c == 1:
                        if count[v][2] > 0 and count[v][3] > 0:
                            dead_neighbor_found = True
                            break
                    elif c == 2:
                        if count[v][1] > 0 and count[v][3] > 0:
                            dead_neighbor_found = True
                            break
                    elif c == 3:
                        if count[v][1] > 0 and count[v][2] > 0:
                            dead_neighbor_found = True
                            break
            
            if not dead_neighbor_found:
                # Apply assignment
                color[u] = c
                # Update counts for neighbors
                for v in adj[u]:
                    if color[v] == 0:
                        count[v][c] += 1
                
                # Recurse
                if backtrack(u + 1):
                    return True
                
                # Backtrack
                color[u] = 0
                for v in adj[u]:
                    if color[v] == 0:
                        count[v][c] -= 1
        
        return False

    if backtrack(1):
        print("YES")
        print(*(color[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()