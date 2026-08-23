import sys

# Increase recursion depth to handle deep recursion trees if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # assignment[i] stores the color of vertex i (1, 2, 3)
    assignment = [0] * (n + 1)
    
    # counts[i][c] stores the number of assigned neighbors of i that have color c
    # i ranges from 1 to n, c from 1 to 3
    # Using 4 columns for 1-based indexing of colors
    counts = [[0] * 4 for _ in range(n + 1)]
    
    def backtrack(u):
        # Base case: all vertices assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to find lexicographically smallest assignment
        for c in (1, 2, 3):
            # Check if c is valid for u
            # It is invalid if any neighbor v < u has color c.
            # This is tracked in counts[u][c].
            if counts[u][c] > 0:
                continue
            
            # If valid, tentatively assign
            assignment[u] = c
            
            # Forward checking: update counts for neighbors v > u
            # We need to revert these changes if we backtrack
            blocked = False
            changed_neighbors = []
            
            for v in adj[u]:
                if v > u:
                    # Increment count for color c at neighbor v
                    counts[v][c] += 1
                    changed_neighbors.append(v)
                    
                    # Check if v is blocked (all colors forbidden by assigned neighbors)
                    if counts[v][1] > 0 and counts[v][2] > 0 and counts[v][3] > 0:
                        blocked = True
                        break
            
            if not blocked:
                if backtrack(u + 1):
                    return True
            
            # Revert changes to counts
            for v in changed_neighbors:
                counts[v][c] -= 1
            
            # Unassign
            assignment[u] = 0
            
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()