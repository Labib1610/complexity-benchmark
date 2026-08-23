import sys

# Increase recursion depth to handle deep recursion
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

    # Store edges in a set to handle duplicates and ensure u < v
    edges = set()
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            if u > v:
                u, v = v, u
            edges.add((u, v))
        except StopIteration:
            break
            
    # Build forward adjacency list
    # forward_adj[u] contains all neighbors v of u such that v > u
    # This optimization allows us to only check future constraints
    forward_adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        forward_adj[u].append(v)
    
    # s[i] stores the color assigned to vertex i (1-based index)
    # 0 indicates uncolored
    s = [0] * (n + 1)
    
    # avail[i] is a bitmask representing available colors for vertex i
    # Colors are 1, 2, 3, mapped to bits 0, 1, 2
    # Initial state: all colors available (1 | 2 | 4 = 7)
    avail = [7] * (n + 1)
    
    # Backtracking function to find lexicographically smallest assignment
    def backtrack(k):
        # Base case: all vertices colored
        if k > n:
            return True
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest
        for c in range(1, 4):
            # Check if color c is available for vertex k
            # avail[k] reflects constraints from already colored neighbors (1..k-1)
            if (avail[k] >> (c - 1)) & 1:
                s[k] = c
                
                # Forward Checking: Update available colors for future neighbors
                history = []
                possible = True
                
                # Iterate over neighbors v > k
                for v in forward_adj[k]:
                    # If color c is currently available for v, remove it
                    if (avail[v] >> (c - 1)) & 1:
                        history.append(v)
                        avail[v] &= ~(1 << (c - 1))
                        # If v has no available colors left, this branch is invalid
                        if avail[v] == 0:
                            possible = False
                            break
                
                if possible:
                    if backtrack(k + 1):
                        return True
                
                # Backtrack: Restore available colors
                for v in history:
                    avail[v] |= (1 << (c - 1))
                
                # Reset color for k
                s[k] = 0
        
        return False

    if backtrack(1):
        print("YES")
        print(*(s[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()