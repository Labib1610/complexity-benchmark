import sys

# Increase recursion depth to handle deep recursion if necessary
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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Remove duplicates in adjacency list if any
    for i in range(n):
        adj[i] = list(set(adj[i]))

    # colors: 0 = uncolored, 1..3 = colors
    colors = [0] * n 
    # forbidden: bitmask of forbidden colors. 1<<0, 1<<1, 1<<2 for colors 1, 2, 3
    forbidden = [0] * n 

    # We need to find the lexicographically smallest solution.
    # We assign colors to 0, 1, ..., n-1.
    # For each, try colors 0, 1, 2 (representing 1, 2, 3).
    
    def backtrack(u):
        # Check if current vertex u is already impossible
        # forbidden[u] == 7 means bits 0, 1, 2 are set, i.e., colors 1, 2, 3 are forbidden
        if forbidden[u] == 7:
            return False
            
        if u == n:
            return True
        
        # Try colors 0, 1, 2 (representing 1, 2, 3)
        for c in range(3):
            # Check if c is forbidden
            if (forbidden[u] >> c) & 1:
                continue
            
            # Assign color c to u (store as c+1)
            colors[u] = c + 1
            
            # Check feasibility for neighbors (Forward Checking)
            affected = []
            possible = True
            
            for v in adj[u]:
                if colors[v] == 0: # Only uncolored neighbors
                    if not ((forbidden[v] >> c) & 1):
                        old_f = forbidden[v]
                        new_f = old_f | (1 << c)
                        if new_f == 7:
                            possible = False
                            break
                        forbidden[v] = new_f
                        affected.append((v, old_f))
            
            if possible:
                if backtrack(u + 1):
                    return True
            
            # Backtrack: revert changes
            colors[u] = 0
            for v, old_f in affected:
                forbidden[v] = old_f
            
        return False

    if backtrack(0):
        print("YES")
        print(*(colors))
    else:
        print("NO")

if __name__ == '__main__':
    solve()