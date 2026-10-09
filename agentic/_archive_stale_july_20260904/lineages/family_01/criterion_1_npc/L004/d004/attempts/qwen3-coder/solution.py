def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    
    # Build adjacency list representation of the graph
    adj = [[] for _ in range(n)]
    index = 2
    edges = []
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        index += 2
    
    # Try all possible assignments of frequencies 1, 2, 3 to n emitters
    # We want the lexicographically smallest valid assignment
    # So we can use backtracking with pruning
    
    assignment = [0] * n  # 0 means unassigned
    
    def is_valid(vertex, freq):
        # Check if assigning 'freq' to 'vertex' violates any constraint
        for neighbor in adj[vertex]:
            if assignment[neighbor] != 0 and abs(assignment[neighbor] - freq) < 1:
                return False
        return True
    
    def backtrack(pos):
        if pos == n:
            return True
            
        # Try frequencies in order 1, 2, 3 for lexicographically smallest
        for freq in [1, 2, 3]:
            if is_valid(pos, freq):
                assignment[pos] = freq
                if backtrack(pos + 1):
                    return True
                assignment[pos] = 0  # Backtrack
                
        return False
    
    # Special case: no constraints
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()